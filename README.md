# Construction Safety Object Detection using YOLOv8 and ONNX

Detects construction site safety equipment and violations — helmets, vests, and missing PPE — using YOLOv8 trained on the RF100 Construction Safety Dataset.

---

## Results

| Metric          | YOLOv8n | YOLOv8s  |
|-----------------|---------|----------|
| Precision       | 0.901   | 0.876    |
| Recall          | 0.801   | 0.865    |
| mAP50           | 0.868   | **0.914** |
| mAP50-95        | 0.478   | **0.504** |
| Inference Speed | 6.5 ms  | 10.5 ms  |
| Model Size      | ~6 MB   | ~22 MB   |

**Best Model: YOLOv8s**

---

## Dataset

- **Source:** [RF100 Construction Safety Dataset](https://universe.roboflow.com/roboflow-100/construction-safety-gsnvb)
- **Total Images:** 1206 (Train: 997 | Val: 119 | Test: 90)
- **Classes:** `helmet`, `no-helmet`, `no-vest`, `person`, `vest`

---

## Repository Structure

```
construction-safety-yolo/
├── dataset/
│   └── dataset_report.md
├── notebooks/
│   └── Task1_Construction_Safety_YOLO.ipynb
├── training/
│   └── train.py
├── evaluation/
│   └── evaluation_report.md
├── deployment/
│   ├── best.onnx
│   ├── onnx_validation.py
│   └── benchmark.md
├── results/
│   ├── class_distribution.png
│   ├── sample_images.png
│   └── sample_predictions.png
├── demo/
│   └── inference.py
├── README.md
├── requirements.txt
└── PROJECT_REPORT.md
```

---

## Installation

```bash
git clone https://github.com/dharshinig27/construction-safety-yolo.git
cd construction-safety-yolo
pip install -r requirements.txt
```

---

## Run Inference

```bash
# On an image
python demo/inference.py --source path/to/image.jpg

# On a video
python demo/inference.py --source path/to/video.mp4

# On webcam
python demo/inference.py --source 0
```

---

## Training

Open `notebooks/Task1_Construction_Safety_YOLO.ipynb` in Google Colab with a T4 GPU runtime and run all cells.

---

**Author:** Dharshini G — Kumaraguru College of Technology
