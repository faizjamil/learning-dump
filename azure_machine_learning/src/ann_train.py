import torch
from torch import nn
from torch import optim
import argparse
import DataLoader
import nnModel

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='./categories', help='Path to images to train with')
parser.add_argument('--save_dir', type=str, default='./', help="path to save checkpoint")
parser.add_argument('--arch', type=str, default='densenet121', help='The architecture used to train model; '
                                                                    'densenet121')
parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate for the model')
parser.add_argument('--batch_size', type=int, default=64, help='size of batches for training')
parser.add_argument('--hidden_units', type=int, default=512, help='Number of hidden units in hidden layer')
parser.add_argument('--epochs', type=int, default=20, help='Number of training epochs to use')
parser.add_argument('--use_gpu', default=False, action='store_true', help="If you would like to use the GPU for "
                                                                          "training")

# changed default value of output_size to accomadate larger dataset																	  #
parser.add_argument('--output_size', type=int, default=63, help='Number of possible classes/categories for output')


args = parser.parse_args()

trainloader, validloader, testloader, train_data = DataLoader.load_image_data(args.dir, args.batch_size)

model = nnModel.create_model(args.arch, args.hidden_units, args.output_size)

if model != 0:
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), args.learning_rate)

    nnModel.train_model(model, trainloader, validloader, criterion, optimizer, args.epochs, args.use_gpu)
    nnModel.save_model(model, train_data, args.learning_rate, args.batch_size, args.epochs, criterion, optimizer,
                       args.arch, args.hidden_units, args.output_size)

    torch.cuda.empty_cache()

