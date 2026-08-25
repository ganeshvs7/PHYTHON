import cv2

import matplotlib.pyplot as plt
import numpy as np

print("🚀 Script started...")

def convert_to_grayscale(image_path):
    print(f"📸 Attempting to load: {image_path}")
    
    # 1. Load the image using OpenCV
    bgr_img = cv2.imread(image_path)
    
    # Check if the image actually exists/loaded properly
    if bgr_img is None:
        print("❌ Error: Could not find or load the image.")
        print("💡 Make sure 'opencv image.jpg' (or .png) is in the exact same folder as this script!")
        return

    print("✅ Image loaded successfully! Converting...")

    # 2. Convert BGR to RGB for Matplotlib
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

    # 3. Convert to Grayscale using NumPy formula
    r_channel = rgb_img[:, :, 0]
    g_channel = rgb_img[:, :, 1]
    b_channel = rgb_img[:, :, 2]
    
    gray_img = (0.299 * r_channel + 0.587 * g_channel + 0.114 * b_channel).astype(np.uint8)

    print("📊 Displaying the plot window now...")

    # 4. Display using Matplotlib
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.title("Original (RGB)")
    plt.imshow(rgb_img)
    plt.axis('off')

    # Grayscale Image
    plt.subplot(1, 2, 2)
    plt.title("Grayscale (NumPy)")
    plt.imshow(gray_img, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    print("🏁 Window closed. Script finished!")

# --- EXECUTION ---
# Change the extension (.jpg, .png, etc.) to match your actual file!
IMAGE_NAME = 'opencv image.png' 

convert_to_grayscale('C:\\Users\\ganes\\OneDrive\\Desktop\\Python\\advance python\\opencv image.png')
