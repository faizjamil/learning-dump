import nnModel
import torchvision
from torchvision import datasets, transforms, models
import JsonLoader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, help='The path to files you want to predict')
parser.add_argument('--checkpoint', type=str, default='checkpoint.pth', help='Path to the checkpoint pth file')
parser.add_argument('--top_k', type=int, default=1, help='Number of most likely classes to return from '
                                                         'predictions')
parser.add_argument('--cat_names', type=str, default='./cat_to_name.json', help='Json file that loads '
                                                                                'class/category names')
parser.add_argument('--use_gpu', default=False, action='store_true')

args = parser.parse_args()
model = nnModel.load_model(args.checkpoint, args.use_gpu)
categories = JsonLoader.load_json(args.cat_names)

probs, classes = nnModel.predict(categories, args.dir, model, args.use_gpu, args.top_k)
print(probs)
print(classes)
