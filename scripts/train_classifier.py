from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset" / "classification"


def main():
    model = YOLO("yolov8n-cls.pt")

    model.train(
        data=str(DATASET),
        epochs=40,       # Maximum training epochs
        imgsz=224,       # Image resolution
        batch=16,        # Images per optimization step
        patience=10,     # Early stopping
        workers=2,       # Data-loading processes
        seed=42,         # Reproducibility
        device="cpu",    # Training hardware
    )

if __name__ == "__main__":
    main()
