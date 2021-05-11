import os
import nnModel
import torchvision
from torchvision import datasets, transforms, models
import JsonLoader
import argparse
from fnmatch import fnmatch


# Variables for predict.py script
# path to the file you want to predict
file_dir = ""
# Path to the checkpoint.pth file that pytorch uses
checkpoint = "checkpoint.pth"
# JSON file that loads class/category names
cat_names = "./cat_to_name.json"
# uses GPU acceleration (CUDA) to speed up prediction
use_gpu = False
# Number of most likely classes to return from prediction
top_k = 1

# this assumes the script runs in the same directory as the other ANN scripts
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='', help='Path to images to sort, they can be either at the root of this directory or in a subdirectory')
args = parser.parse_args()

#root = args.dir
root = "E:\\Downloads\\01-Library\\script_testing\\c10\\"
pattern = "*.jpg"
images = []
count = 0


for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            src = os.path.join(path,name)
            # file_dir = os.path.join(path,name)
            # model = nnModel.load_model(checkpoint, use_gpu)
            # categories = JsonLoader.load_json(cat_names)

            # probs, classes = nnModel.predict(categories, file_dir, model, use_gpu, top_k)
            # print(probs)
            # print(classes)

            dst = os.path.join(path,str(count)) + ".jpg"
            
            print(src)
            #print (os.path.join(path, name))
            #images.append(os.path.join(path, name))
            count = count + 1

# for name in images:
#     print(name)

