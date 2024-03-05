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
    for ch in text:
        if ch == 255:
            break

        un += orig[ch]

    if not os.path.exists(new_name):
        with open(new_name, 'w', encoding='utf8') as w:
            w.write('#%s#\n' % un)
            w.write(un)


def main(orig_tbl):
    root = './src/cutscenes/'
    for path in os.listdir(root):
        if path.endswith('_or.bin'):
            path = os.path.join(root, path)
            copyfile(path, path.replace('_or.bin', '.bin'))

    for path in os.listdir(root):
        if path.endswith('.bin') and not path.endswith('_or.bin'):
            path = os.path.join(root, path)
            unmake(path, orig_tbl)


if __name__ == '__main__':
    main(sys.argv[1])
