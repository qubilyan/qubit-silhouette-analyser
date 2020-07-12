##################################################
## Deeplabv3 Silhouette Extractor
##################################################
## Takes video file as input, generates silhouette
## mask and saves it.
##################################################
## Author: Jordan Kee
## Date: 2020-07-16
##################################################

from __future__ import print_function
import cv2
import torch
import torch.nn.functional as F
from torchvision import transforms
import time

# Load pretrained model
model = torch.hub.load('pytorch/vision:v0.6.0', 'de