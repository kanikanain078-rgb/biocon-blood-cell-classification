
import os
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

# 1. Set the dataset path
project_path = Path(__file__).resolve().parent.parent
dataset_path = project_path / "dataset" / "original"

# 2. Define the two categories
categories = ["Parasitized", "Uninfected"]

total_images = 0

# 3. Count and check images
for category in categories:

    folder_path = dataset_path / category

    image_files = list(folder_path.glob("*.png"))

    valid_images = []
    corrupted_images = []

    for image_path in image_files:
        try:
            with Image.open(image_path) as img:
                img.verify()
            valid_images.append(image_path)

        except Exception:
            corrupted_images.append(image_path)

    print("\nCategory:", category)
    print("Total PNG images:", len(image_files))
    print("Valid images:", len(valid_images))
    print("Corrupted images:", len(corrupted_images))

    total_images += len(valid_images)

    # 4. Display one sample image
    if valid_images:
        sample_path = valid_images[0]

        image = Image.open(sample_path)

        plt.figure(figsize=(4, 4))
        plt.imshow(image)
        plt.title(category)
        plt.axis("off")
        plt.show()

# 5. Display final statistics
print("\n-------------------------")
print("DATASET SUMMARY")
print("-------------------------")
print("Total valid images:", total_images)
print("Expected images: 27558")
