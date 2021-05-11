import torch
from torch import nn
import torch.nn.functional as F
from torchvision import datasets, transforms, models


class Classifier(nn.Module):
    def __init__(self, input_size, hidden_units, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_units)
        self.output = nn.Linear(hidden_units, output_size)

        self.dropout = nn.Dropout(p=0.5)

    def forward(self, x):
        x = x.view(x.shape[0], -1)  # flatten tensor
        x = self.dropout(F.relu(self.fc1(x)))

        x = F.log_softmax(self.output(x), dim=1)
        return x