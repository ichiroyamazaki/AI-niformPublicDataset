# AI-niform Dataset STI Balagtas V1.0

YOLO-format uniform detection dataset for STI Balagtas.

## Dataset structure

```
uniform-dataset/
├── data.yaml
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

## Classes

- `uniform` (1 class)

## Usage

This dataset is compatible with [Ultralytics YOLO](https://docs.ultralytics.com/). Point training to `uniform-dataset/data.yaml`.

## Scripts

- `ictpicture.py` — utility script used to organize source images and labels into the YOLO train/val split.
