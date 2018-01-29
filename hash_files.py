import hashlib
import os
import sys
BLOCKSIZE = 65536

def h(r):
    files = [os.path.join(dp, f) for dp, dn, fn in os.walk(r) for f in fn]
    for f in files:
        hasher = hashlib.md5()
        with open(f, 'rb') as g:
            b = g.read(BLOCKSIZE)
            while len(b) > 0:
                hasher.update(b)
                b = g.read(BLOCKSIZE)
        with open("hashes.txt", 'ab') as h:
            h.write("{0} - {1}\r\n".format(f, hasher.hexdigest()).encode(encoding='utf_8', errors='replace'))
        print("{0} - {1}".format(f, hasher.hexdigest()).encode(encoding='utf_8', errors='replace'))

if len(sys.argv) > 1:
    h(sys.argv[1].lstrip('"').rstrip('"'))
