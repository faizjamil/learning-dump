import matplotlib.pyplot as plt
import torch
from torch import nn
from torch import optim
import torchvision
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import numpy as np
import Classifier
import ProcessImage
from PIL import Image


def create_model(arch, hidden_units, output_size):
    print('Creating your model.')

    if arch == 'densenet121':
        model = models.densenet121(pretrained=True)
        input_size = 1024
    else:
        return 0

    for param in model.parameters():
        param.requires_grad = False

    model.classifier = Classifier.Classifier(input_size, hidden_units, output_size)

    print("Model created")
    return model


def train_model(model, trainloader, validloader, criterion, optimizer, epochs, use_gpu):
    print('Training..')

    if use_gpu:
        device = torch.device('cuda' if use_gpu else 'cpu')
        if device == 'cuda':
            print('Using gpu')
        elif device == 'cpu':
            print('Sorry, there is no CUDA capable device available, using CPU')
    else:
        device = torch.device('cpu')
        print('Using CPU')

    model.to(device)

    train_losses, valid_losses = [], []
    for e in range(epochs):
        model.train()
        running_loss = 0
        for images, labels in trainloader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            logps = model.forward(images)
            loss = criterion(logps, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        else:
            valid_loss = 0
            accuracy = 0
            model.eval()
            with torch.no_grad():
                for images, labels, in validloader:
                    images, labels = images.to(device), labels.to(device)
                    logps = model.forward(images)
                    valid_loss += criterion(logps, labels)

                    # Calculate accuracy
                    ps = torch.exp(logps)
                    top_p, top_class = ps.topk(1, dim=1)
                    equality = top_class == labels.view(*top_class.shape)
                    accuracy += torch.mean(equality.type(torch.FloatTensor))

            model.train()
            train_losses.append(running_loss / len(trainloader))
            valid_losses.append(valid_loss / len(validloader))
            print("Epoch: {}/{}.. ".format(e + 1, epochs),
                  "Training Loss: {:.3f}.. ".format(running_loss / len(trainloader)),
                  "Validation Loss: {:.3f}.. ".format(valid_loss / len(validloader)),
                  "Accuracy: {:.3f}".format(accuracy / len(validloader)))


def save_model(model, train_data, learning_rate, batch_size, epochs, criterion, optimizer, arch, hidden_units, output_size):
    print('Saving model..')
    model.class_to_idx = train_data.class_to_idx
    if arch == 'densenet121':
        input_size = 1024

    checkpoint = {'input_size': input_size,
                  'output_size': output_size,
                  'hidden_units': hidden_units,
                  'arch': arch,
                  'batch_size': batch_size,
                  'epochs': epochs,
                  'learning_rate': learning_rate,
                  'classifier': model.classifier,
                  'criterion': criterion,
                  'optimizer': optimizer,
                  'state_dict': model.state_dict(),
                  'class_to_idx': model.class_to_idx}
    torch.save(checkpoint, 'checkpoint.pth')
    print('Model Saved!')


def load_model(checkpoint_path, use_gpu):
    print("Loading.")
    if use_gpu:
        checkpoint = torch.load(checkpoint_path)
    else:
        checkpoint = torch.load(checkpoint_path, map_location=torch.device('cpu'))
    model = getattr(torchvision.models, checkpoint['arch'])(pretrained=True)
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']

    for param in model.parameters():
        param.requires_grad = False

    print('Loaded!')
    return model


def predict(categories, image_path, model, use_gpu, topk):
    if use_gpu:
        device = torch.device('cuda' if use_gpu else 'cpu')
        if device == 'cuda':
            print('Using gpu')
        elif device == 'cpu':
            print('Sorry, there is no CUDA capable device available, using CPU')
    else:
        device = torch.device('cpu')
        print('Using CPU')

    model.to(device)
    model.eval()
    image_pil = Image.open(image_path)
    image = ProcessImage.process_image(image_pil)
    image.unsqueeze_(0)
    image.to(device)
    with torch.no_grad():
        output = model(image)
        ps = torch.exp(output)
        probs, indices = ps.topk(topk)
        probs = probs.cpu().numpy()[0]
        indices = indices.cpu().numpy()[0]

        idx_to_class = {v: k for k, v in model.class_to_idx.items()}
        classes = [idx_to_class[x] for x in indices]
        labels = []
        for c in classes:
            labels.append(categories[c])

        return probs, labels
