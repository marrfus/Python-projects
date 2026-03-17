import tensorflow as tf
import numpy as np
from keras.preprocessing import image
from keras import models


MODEL_PATH="hunde_katzen_model.h5"
IMG_SIZE=(160,160)
IMAGE_TO_PREDICT = r"\Users\MariaSizintseva\Desktop\MariaDocs\marrfusProgBackup\python\ML\tensor_scikit\my_ann_prj\image.png"

# class_names = ["hunde","katzen"]
class_names = ["male","female"]

model = models.load_model(MODEL_PATH)
print("Modell geladen.")

img = image.load_img(IMAGE_TO_PREDICT, target_size=IMG_SIZE)
img_array = image.img_to_array(img)

img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = predictions[0][0]

predicted_class = class_names[int(np.round(score))]

confidence = score if score > 0.5 else 1 - score

print(f"Das ist wahrscheinlich ein(e) {predicted_class.upper()} \n({confidence:.2%} Sicherheit.)")