import tensorflow as tf
from PIL import Image
import numpy as np

IMAGE_SHAPE = (224, 224)
MODEL_PATH = './models/basic_classifier.h5'

def use_model(path):

    path = '.' + path
    
    model = tf.keras.models.load_model(MODEL_PATH)

    pic = Image.open(path).resize((IMAGE_SHAPE[0], IMAGE_SHAPE[1]))
    
    prediction = model.predict(np.expand_dims(pic, axis=0))[0]
    lst = [i for i,prob in enumerate(prediction) if prob > 0.5][0]
    
    return 'Organic' if lst==0 else 'Recyclable'