# 🪄 Invisibility Cloak Project

This project brings Harry Potter's invisibility cloak to life using **Python** and **OpenCV**. The effect is achieved by detecting a specific color in the video stream and replacing it with the background.

## ✅ Features
- Real-time disappearing effect
- Two versions:
  1. **Basic Version with Adjustable Color Detection (Trackbars)**
  2. **Dynamic Background Update (Works if camera moves)**

## 📦 Requirements
- Python 3.x
- Libraries: `opencv-python`, `numpy`

Install dependencies:
```
pip install -r requirements.txt
```

## ▶ How to Run

### **1. Basic Version (with Trackbars)**
```
python invisibility_cloak_basic.py
```
- Adjust HSV values using the trackbars to match your cloak color.

### **2. Dynamic Background Update Version**
```
python invisibility_cloak_dynamic.py
```
- This version updates the background automatically if the cloak is not detected.

## 🛠 How it Works
1. Captures background frame
2. Detects cloak color using **HSV color space**
3. Applies morphological operations to refine mask
4. Replaces cloak region with background

## 🎯 Future Enhancements
- Add Deep Learning-based segmentation (Mask R-CNN, U-Net)
- Add GUI for easier controls

---
Enjoy the magic! ✨
