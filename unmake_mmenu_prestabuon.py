import sys
import os
from shutil import copyfile


def prepare_dec_tbl(path):
    tbl = {}

    lines = open(path, encoding='utf8').readlines()

    for line in lines:
        line = line.rstrip('\r\n')

        k, v = line.split('=', maxsplit=1)
        tbl[int(k, 16)] = v

    return tbl


def unmake(path, orig_tbl):
    f, e = os.path.splitext(path)

    new_name = '%s.txt' % f

    text = open(path, 'rb').read()
    orig = prepare_dec_tbl(orig_tbl)

    un = ''
    offset = 0
    prev_mod = -1
    while offset < len(text):
        mod = text[offset+0]
        mod_low = mod & 0x0F
        mod &= 0xF0

        if prev_mod != mod:
            un += '{%02X}' % mod
            prev_mod = mod

        val = (mod_low << 8) | text[offset+1]
        un += orig[val]
        offset += 2

    with open(new_name, 'w', encoding='utf8') as w:
        w.write('#%s#\n' % un)
        w.write(un)


def main(orig_tbl):
    bak_name = 'src/main_menu/prestabuon_text_or.bin'
    orig_name = 'src/main_menu/prestabuon_text.bin'

    if os.path.exists(bak_name):
        copyfile(bak_name, orig_name)

    unmake(orig_name, orig_tbl)


if __name__ == '__main__':
    main(sys.argv[1])
