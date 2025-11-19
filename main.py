import cv2
import numpy as np

# -------------------------------
# Currency Image Feature Extractor
# -------------------------------

def load_image(path):
    """Loads an image from a given path"""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError("Image not found. Check path.")
    return img

def convert_to_gray(img):
    """Converts image to grayscale"""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def detect_edges(img):
    """Applies Canny edge detection"""
    return cv2.Canny(img, 100, 200)

def detect_contours(edge_img):
    """Finds contours in the image"""
    contours, _ = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def highlight_security_features(img, contours):
    """Draw detected contours on image"""
    output = img.copy()
    cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
    return output

def save_output(img, filename="output.png"):
    """Save the processed image"""
    cv2.imwrite(filename, img)
    print(f"Saved output file: {filename}")

# -------------------------------
# Main Execution
# -------------------------------
if _name_ == "_main_":
    try:
        print("Loading image...")
        image = load_image("currency.jpg")   # <-- Replace with your image name

        print("Converting to grayscale...")
        gray = convert_to_gray(image)

        print("Detecting edges...")
        edges = detect_edges(gray)

        print("Finding contours...")
        contours = detect_contours(edges)
        print(f"Contours detected: {len(contours)}")

        print("Highlighting security features...")
        processed = highlight_security_features(image, contours)

        print("Saving output...")
        save_output(processed, "currency_security_output.png")

        print("Processing Completed Successfully!")

    except Exception as e:
        print("Error:", e)
