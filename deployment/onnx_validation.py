import onnx
import onnxruntime as ort
import numpy as np
import os

ONNX_PATH = "deployment/best.onnx"

onnx_model = onnx.load(ONNX_PATH)
onnx.checker.check_model(onnx_model)
print("ONNX model structure: VALID")

session = ort.InferenceSession(ONNX_PATH, providers=["CPUExecutionProvider"])
input_name = session.get_inputs()[0].name

dummy = np.random.rand(1, 3, 640, 640).astype(np.float32)
outputs = session.run(None, {input_name: dummy})
print(f"Output shape: {outputs[0].shape}")

size_mb = os.path.getsize(ONNX_PATH) / (1024 * 1024)
print(f"Model size: {size_mb:.2f} MB")
print("Validation passed!")
