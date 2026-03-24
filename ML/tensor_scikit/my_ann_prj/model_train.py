import tensorflow as tf
#from tensorflow.keras import layers, models
from keras import layers, models
import keras

import matplotlib.pyplot as plt
import numpy as np
import os

BASE_PATH = r"\Users\MariaSizintseva\Desktop\MariaDocs\marrfusProgBackup\python\ML\tensor_scikit\my_ann_prj\archive"  #male female
# BASE_PATH = r"\Users\MariaSizintseva\Desktop\MariaDocs\marrfusProgBackup\python\ML\tensor_scikit\my_ann_prj\daten"  #cats dogs

TRAIN_PATH = os.path.join(BASE_PATH,'train')
VALIDATION_PATH = os.path.join(BASE_PATH,'validation')

BATCH_SIZE= 32
IMG_SIZE=(160,160)


train_dataset = keras.utils.image_dataset_from_directory(
    TRAIN_PATH,
    shuffle=True,
    batch_size= BATCH_SIZE,
    image_size=IMG_SIZE
)

validation_dataset = keras.utils.image_dataset_from_directory(
    VALIDATION_PATH,
    shuffle=True,
    batch_size= BATCH_SIZE,
    image_size=IMG_SIZE
)

class_names = train_dataset.class_names
print(f"Klassen gefunden: {class_names}")

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)

model = models.Sequential([
    layers.Rescaling(1./127.5, offset=-1, input_shape=(160,160,3)),

    layers.Conv2D(32,(3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    
    layers.Conv2D(64,(3,3), activation="relu"),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128,(3,3), activation="relu"),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(1,activation="sigmoid")
])

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["accuracy"])

model.summary()

EPOCHS = 10
history = model.fit(train_dataset, epochs=EPOCHS, validation_data=validation_dataset)

model.save(os.path.join(BASE_PATH, "male_female_model.h5"))  #human
# model.save("hunde_katzen_model.h5")  #cat dog
print("Modell wurde gespeichert!")

