import os.path
import struct
import sys


def main(path):
    size = os.path.getsize(path) - 0x200

    with open(path, 'r+b') as rom:
        rom.seek(0x200)

        csum = 0

        while size > 0:
            w = rom.read(2)
            size -= 2

            csum += struct.unpack('>H', w)[0]

        csum &= 0xFFFF

        rom.seek(0x18E)
        rom.write(struct.pack('>H', csum))

        print('checksum fixed')


if __name__ == '__main__':
    main(sys.argv[1])
