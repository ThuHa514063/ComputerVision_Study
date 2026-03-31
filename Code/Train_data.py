from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")  # pretrained model

    model.train(
        data=r"F:\ThuHa\Computer Vision\ComputerVision_Study\Code\data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        device="cpu",      # neu co GPU thi doi thanh 0
        workers=0,         # Windows hay de 0 cho on dinh
        pretrained=True,
        project="runs_detect",
        name="train_custom"
    )

if __name__ == "__main__":
    main()