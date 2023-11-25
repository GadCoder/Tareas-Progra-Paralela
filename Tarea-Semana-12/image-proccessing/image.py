from PIL import Image

def divide_image_in_quarters(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Calculate the coordinates for the four quarters
    left_upper = (0, 0, width // 2, height // 2)
    right_upper = (width // 2, 0, width, height // 2)
    left_lower = (0, height // 2, width // 2, height)
    right_lower = (width // 2, height // 2, width, height)

    # Crop the quarters
    upper_left_img = img.crop(left_upper)
    upper_right_img = img.crop(right_upper)
    lower_left_img = img.crop(left_lower)
    lower_right_img = img.crop(right_lower)

    return [upper_left_img, upper_right_img, lower_left_img, lower_right_img]


