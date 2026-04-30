
import streamlit as st
from detect import detect_image
from PIL import Image
import numpy as np

# ------------------ SIMPLE USER DATABASE ------------------
# (for project demo only)
users = {
    "admin": "admin123"
}

# ------------------ SESSION STATE ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------ LOGIN FUNCTION ------------------
def login():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful ✅")
        else:
            st.error("Invalid username or password ❌")

# ------------------ MAIN APP ------------------
def main_app():
    st.title("YOLO Object Detection App 🚀")

    if st.button("Logout"):
        st.session_state.logged_in = False

    file = st.file_uploader("Upload Image")

    if file:
        image = Image.open(file)
        st.image(image, caption="Uploaded Image")

        img_array = np.array(image)

        result = detect_image(img_array)

        st.image(result, caption="Detected Image")

# ------------------ APP FLOW ------------------
if st.session_state.logged_in:
    main_app()
else:
    login()
    import streamlit as st
    if "logged_in" not in st.session_state:
    st.session_state.logged_in = False