# Dataset Report

## Dataset Overview

- **Source:** [RF100 Construction Safety Dataset](https://universe.roboflow.com/roboflow-100/construction-safety-gsnvb)
- **Total Images:** 1206
- **Train Images:** 997
- **Validation Images:** 119
- **Test Images:** 90
- **Number of Classes:** 5

## Classes

| ID | Class     |
|----|----------|
| 0  | helmet   |
| 1  | no-helmet|
| 2  | no-vest  |
| 3  | person   |
| 4  | vest     |

## Class Distribution (Training Set)

| Class     | Count |
|-----------|------:|
| person    | 2362  |
| helmet    | 2116  |
| vest      | 1073  |
| no-vest   | 741   |
| no-helmet | 94    |

## Verification

- Images load correctly: YES
- Labels are properly mapped: YES
- Train/Validation/Test split exists: YES

## Observations

- Dataset is imbalanced — `no-helmet` has only 94 instances.
- `person` and `helmet` are the dominant classes.
- Detecting `no-helmet` violations may be harder due to limited samples.
