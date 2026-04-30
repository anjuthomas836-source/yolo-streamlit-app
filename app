import streamlit as st
import cv2

st.set_page_config(page_title="YOLO App")

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------- LOGIN ----------
if not st.session_state.logged_in:

    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong credentials")

    st.stop()   # 🔥 THIS IS THE KEY FIX

# ---------- AFTER LOGIN ----------
st.title("YOLO Dashboard")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.success("Login successful ✔")

# ---------- IMAGE UPLOAD ----------
uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    st.write("Image uploaded ✔")

# ---------- WEBCAM ----------
if st.button("Start Webcam"):

    cap = cv2.VideoCapture(0)
    frame_placeholder = st.image([])

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_placeholder.image(frame, channels="BGR")

    cap.release()
    from detect import detect_image