# Evaluation Report

## Model Comparison

| Metric          | YOLOv8n | YOLOv8s |
|-----------------|---------|--------|
| Precision       | 0.901   | 0.835   |
| Recall          | 0.801   | 0.872   |
| mAP50           | 0.868   | 0.899   |
| mAP50-95        | 0.478   | 0.502   |
| Inference Speed | 6.5 ms  | 10.5 ms |
| Model Size      | 6.0 MB  | 21.5 MB   |

## Best Model

**YOLOv8s** — higher mAP50 and mAP50-95.

## Confusion Matrix Analysis

Most classes are correctly predicted. Minor confusion between PPE classes due to visual similarity.

## PR Curve Analysis

High precision is maintained across most recall levels for all 5 classes.

## F1 Curve Analysis

F1 score is stable across confidence thresholds. Optimal threshold is approximately 0.35.

## Failure Cases

**False Positives:**
- Reflective surfaces occasionally misclassified as safety vests.

**False Negatives:**
- `no-helmet` is the most commonly missed class (only 94 training samples).
- Small or partially occluded workers may be missed.
