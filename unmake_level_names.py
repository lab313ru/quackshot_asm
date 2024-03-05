import sys
import os
import glob
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

    with open(new_name, 'w', encoding='utf8') as w:
        w.write('#%s#\n' % un)
        w.write(un)


def main(orig_tbl):
    root = './src/levels/'
    for path in glob.iglob(root + '**/name_or.bin'):
        copyfile(path, path.replace('_or.bin', '.bin'))

    for path in glob.iglob(root + '**/name.bin'):
        unmake(path, orig_tbl)
            


if __name__ == '__main__':
    main(sys.argv[1])
