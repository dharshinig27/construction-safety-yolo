# Project Report: Construction Safety Object Detection using YOLOv8

## 1. Objective

Build an object detection system to identify construction safety equipment and violations (helmets, vests, missing PPE) on construction sites using YOLOv8, and export the best model to ONNX format for portable deployment.

---

## 2. Dataset

- **Source:** [RF100 Construction Safety Dataset](https://universe.roboflow.com/roboflow-100/construction-safety-gsnvb)
- **Total Images:** 1206 — Train: 997 | Validation: 119 | Test: 90
- **Classes (5):** `helmet`, `no-helmet`, `no-vest`, `person`, `vest`
- **Format:** YOLOv8 (images + `.txt` labels + `data.yaml`)

The dataset is imbalanced — `person` and `helmet` dominate while `no-helmet` has only 94 training instances.

---

## 3. Training Setup

| Parameter      | Value                        |
|----------------|------------------------------|
| Models         | YOLOv8n, YOLOv8s             |
| Image Size     | 640 × 640                    |
| Epochs         | 100                          |
| Batch Size     | Auto                         |
| Pretrained     | Yes (COCO weights)           |
| Platform       | Google Colab (T4 GPU)        |

---

## 4. Results

| Metric          | YOLOv8n | YOLOv8s |
|-----------------|---------|---------|
| Precision       | 0.901   | 0.876   |
| Recall          | 0.801   | 0.865   |
| mAP50           | 0.868   | 0.914   |
| mAP50-95        | 0.478   | 0.504   |
| Inference Speed | 6.5 ms  | 10.5 ms |
| Model Size      | ~6 MB   | ~22 MB  |

**YOLOv8s selected as best model** — higher mAP50 (0.914) and mAP50-95 (0.504).

---

## 5. Evaluation

- **Confusion Matrix:** Most classes predicted correctly. Minor confusion between visually similar PPE classes.
- **PR Curve:** High precision maintained across most recall levels for all 5 classes.
- **F1 Curve:** Optimal confidence threshold ~0.35.
- **Hardest class:** `no-helmet` — only 94 training samples causes most false negatives.

---

## 6. ONNX Export

```bash
yolo export model=runs/yolov8s/weights/best.pt format=onnx
```

| Metric                | Value         |
|-----------------------|---------------|
| Model Size            | 42.68 MB      |
| Avg Inference Time    | ~313 ms (CPU) |
| Validation            | Passed        |

---

## 7. Inference

`demo/inference.py` supports image, video, and webcam input using the exported ONNX model.

---

## 8. Conclusion

YOLOv8s achieves strong performance with mAP50 of 0.914. Successfully exported to ONNX for hardware-agnostic deployment. Main limitation is the `no-helmet` class — more training samples would improve safety violation detection.

---

**Author:** Dharshini G — Kumaraguru College of Technology
