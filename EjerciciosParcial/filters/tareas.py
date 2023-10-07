import time
import threading
import cv2 as cv
from matplotlib import pyplot as plt


IMG_FOLDER = 'static/'


def load_image(img_path: str):
    img = cv.imread(img_path)
    return img


def get_image_dimensions(img):
    height, width, channels = img.shape
    return height, width


def show_image(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def get_quarters(img, height, width):
    first_quarter = img[0:int(height/2), 0:int(width/2)]
    second_quarter = img[0:int(height/2), int(width/2):width]
    third_quarter = img[int(height/2):height, 0:int(width/2)]
    fourth_quarter = img[int(height/2):height, int(width/2):width]
    return {
        "first": first_quarter,
        "second": second_quarter,
        "third": third_quarter,
        "fourth": fourth_quarter
    }


def apply_parallel_filter(img, img_parts, quarter):
    blur_effect_img = cv.blur(img, (35, 35), 0)
    img_parts[quarter] = blur_effect_img


def parallel_filter(img_quarters: dict):
    threads = []
    img_parts = {}
    for key, value in img_quarters.items():
        thread = threading.Thread(
            target=apply_parallel_filter, args=(value, img_parts, key))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    for key in img_parts.keys():
        print(key)
    top_part = cv.hconcat([img_parts["first"], img_parts["second"]])
    bottom_part = cv.hconcat([img_parts["third"], img_parts["fourth"]])
    final_image = cv.vconcat([top_part, bottom_part])
    return final_image


def tareas_process(img_extension):
    img_path = IMG_FOLDER + "upload_image." + img_extension
    img = load_image(img_path=img_path)

    height, width = get_image_dimensions(img)
    img_quarters = get_quarters(img, height, width)
    start_time = time.time()
    parallel_image = parallel_filter(img_quarters)
    end_time = time.time()
    parallel_time = round(end_time - start_time, 4)

    parallel_output = IMG_FOLDER + "tareas_processed_image." + img_extension
    cv.imwrite(parallel_output, parallel_image)

    return parallel_time
