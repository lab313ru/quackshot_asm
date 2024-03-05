import sys
import os
from shutil import copyfile


def prepare_enc_tbl(path):
    tbl = {}

    lines = open(path, encoding='utf8').readlines()

    for line in lines:
        line = line.rstrip('\r\n')

        k, v = line.split('=', maxsplit=1)
        tbl[v] = int(k, 16)

    return tbl


def make(path, new_tbl):
    f, _ = os.path.splitext(path)

    new_name = '%s.bin' % f
    bak_name = '%s_or.bin' % f

    f_or = open(path, encoding='utf8')
    f_or.readline()  # skip original string
    text = f_or.read()
    f_or.close()

    new = prepare_enc_tbl(new_tbl)

    mk = bytearray()
    for ch in text:
        mk.append(new[ch])

    mk.append(0xff)

    if not os.path.exists(bak_name):
        copyfile(new_name, bak_name)

    with open(new_name, 'wb') as w:
        w.write(bytes(mk))


def main(new_tbl):
    root = './src/cutscenes/'
    for path in os.listdir(root):
        if path.endswith('.txt'):
            path = os.path.join(root, path)
            make(path, new_tbl)


if __name__ == '__main__':
    main(sys.argv[1])
