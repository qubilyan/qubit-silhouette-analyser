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
model = torch.hub.load('pytorch/vision:v0.6.0', 'deeplabv3_resnet101', pretrained=True)
# Segment people only for the purpose of human silhouette extraction
people_class = 15

# Evaluate model
model.eval()
print ("Model has been loaded.")

blur = torch.FloatTensor([[[[1.0, 2.0, 1.0],[2.0, 4.0, 2.0],[1.0, 2.0, 1.0]]]]) / 16.0

# Use GPU if supported, for better performance
if torch.cuda.is_available():
	model.to('cuda')
	blur = blur.to('cuda')
	
# Apply preprocessing (normalization)
preprocess = transforms.Compose([
	transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to create segmentation mask
def makeSegMask(img):
    # Scale input frame
	frame_data = torch.FloatTensor( img ) / 255.0

	input_tensor = prepro