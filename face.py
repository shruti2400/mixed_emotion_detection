# -*- coding: utf-8 -*-
"""face.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17RR3Frk0ge-2w23ltJyEvsia8EP9AR3h
"""

!pip install tensorflow
!pip install fer

import tensorflow as tf
from fer import FER

print("TensorFlow version:", tf.__version__)
print("FER module imported successfully.")

!pip install pandas

from google.colab import files
from fer import FER
import cv2
import pandas as pd
import matplotlib.pyplot as plt

# Upload an image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
img = cv2.imread(image_path)

# Initialize the FER emotion detector
emotion_detector = FER(mtcnn=True)

# Detect emotions in the image
emotions = emotion_detector.detect_emotions(img)

# Display the detected emotions
if emotions:
    # Extracting emotion scores for the first detected face
    emotion_scores = emotions[0]["emotions"]
    emotion_df = pd.DataFrame([emotion_scores])

    # Display as a table
    print("Detected Emotions:")
    display(emotion_df)

    # Display the image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
else:
    print("No faces detected in the image.")