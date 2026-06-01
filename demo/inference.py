"""Construction Safety Inference Script
Usage:
  python inference.py --source image.jpg
  python inference.py --source video.mp4
  python inference.py --source 0          # webcam
"""
import argparse
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument("--source", type=str, required=True, help="Image / video path or 0 for webcam")
parser.add_argument("--model",  type=str, default="deployment/best.onnx")
parser.add_argument("--conf",   type=float, default=0.25)
args = parser.parse_args()

model = YOLO(args.model)
results = model.predict(source=args.source, conf=args.conf, save=True)
print("Inference complete. Output saved to runs/detect/predict/")
