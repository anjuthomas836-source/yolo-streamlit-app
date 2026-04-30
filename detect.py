from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_image(image):
    results = model(image)
    return results[0].plot()