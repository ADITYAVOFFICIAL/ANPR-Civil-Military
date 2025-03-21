# ANPR-Civil-Military
![Forks](https://img.shields.io/github/forks/ADITYAVOFFICIAL/ANPR-Civil-Military.svg)
![PR](https://img.shields.io/github/issues-pr/ADITYAVOFFICIAL/ANPR-Civil-Military.svg)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![Views](https://views.whatilearened.today/views/github/ADITYAVOFFICIAL/ANPR-Civil-Military.svg)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub repo size](https://img.shields.io/github/repo-size/ADITYAVOFFICIAL/ANPR-Civil-Military)

<p align="center">
  <a href="#">
    <img alt="Logo" height="150" width="300" src="https://images.livemint.com/img/2020/08/04/1600x900/20200722017L_1596550154426_1596550162189.jpg">
  </a>
</p>

<h1 align="center">ANPR-Civil-Military</h1>

## Overview  

The **ANPR-Civil-Military** system is a specialized solution for Automatic Number Plate Recognition (ANPR) designed for civil and Indian military applications. This project leverages advanced computer vision and deep learning technologies to detect, extract, and store text from license plates, including military unit numbers, with high accuracy.

---

## Features  

- **YOLO Models**: Utilizes YOLOv8, YOLOv9 and YOLOv11 variants for efficient plate detection.
- **PaddleOCR Integration**: Extracts textual data from license plates with precision.
- **Real-Time Video and Image Processing**: Works seamlessly on both videos and static images.
- **Custom Military Detection**: Enhanced recognition for Indian military-specific number plates and unit markings.
- **Confidential Data Handling**: Secure storage and processing for sensitive information.

---
## Dataset

> [!IMPORTANT]
> **Download the Dataset:**  
> The complete dataset is available for download at [militaryanpr.netlify.app](https://militaryanpr.netlify.app/).


---

## Demo Screenshots  

### Civilian Plate Recognition:  
![Civilian Plate](https://raw.githubusercontent.com/ADITYAVOFFICIAL/ANPR-Civil-Military/refs/heads/main/inference/Yolov8l-Civil.jpg)  

### Military Plate Recognition:  
![Military Plate](https://raw.githubusercontent.com/ADITYAVOFFICIAL/ANPR-Civil-Military/refs/heads/main/inference/Yolov8l-Military.png) 

### Military Plate with Unit Number Recognition:  
![Military Plate](https://raw.githubusercontent.com/ADITYAVOFFICIAL/ANPR-Civil-Military/refs/heads/main/inference/Yolov11m-Military-Unit.png)

---

📂 ANPR-Civil-Military  
├── YOLOV11m/                   # YOLOv11 model files  
├── Yolov8n_OCR/                # YOLOv8 model optimized for OCR  
├── test_images/                # Sample test images  
├── test_videos/                # Sample test videos  
├── image_inference.py          # Script for image processing  
├── nplate_inference_video.py   # Script for video processing  
├── PaddleOCR.py                # PaddleOCR integration  
├── LICENSE.md                  # License details  
├── README.md                   # Project documentation  
└── requirements.txt            # Dependency list  

---

## License:
This project is licensed under the Military ANPR System License (MASL) v1.0. See the LICENSE.md file for details.

## Contribution
Contributions to this project are not currently accepted due to its military-specific nature. For any suggestions or inquiries, please contact the repository owner.


## Acknowledgments
- **Ultralytics** for YOLO models.  
- **PaddleOCR** for OCR integration.  
- Special thanks to contributors of the open-source computer vision community.  
