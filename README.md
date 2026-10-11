# Michael - Autonomous Fire Detection Robot 🤖🔥

Michael is an autonomous robotics project designed for real-time fire and smoke detection using computer vision, dual-model verification (object detection and classification), and edge computing.

---

## 🛠️ Tech Stack & Hardware
- **Hardware:** Raspberry Pi (8GB)
- **Computer Vision:** YOLOv8 (Ultralytics) for Object Detection & Classification
- **Environment:** Python 3, OpenCV, PyTorch

---

## 📁 Repository Structure
```text
Michael/
├── dataset/             # Dataset configuration, detection, and classification trees
├── docs/                # Hardware diagrams and documentation
├── scripts/             # Utility and training scripts (e.g., train_classifier.py)
├── src/                 # Main robot scripts (vision & control)
├── tests/               # Test suites and setup checks
├── .gitignore           # File exclusion rules
├── README.md            # Project overview
└── requirements.txt     # Python dependencies

## Citation & Dataset Attribution

```bibtex
@misc{ fire-indoor-ghkgq_dataset,
  title = { fire-indoor Dataset },
  type = { Open Source Dataset },
  author = { fire null },
  howpublished = { \url{[https://universe.roboflow.com/fire-null/fire-indoor-ghkgq](https://universe.roboflow.com/fire-null/fire-indoor-ghkgq)} },
  url = {[https://universe.roboflow.com/fire-null/fire-indoor-ghkgq](https://universe.roboflow.com/fire-null/fire-indoor-ghkgq)},
  journal = { Roboflow Universe },
  publisher = { Roboflow },
  year = { 2024 },
  month = { apr },
  note = { visited on 2026-10-11 }
}

@misc{ fire-no-fire-classification_dataset,
  title = { fire no fire classification Dataset },
  type = { Open Source Dataset },
  author = { National University of Sciences  Technology },
  howpublished = { \url{ https://universe.roboflow.com/national-university-of-sciences-technology/fire-no-fire-classification } },
  url = { https://universe.roboflow.com/national-university-of-sciences-technology/fire-no-fire-classification },
  journal = { Roboflow Universe },
  publisher = { Roboflow },
  year = { 2025 },
  month = { mar },
  note = { visited on 2026-10-11 },
}