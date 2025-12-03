from ultralytics import YOLO

model=YOLO("yolov8n.pt")

result=model.predict(source="https://ultralytics.com/images/bus.jpg",save=True,conf=0.25)

print("Mission complete! Check the 'runs/detect' folder for the output image.")