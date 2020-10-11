import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from Model import Model

# Loads dataset for validation - the last 10% of dataset
test, _ = tfds.load('cats_vs_dogs', split=['train[-10%:]'], with_info=True, as_supervised=True)

# Create new model instance
model = Model()
model.configure()
model.load_weights()

# Prepare test data
test_resized = test[0].map(model.resize_image)
test_batches = test_resized.shuffle(1000).batch(16)

# Display model config
# It prints so few trainable params because of MobileNetV2 already trained
model.summary()

# Check model accuracy after training
loss, acc = model.evaluate(test_batches, verbose=1)
print("Model accuracy: {:5.2f}%".format(100*acc))

# Save model weight for reuse
model.save_weights()