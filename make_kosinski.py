import os
from shutil import copyfile


def make(path):
    or_name = path.replace('_new.bin', '.bin')
    f, _ = os.path.splitext(or_name)

    bak_name = '%s_or.bin' % f

    if not os.path.exists(bak_name):
        copyfile(or_name, bak_name)

    os.system('python %s ck %s' % (os.path.abspath('src/kens/kens_funcs.py'), os.path.abspath(path)))

    new_name = path.replace('_new.bin', '_new_enc.bin')
    os.replace(new_name, or_name)


def main():
    root = './src/kosinski/'
    for path in os.listdir(root):
        if path.endswith('_new.bin'):
            path = os.path.join(root, path)
            make(path)


if __name__ == '__main__':
    main()
