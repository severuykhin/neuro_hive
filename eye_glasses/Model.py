import os
import tensorflow as tf
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

class Model():

    model = None
    IMAGE_SIDE_SIZE = 224
    WEIGHTS_FILE_PATH = 'weights.h5'

    def configure(self):

        base_layers = tf.keras.applications.MobileNetV2(input_shape=(self.IMAGE_SIDE_SIZE, self.IMAGE_SIDE_SIZE, 3), include_top=False)
        base_layers.trainable = False
        model = tf.keras.Sequential([
            base_layers,
            GlobalAveragePooling2D(),
            Dropout(0.1),
            Dense(1, activation = "sigmoid")
        ])

        model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])
        self.model = model

    def fit(self, train_data, epochs=1):
        self.model.fit(train_data, epochs=epochs)

    def predict(self, image):
        img = load_img(image['file_path'])
        img_array = img_to_array(img)
        img_resized, _ = self.resize_image(img_array, None)
        img_expended = np.expand_dims(img_resized, axis=0)
        prediction = self.model.predict(img_expended)[0][0]
        print(prediction, int(round(prediction)))
        return int(round(prediction))

    def save_weights(self):
        self.model.save_weights(self.WEIGHTS_FILE_PATH)

    def load_weights(self):
        file_path = os.path.dirname(__file__) + '/' + self.WEIGHTS_FILE_PATH 
        print((file_path))
        self.model.load_weights(file_path)

    def summary(self):
        self.model.summary()

    def evaluate(self, test_data, verbose=1):
        loss, acc = self.model.evaluate(test_data, verbose=verbose)   
        return loss, acc

    def resize_image(self, img, label):
        img = tf.cast(img, tf.float32)
        img = tf.image.resize(img, (self.IMAGE_SIDE_SIZE, self.IMAGE_SIDE_SIZE))
        img = img / 255.0
        return img, label