import cv2
from ultralytics import YOLO

def main():
    model = YOLO(r"runs_detect/train_custom/weights/best.pt")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Khong mo duoc webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Khong doc duoc frame tu webcam")
            break

        results = model(frame, conf=0.25, verbose=False)
        annotated_frame = results[0].plot()

        cv2.imshow("Custom YOLO Webcam", annotated_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()