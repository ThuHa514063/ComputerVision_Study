from ultralytics import YOLO
import cv2

# load model
model = YOLO("yolov8n.pt")

# mở camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # detect
    results = model(frame)

    # vẽ kết quả
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()