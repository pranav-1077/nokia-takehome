from fastapi import FastAPI, File, UploadFile, Request
import torch
from torchvision import models, transforms
from PIL import Image
import io
import base64

app = FastAPI()

# load in fine tuned resnet18 model 
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 2)  
model.load_state_dict(torch.load("src/checkpoints/model_ep_05.pth", map_location=torch.device('cpu')))
model.eval()

# quantize model for optimized cpu inference 
model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8  
)

# define image transformation
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# class mapping for model output
class_labels = {0: 'empty', 1: 'filled'}

@app.get("/author")
def get_author():

    return {
        "author": "pranav.walimbe@berkeley.edu"
    }

@app.post("/classify")
async def post_classify(request: Request):

    try:
        # Parse image from form
        form = await request.form()
        image_file = form['image']
        image_bytes = await image_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        image = image.convert("RGB")  

        # transform image
        input_tensor = preprocess(image).unsqueeze(0)  

        # Perform inference
        with torch.no_grad():
            output = model(input_tensor)

        _, predicted_class_idx = torch.max(output, 1)
        predicted_label = class_labels[predicted_class_idx.item()]

        return {"class": predicted_label}

    except Exception as e:
        print("Internal Server Error:", e)
        return {"error": "Internal Server Error: " + str(e)}