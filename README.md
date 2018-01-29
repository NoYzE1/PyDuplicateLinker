# PyDuplicateLinker
A python script to recursively create md5 hashes from files in a folder and a linker-script to hardlink duplicate files.

Usage:
Running hash_files.py \<rootDir\> creates a hashes.txt containing the files and hashes.
Running duplicate_linker.py replaces duplicate files with hardlinks reading from the hashes.txt.

Use at own risk.
