### Nokia Assessment: Pranav Walimbe

## Introduction
Description: API service for warehouse space classification <br>
Name: Pranav Walimbe <br>
Email: pranav.walimbe@berkeley.edu 

## Codebase structure 
project-root/<br>
├── src/<br>
│   ├── app/<br>
│   │   └── main.py <- script for defining API service<br>
│   ├── checkpoints/<br>
│   │   ├── model_ep_01.pth<br>
│   │   ├── model_ep_02.pth<br>
│   │   ├── model_ep_03.pth<br>
│   │   ├── model_ep_04.pth<br>
│   │   └── model_ep_05.pth <- model checkpoint used in API<br>
│   ├── models/<br>
│   │──resnet18_training.ipynb <- script for fine-tuning ML model <br>
│   ├── training_data/<br> 
│   │   ├── images.zip<br>
│   │   └── labels.csv<br>
├── Assignment_Coop_2025_MLEng.pdf<br>
├── Dockerfile <- script for docker build<br>
└── requirements.txt



