import os
from shutil import copyfile


def unmake(path):
    os.system('python %s dn %s' % (os.path.abspath('src/kens/kens_funcs.py'), os.path.abspath(path)))


def main():
    root = './src/fonts/'
    for path in os.listdir(root):
        if path.endswith('_or.bin'):
            path = os.path.join(root, path)
            copyfile(path, path.replace('_or.bin', '.bin'))

    for path in os.listdir(root):
        if path.endswith('.bin') and not path.endswith('_or.bin') and not path.endswith('_new.bin') and not path.endswith('_dec.bin'):
            path = os.path.join(root, path)
            unmake(path)


if __name__ == '__main__':
    main()
