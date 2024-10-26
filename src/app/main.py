from fastapi import FastAPI, File, UploadFile, Request
import torch
from torchvision import models, transforms
from PIL import Image
import io
import base64

app = FastAPI()

# load in fine tuned resnet18 model 
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 2)  # Adjust to your number of output classes
model.load_state_dict(torch.load("src/checkpoints/model_ep_05.pth", map_location=torch.device('cpu')))
model.eval()

# define image transformation
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# class mapping for model output
class_labels = {0: 'empty', 1: 'filled'}

# TODO: Implement a GET /author endpoint here
@app.get("/author")
def get_author():

    return {
        "author": "pranav.walimbe@berkeley.edu"
    }

# TODO: Implement a POST /classify endpoint here
@app.post("/classify")
async def post_classify(request: Request):

    form = await request.form()
    image_file = form['image']
    image_bytes = await image_file.read()
    image = Image.open(io.BytesIO(image_bytes))
    input_tensor = preprocess(image).unsqueeze(0)  

    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)
    _, predicted_class_idx = torch.max(output, 1)
    predicted_label = class_labels[predicted_class_idx.item()]

    return { 
        "class": predicted_label
    }