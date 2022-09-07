from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

app = FastAPI()

origins = [
    os.environ['API_URL_1'],
    os.environ['API_URL_2'],
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("/opt/saved_models")

CLASS_NAMES = ["Blast rice", "Brown rice", "Healthy rice"]

@app.get("/project_message")
async def project_message():
    return "Hello, this is our final ARTFECAT project : Rice disease classification ! Author : Meriem BOUGUEZZI :)"

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize((224,224))
    image = np.array(image)
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())

    # tensor_from_img = tf.convert_to_tensor(image)

    img_tensor = tf.expand_dims(image, 0)

    predictions = MODEL.predict(img_tensor)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {    
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

    
