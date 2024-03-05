import json
import os
import struct
import sys
from shutil import copyfile


DIALOGS_START = 0xFFCE00


def prepare_dec_tbl(path):
    tbl = {}

    lines = open(path, encoding='utf8').readlines()

    for line in lines:
        line = line.rstrip('\r\n')

        k, v = line.split('=', maxsplit=1)
        tbl[int(k, 16)] = v

    return tbl


def vram_write_addr(val):
    return (((val & 3) << 14) | ((val & 0x3FFF0000) >> 16)) & 0xFFFF


def decode_vram(w, h, val):
    plane_addr = (val & 0xE000)
    val &= 0x1FFF
    val >>= 1
    x = (val % 0x40)
    y = (val // 0x40)

    return {'w': w+1, 'h': h+1, 'x': x, 'y': y, 'addr': '0x%04X' % plane_addr}


def decode_rect(buf, offset):
    vram, w, h = struct.unpack_from('>HHH', buf, offset)
    return decode_vram(w, h, vram_write_addr((vram << 16) | 0x0003))


def decode_dialog(buf, offset, rect, orig_tbl):
    orig = prepare_dec_tbl(orig_tbl)

    color = 'grey' if (buf[offset] == 1) else 'green'
    offset += 1

    max_h = rect['h']
    max_w = rect['w']

    text = ''

    for h in range(max_h - 2):
        line_len = 0

        for w in range(max_w - 2):
            ch = buf[offset]
            offset += 1

            if ch != 0xFF:
                text += orig[ch]
                line_len += 1
            else:
                text += '\n'
                break

        if line_len == (max_w - 2) and h + 1 < (max_h - 2):
            text += '\n'

    # text = text.rstrip()

    return {'text': {'color': color, 'lines': text.split('\n')}}


def decode_dialogs(path, orig_tbl):
    buf = open(path, 'rb').read()

    off0, off2 = struct.unpack_from('>HH', buf)

    dialogs = []

    dialogs_count = (off2 - off0) // 4

    for i in range(dialogs_count):
        ridx, dialog_off = struct.unpack_from('>HH', buf, off0 + i * 4)

        rect = decode_rect(buf, off2 + (ridx-1) * 6)

        screens_count = struct.unpack_from('>H', buf, off0 + dialog_off)[0] + 1

        screens = []
        for screen_idx in range(screens_count):
            s_dialog_off = struct.unpack_from('>I', buf, off0 + dialog_off + 2 + screen_idx * 4)[0]

            if s_dialog_off == 0 or s_dialog_off < DIALOGS_START:
                continue

            screens.append(decode_dialog(buf, s_dialog_off - DIALOGS_START, rect, orig_tbl))

        dialogs.append({'rect': rect, 'screens': screens})

    return dialogs


def unmake(path, orig_tbl):
    orig_bin = os.path.abspath(path)
    os.system('python %s dk %s' % (os.path.abspath('src/kens/kens_funcs.py'), orig_bin))

    f, e = os.path.splitext(orig_bin)
    dec_bin = '%s_dec%s' % (f, e)
    dec_txt = '%s_new.txt' % f

    dialogs = decode_dialogs(dec_bin, orig_tbl)
    os.remove(dec_bin)

    with open(dec_txt, 'w', encoding='utf8') as w:
        json.dump(dialogs, w, ensure_ascii=False, indent=4)


def main(orig_tbl):
    unmake('src/dialogs/kosinski_dialogs.bin', orig_tbl)


if __name__ == '__main__':
    main(sys.argv[1])
