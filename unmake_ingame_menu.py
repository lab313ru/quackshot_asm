import os
import sys
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

        if prev_mod != mod:
            un += '{%02X}' % mod
            prev_mod = mod

        un += orig[text[offset+1]]
        offset += 2

    if not os.path.exists(new_name):
        with open(new_name, 'w', encoding='utf8') as w:
            w.write('#%s#\n' % un)
            w.write(un)


def main(orig_tbl):
    root = './src/ingame_menu/'
    for path in os.listdir(root):
        if path.endswith('_or.bin'):
            path = os.path.join(root, path)
            copyfile(path, path.replace('_or.bin', '.bin'))

    for path in os.listdir(root):
        if path.endswith('.bin') and not path.endswith('_or.bin') and not path.endswith('_new.bin') and not path.endswith('_dec.bin') and not path.startswith('mapping'):
            path = os.path.join(root, path)
            unmake(path, orig_tbl)


if __name__ == '__main__':
    main(sys.argv[1])
