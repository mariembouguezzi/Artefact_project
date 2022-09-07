from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np



model = None

class_names = ["blast__rice", "brown__rice", "healthy__rice"]

BUCKET_NAME = "rice-disease-bucket" # Here you need to put the name of your GCP bucket


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "models/rice_disease.h5",
            "/tmp/rice_disease.h5",
        )
        model = tf.keras.models.load_model("/tmp/rice_disease.h5")


    image = request.files["file"]


    image = np.array(Image.open(image).convert("RGB") )

    # image = image/255 # normalize the image in 0 to 1 range
    
    tensor_from_img = tf.convert_to_tensor(image)

    tensor_image= tf.expand_dims(tensor_from_img, 0)

    predictions = model.predict(tensor_image)

    print("Predictions:",predictions) 

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}

