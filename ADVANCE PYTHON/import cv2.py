import cv2

# Read image (BGR)
img = cv2.imread("photo.jpg")

# Convert BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert RGB to Grayscale
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

# Display images
cv2.imshow("Original BGR", img)
cv2.imshow("Gray Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()