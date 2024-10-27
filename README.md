### Nokia Assessment: Pranav Walimbe

## Introduction
Description: API service for warehouse space classification <br>
Name: Pranav Walimbe <br>
Email: pranav.walimbe@berkeley.edu 

## Codebase structure 
project-root/<br>
├── __src/__<br>
│&nbsp;&nbsp;&nbsp;&nbsp;├── __app/__<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── main.py <- script for defining API service<br>
│&nbsp;&nbsp;&nbsp;&nbsp;├── __checkpoints/__<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── model_ep_01.pth<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── model_ep_02.pth<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── model_ep_03.pth<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── model_ep_04.pth<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── model_ep_05.pth <- model checkpoint used in API<br>
│&nbsp;&nbsp;&nbsp;&nbsp;├── __training_data/__<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── images.zip<br>
│&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── labels.csv<br>
├── resnet18_training.ipynb <- script for fine-tuning ML model<br>
├── Assignment_Coop_2025_MLEng.pdf<br>
├── Dockerfile <- script for docker build<br>
└── requirements.txt




