import time
import threading
import cv2 as cv
from matplotlib import pyplot as plt


IMG_FOLDER = 'static/'


def load_image(img_path: str):
    img = cv.imread(img_path)
    return img


def sequencial_filter(img):
    blur_effect_img = cv.GaussianBlur(img, (35, 35), 0)
    return blur_effect_img


def sequential_process(img_extension):
    img_path = IMG_FOLDER + "upload_image." + img_extension
    img = load_image(img_path=img_path)

    start_time = time.time()
    sequencial_image = sequencial_filter(img)
    end_time = time.time()
    sequential_time = round(end_time - start_time, 4)

    sequencial_output = IMG_FOLDER + \
        "sequencial_processed_image." + img_extension
    cv.imwrite(sequencial_output, sequencial_image)

    return sequential_time
