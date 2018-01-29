import hashlib
import os
import sys
BLOCKSIZE = 65536

def hash_files(root, fast):
    files = [os.path.join(dp, f) for dp, dn, fn in os.walk(root) for f in fn]
    for f in files:
        print("Reading ", f)
        try:
            hasher = hashlib.md5()
            with open(f, 'rb') as current_file:
                if fast:
                    buff = current_file.read(BLOCKSIZE)
                    hasher.update(buff)
                else:
                    block = 1
                    buff = current_file.read(BLOCKSIZE)
                    while len(buff) > 0:
                        print("\rReading Block...", block, end="")
                        block += 1
                        hasher.update(buff)
                        buff = current_file.read(BLOCKSIZE)
            with open("hashes.txt", 'ab') as h:
                h.write("{0} - {1}\r\n".format(f, hasher.hexdigest()).encode(encoding='utf_8', errors='replace'))
            print("\r", hasher.hexdigest())
        except PermissionError:
            print("Permission denied!")
            continue
        except FileNotFoundError:
            print("File not found!")
            continue
if len(sys.argv) > 2:
    if sys.argv[1] == "-f": # Fast Mode
        hash_files(sys.argv[1].lstrip('"').rstrip('"'), True)
elif len(sys.argv) > 1:
    hash_files(sys.argv[1].lstrip('"').rstrip('"'), False)
