import cv2
import numpy as np
from PIL import Image
import io

def image_to_bytes(img):
    # Create an in-memory binary stream
    img_bytes = io.BytesIO()

    # Save the image to the binary stream
    img.save(img_bytes, format='JPEG')  # You can change the format if needed

    # Get the bytes from the binary stream
    img_bytes = img_bytes.getvalue()

    return img_bytes

def apply_sepia_filter(img):
    # Read the image

    image_bits = image_to_bytes(img)
    image_array = np.frombuffer(image_bits, dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)


    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    sepia_image = cv2.transform(img, sepia_filter)

    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)
     # Convert the NumPy array back to Image
    sepia_image = Image.fromarray(sepia_image)

    return sepia_image






