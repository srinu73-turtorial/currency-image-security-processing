# currency-image-security-processing
Real time currency recognition and authentication using image processing 
🏦 Enhancing Currency Security Through Real-Time Image Processing Based Recognition and Authentication

This project aims to improve the detection of fake vs. genuine currency using real-time image processing techniques.
It uses Python-based image processing (without machine learning) to analyze currency features such as:

Watermarks

Security threads

Color patterns

Edges and texture

Micro-text detection



---

🚀 Project Overview

Fake currency circulation is a major issue in financial systems.
The proposed solution captures a currency note image in real-time (via webcam or uploaded image) and performs:

1. Preprocessing (grayscale, blur, normalization)
2. Feature extraction (edges, security thread, watermark region)
3. Comparison with reference standards
4. Decision: GENUINE or FAKE
No machine learning is used—only OpenCV and image processing techniques.


---

🛠 Tech Stack

Component	Technology

Programming	Python
Libraries	OpenCV, NumPy, Imutils, Matplotlib
Image Processing	Edge detection, Thresholding, Keypoint matching
Input	Webcam or uploaded currency image



---

📂 Folder Structure

currency-image-security-processing/
│
├── main.py
├── detect_features.py
├── reference_images/
│      ├── genuine_100.jpg
│      ├── genuine_500.jpg
│      ├── genuine_2000.jpg
│
├── test_images/
│      ├── test1.jpg
│      ├── test2.jpg
│
├── output/
│      ├── processed.jpg
│      ├── comparison.jpg
│
├── README.md
└── requirements.txt
