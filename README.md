## Nokia Assessment: Pranav Walimbe

## Introduction
Description: API service for warehouse space classification <br>
Name: Pranav Walimbe <br>
Email: pranav.walimbe@berkeley.edu 

## Codebase structure 
- **src/**
  - **app/**
    - `main.py`: Script for defining the API service
  - **checkpoints/**
    - `model_ep_01.pth`
    - `model_ep_02.pth`
    - `model_ep_03.pth`
    - `model_ep_04.pth`
    - `model_ep_05.pth`: Checkpoint used in the API
  - **training_data/**
    - `images.zip`
    - `labels.csv`
- `resnet18_training.ipynb`: Script for fine-tuning ML model
- `Assignment_Coop_2025_MLEng.pdf`
- `Dockerfile`: Script for Docker build
- `requirements.txt`

## Model Training + Performance 
- **Architecture**: ResNet18
  - Finetuned pretrained ResNet18 model due to strong balance between computational efficiency (less layers than most pretrained vision models) and residual connection architecture enabling high performance on downstream tasks
  
- **Dataset**:
  - Dataset split: Used scaled class weights in loss function to address ~70/30 class imbalance in dataset
  - Augmentation: Used various techniques (normalization, color jitter, gaussian blur, random rotate) to increase dataset variability and quality 
  
- **Performance**:
  - Test accuracy: 100% (70-30 train-test split) 
  - Train accuracy: 100%
  - Recall: 1.00
  - Precision: 1.00
  - Training Duration: ~4 minutes of training using T4 GPU
  epoch-based accuracies viewable in training script 

## Usage

1. clone repository:
   
   `git clone git@github.com:pranav-1077/nokia-takehome.git`

2. enter repository:
   
   `cd nokia-takehome`

3. build docker image:
   
   `docker build -t <build name> .`

4. run container:
   
   `docker run -d -p 8080:8080 <build name>`

5. image API call:
   
   `curl -X POST 'http://localhost:8080/classify' -H 'Content-Type: multipart/form-data' -F 'image=@/image_path.jpg'`

   sample output: {'class':'filled'}
   
   author API call: 
   
   `curl -X GET 'http://localhost:8080/author'`

   sample output: {'author':'pranav.walimbe@berkeley.edu'}

## Further Information

Model is used in quantized form when called through API for optimized inference efficiency on CPU. Container is optimized for CPU usage rather than GPU compatibility. 

## Acknowledgments

The ResNet18 model finetuned in this project is based on the work of Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Their paper, **"Deep Residual Learning for Image Recognition"**

 

   



