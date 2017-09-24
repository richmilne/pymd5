#! /usr/bin/env python
# Usually placed in /usr/bin

import os
import sys
import hashlib

chunk_size = 1024*1024

def hash_file(f):

    digest = hashlib.md5()
    handle = open(f, 'rb')

    chunk = handle.read(chunk_size)
    while chunk != '':
        digest.update(chunk)
        chunk = handle.read(chunk_size)
        
    handle.close()
    return digest.hexdigest()

def calculate_hashes(path):

    length = len(path) + 1

    for root, dirs, files in os.walk(path):
        dirs.sort()
        files.sort()
        for f in files:
            file_path = os.path.join(root, f)
            rel_path = file_path[length:]
            digest = hash_file(file_path)
            sys.stdout.write('%s *%s\n' % (digest, rel_path))
            sys.stdout.flush()

if __name__ == '__main__':

    path = os.path.abspath(sys.argv[1])
    if not(os.path.isdir(path)):
        print 'Invalid directory:', path
        sys.exit(1)
        
    calculate_hashes(path)
