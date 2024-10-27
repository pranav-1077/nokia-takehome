### Nokia Assessment: Pranav Walimbe

## Introduction
Description: API service for warehouse space classification <br>
Name: Pranav Walimbe <br>
Email: pranav.walimbe@berkeley.edu 

## Codebase structure 
project-root/
├── src/
│   ├── app/
│   │   └── main.py <- script for defining API service
│   ├── checkpoints/
│   │   ├── model_ep_01.pth
│   │   ├── model_ep_02.pth
│   │   ├── model_ep_03.pth
│   │   ├── model_ep_04.pth
│   │   └── model_ep_05.pth <- model checkpoint used in API
│   ├── training_data/
│   │   ├── images.zip
│   │   └── labels.csv
├── resnet18_training.ipynb <- script for fine-tuning ML model
├── Assignment_Coop_2025_MLEng.pdf
├── Dockerfile <- script for docker build
└── requirements.txt



