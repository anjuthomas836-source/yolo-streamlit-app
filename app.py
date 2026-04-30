import streamlit as st
from PIL import Image
import numpy as np
from detect import detect_image

st.title("YOLO Object Detection App 🚀")

# Upload image
file = st.file_uploader("Upload an Image")

if file:
    image = Image.open(file)
    st.image(image, caption="Uploaded Image")

    img_array = np.array(image)

    # Run detection
    result = detect_image(img_array)

    # Show detected image
    st.image(result, caption="Detected Image")