from ultralytics import YOLO

model=YOLO("yolov8n.pt")

results=model(source="https://ultralytics.com/images/bus.jpg")

for result in results:
    result.save(filename="results.jpg")
    print("Image saved as results.jpg")