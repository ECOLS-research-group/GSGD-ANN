import numpy as np
import pandas as pd
import torch
import torchmetrics
import copy
from getError import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def validate(inputVal, network, actual, loss_function, NC):
    xval = inputVal.to(device = device)
    actual = actual.to(device = device)
    
    #get predicted value
    predicted = get_predictions(network, xval)
    
    SR = torchmetrics.functional.accuracy(predicted, actual,num_classes=NC)
    m = nn.Sigmoid()
    loss = loss_function(m(predicted), actual)
    E = loss.item()   
    return SR, E  

def get_predictions(network, xts):
    network.zero_grad()
    pred_y = network(xts)
    return pred_y

