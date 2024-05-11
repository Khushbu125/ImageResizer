import cv2
# Configurable Parameters
source = "khushbu.jpg"
destination = 'newImage.png' # 'newImage.jpeg'

scale_percent = 50  # Percent by which the image is resized
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# CV2.imshow("title",src)

# Calculate the 50% of original dimensions
new_width = int(src.shape[1]*scale_percent/100)
new_height = int(src.shape[0]*scale_percent/100)

# resize image
output = cv2.resize(src, (new_width,new_height))
cv2.imwrite(destination, output)

