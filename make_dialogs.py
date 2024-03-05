import json
import os
import struct
import sys


DIALOGS_START = 0xFFCE00


def make_bin(path):
    or_name = path.replace('_tmp.txt', '.bin')
    f, _ = os.path.splitext(or_name)

    os.system('python %s ck %s' % (os.path.abspath('src/kens/kens_funcs.py'), os.path.abspath(path)))

    new_name = path.replace('_tmp.txt', '_tmp_enc.txt')
    os.replace(new_name, or_name)


def prepare_enc_tbl(path):
    tbl = {}

    lines = open(path, encoding='utf8').readlines()

    for line in lines:
        line = line.rstrip('\r\n')

        k, v = line.split('=', maxsplit=1)
        tbl[v] = int(k, 16)

    return tbl


def encode_vram(x, y, plane_addr):
    vram_addr = (y * 0x40 + x) & 0xFFFF
    vram_addr <<= 1
    vram_addr &= 0x1FFF
    vram_addr |= (plane_addr & 0xE000) & 0xFFFF
    return vram_addr


def vram_write_addr(val):
    return ((val >> 14) & 3) | ((val << 16) & 0x3FFF0000) | (1 << 30)


def encode_rect(rect):
    vram_addr = encode_vram(rect['x'], rect['y'], int(rect['addr'], 16))
    vram = (vram_write_addr(vram_addr) >> 16) & 0xFFFF
    w = rect['w'] - 1
    h = rect['h'] - 1

    return struct.pack('>HHH', vram, w, h)


def encode_text(buf, new, rect):
    res = bytearray(b'\x01' if buf['color'] == 'grey' else b'\x00')

    lines = buf['lines']

    for line in lines:
        line_len = 0

        for ch in line:
            res.append(new[ch])
            line_len += 1

        if line_len < (rect['w'] - 2):
            res.append(0xFF)

    res = bytes(res)
    if res[-2:] == b'\xFF\xFF':
        res = res[:-1]

    return res


def encode_dialogs(dialogs, new_tbl):
    orig_name = 'src/dialogs/kosinski_dialogs_tmp.txt'

    new = prepare_enc_tbl(new_tbl)

    rects = []

    for dialog in dialogs:
        rect_buf = encode_rect(dialog['rect'])

        if rect_buf not in rects:
            rects.append(rect_buf)

        dialog['rect_idx'] = rects.index(rect_buf) + 1

    res = struct.pack('>HH', 4, 4+len(dialogs)*4)  # off0, off2
    res += struct.pack('>HH', 0, 0) * len(dialogs)  # rect_idx, dialog offset

    for rect in rects:
        res += rect

    texts = {}

    for i, dialog in enumerate(dialogs):
        rect_idx = dialog['rect_idx']

        res = bytearray(res)
        struct.pack_into('>HH', res, 4 + i * 4, rect_idx, len(res)-4)
        res = bytes(res)

        if i == 0:
            continue

        screens = dialog['screens']

        if len(screens) == 0:
            res += struct.pack('>H', 0)
        else:
            res += struct.pack('>H', len(screens)-1)

        curr_off = len(res)

        res += struct.pack('>I', 0) * len(screens)

        for j, screen in enumerate(screens):
            text = encode_text(screen['text'], new, dialog['rect'])

            screen_off = DIALOGS_START + len(res)
            found = False

            if text not in texts:
                texts[text] = screen_off
            else:
                screen_off = texts[text]
                found = True

            res = bytearray(res)
            struct.pack_into('>I', res, curr_off + j * 4, screen_off)
            res = bytes(res)

            if not found:
                res += text

                if len(res) & 1:
                    res += b'\x00'

    with open(orig_name, 'wb') as w:
        w.write(res)


def make_txt(path, new_tbl):
    with open(path, encoding='utf8') as f:
        dialogs = json.load(f)

        encode_dialogs(dialogs, new_tbl)


def main(new_tbl):
    make_txt('src/dialogs/kosinski_dialogs_new.txt', new_tbl)
    make_bin('src/dialogs/kosinski_dialogs_tmp.txt')
    os.remove('src/dialogs/kosinski_dialogs_tmp.txt')


if __name__ == '__main__':
    main(sys.argv[1])
