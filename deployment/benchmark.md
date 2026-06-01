# ONNX Benchmark

## Model
YOLOv8s exported from `runs/yolov8s/weights/best.pt`

## Validation

| Check | Result |
|-------|--------|
| ONNX loads successfully | YES |
| Model structure check passed | YES |
| Inference runs correctly | YES |
| Output shape matches PyTorch | YES |

## Measurements

| Metric | Value |
|--------|-------|
| ONNX Model Size | 42.68 MB |
| Average Inference Time | 313.09 ms |
| Benchmark Runs | 100 iterations |
| Runtime Provider | CPUExecutionProvider |
