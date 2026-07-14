import os
import shutil
import random

# Original folder where your images and .txt annotations are
SOURCE_DIR = r'C:\Users\son\Desktop\Ict shirt\new ict shirt w- annotate'


# New YOLO dataset structure output folder
BASE_DIR = 'uniform-dataset'
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
LABELS_DIR = os.path.join(BASE_DIR, 'labels')

# Create target directory structure
for split in ['train', 'val']:
    os.makedirs(os.path.join(IMAGES_DIR, split), exist_ok=True)
    os.makedirs(os.path.join(LABELS_DIR, split), exist_ok=True)

# Get all image filenames
all_images = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(('.jpg', '.png'))]
random.shuffle(all_images)

# Split 80% train, 20% val
split_idx = int(0.8 * len(all_images))
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]

# Function to copy image and matching label
def move_files(image_list, split):
    for img_file in image_list:
        img_path = os.path.join(SOURCE_DIR, img_file)
        label_file = os.path.splitext(img_file)[0] + '.txt'
        label_path = os.path.join(SOURCE_DIR, label_file)

        # Destination
        dest_img_path = os.path.join(IMAGES_DIR, split, img_file)
        dest_label_path = os.path.join(LABELS_DIR, split, label_file)

        # Copy if label exists
        if os.path.exists(label_path):
            shutil.copy(img_path, dest_img_path)
            shutil.copy(label_path, dest_label_path)
        else:
            print(f"⚠️ Label missing for: {img_file}, skipping.")

# Move training and validation sets
move_files(train_images, 'train')
move_files(val_images, 'val')

# Create data.yaml
yaml_path = os.path.join(BASE_DIR, 'data.yaml')
with open(yaml_path, 'w') as f:
    f.write("train: images/train\n")
    f.write("val: images/val\n\n")
    f.write("nc: 1\n")
    f.write("names: ['uniform']\n")

print("✅ Dataset organized successfully in 'uniform-dataset/'")
