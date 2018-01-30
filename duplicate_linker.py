import os
import sys

def link_duplicates():
    with open("hashes.txt", 'r', encoding='utf_8', errors='replace') as hashfile:
        hashmap = []
        for f in hashfile:
            filename = "".join(f.rsplit(" - ", 1)[0:-1])
            hash_value = f.rsplit(" - ", 1)[-1]
            hashmap.append((filename, hash_value))
    for i in range(len(hashmap)):
        for j in range(i+1, len(hashmap)):
            if hashmap[i][1] == hashmap[j][1]:
                if os.stat(hashmap[i][0]).st_ino != os.stat(hashmap[j][0]).st_ino:
                    print("Duplicate found! ", hashmap[i][0], hashmap[j][0])
                    print("Deleting duplicate...", end="")
                    try:
                        os.remove(hashmap[j][0])
                        print("Linking...", end="")
                        os.link(hashmap[i][0], hashmap[j][0])
                        print("OK.")
                    except FileNotFoundError:
                        print("File not found!")
                    except PermissionError:
                        print("No permission!")
                    except OSError:
                        print("OS Error!")
link_duplicates()
