import sys
import os
import glob
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

    offset = 0
    mod = 0
    mk = bytearray()
    while offset < len(text):
        if text[offset] == '{':
            mod = int(text[offset+1:offset+3], 16)
            offset += 4

        mk.append(mod)

        ch = text[offset:offset+1]
        offset += 1
        
        mk.append(new[ch])

    if not os.path.exists(bak_name):
        copyfile(new_name, bak_name)

    with open(new_name, 'wb') as w:
        w.write(bytes(mk))


def main(new_tbl):
    root = './src/levels/'
    for path in glob.iglob(root + '**/name.txt', recursive=True):
        make(path, new_tbl)


if __name__ == '__main__':
    main(sys.argv[1])
