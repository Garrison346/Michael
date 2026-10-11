from ultralytics import YOLO

# This will download the base nano model and test if everything works
model = YOLO("yolov8n.pt")
print("Ultralytics is successfully installed and ready!")