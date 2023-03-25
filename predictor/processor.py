import io
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf

from expert.models import Activation


def preprocess_image(image):
    # Resize the image while keeping the aspect ratio
    w, h = image.size
    ratio = 224.0 / max(w, h)
    new_size = (int(ratio * w), int(ratio * h))
    image = image.resize(new_size)
    # Add padding if necessary
    delta_w = 224 - new_size[0]
    delta_h = 224 - new_size[1]
    padding = (
        delta_w // 2,
        delta_h // 2,
        delta_w - (delta_w // 2),
        delta_h - (delta_h // 2),
    )
    image = ImageOps.expand(image, padding)
    # Convert to numpy array
    image = np.array(image)
    image = image / 255.0
    if len(image.shape) == 2:
        image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
    elif image.shape[2] == 4:
        image = image[:, :, :3]
    image = np.expand_dims(image, axis=0)
    return image


def predict(path):
    # Load the image from file
    image = Image.open(path)
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Load the trained model
    activation = Activation.objects.last()
    if activation is None:
        raise Exception("x cannot be negative")
    
    model_path = activation.model.file.path
    model = tf.keras.models.load_model(model_path)
    # Make a prediction
    predictions = model.predict(processed_image)
    # Convert the predictions to class names
    class_names = ["MildDemented", "NonDemented", "VeryMildDemented"]
    predicted_class = class_names[np.argmax(predictions)]
    # Get the percentage of each label
    percentage = {}
    for i in range(len(class_names)):
        percentage[class_names[i]] = round(float(predictions[0][i]) * 100, 2)

    return predicted_class, percentage
