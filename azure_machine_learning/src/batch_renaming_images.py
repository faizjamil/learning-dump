import os
import random
import argparse
from fnmatch import fnmatch

parser = argparse.ArgumentParser()

parser.add_argument('--dir', type=str, default='', help='Path to images to sort, they can be either at the root of this directory or in a subdirectory')

args = parser.parse_args()

random.seed()
root = args.dir
print(root)
#root = "E:\\Downloads\\01-Library\\script_testing\\c10\\"
pattern = "*.jpg"
count = random.getrandbits(14)
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            src = os.path.join(path,name)
            dst = os.path.join(path,str(count)) + ".jpg"
            
            print(dst)
            #os.rename(src, dst)
            #print (os.path.join(path, name))
            count = count + 1
