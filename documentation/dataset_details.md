# Dataset Details – Malaria Detection Project

## 1. Project Information

**Project Title:** AI-Based Malaria Detection through Microscopic Blood Cell Image Classification using CNN and Deep Learning.

**Company:** Biocon Ltd.

## 2. Dataset Source

**Dataset Name:** Cell Images for Detecting Malaria

**Source:** Kaggle – NIH Malaria Cell Images Dataset

**Dataset Link:** https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria

## 3. Dataset Description

The dataset contains microscopic images of blood cells divided into two categories:

- Parasitized: Images of malaria-infected cells.
- Uninfected: Images of cells without malaria infection.

**Image Format:** PNG

## 4. Dataset Statistics

| Category | Number of Images |
|---|---:|
| Parasitized | 13,779 |
| Uninfected | 13,779 |
| Total | 27,558 |

The dataset is balanced, with an equal number of images in both categories.

## 5. Dataset Quality Inspection

Dataset inspection was performed using Python, Pillow and Matplotlib.

The following checks were completed:

1. Counted PNG images in both categories.
2. Checked images for corruption or unreadable files.
3. Displayed sample images from both categories.
4. Verified the total number of valid images.

### Inspection Results

| Category | Total Images | Valid Images | Corrupted Images |
|---|---:|---:|---:|
| Parasitized | 13,779 | 13,779 | 0 |
| Uninfected | 13,779 | 13,779 | 0 |
| Total | 27,558 | 27,558 | 0 |

## 6. Tools Used

- Python
- VS Code
- Pillow
- Matplotlib
- pathlib

## 7. Conclusion

The dataset contains 27,558 PNG images, equally distributed between Parasitized and Uninfected categories.

All images passed the readability and corruption checks performed by the Python inspection script. Sample images from both categories were also successfully displayed.

The dataset is organised and ready for the next stages of the project.