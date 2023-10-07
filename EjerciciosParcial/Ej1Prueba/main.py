from PIL import Image, ImageFilter
import threading

def apply_blur_filter(image, start_row, end_row, result):
    width, height = image.size
    for y in range(start_row, end_row):
        for x in range(width):
            # Aplica un filtro de desenfoque a cada píxel
            blurred_pixel = image.filter(ImageFilter.BLUR).getpixel((x, y))
            result.putpixel((x, y), blurred_pixel)

def parallel_process(image, num_threads=3):
    width, height = image.size
    step = height // num_threads

    threads = []
    results = [Image.new("RGB", (width, height)) for _ in range(num_threads)]

    for i in range(num_threads):
        start_row = i * step
        end_row = start_row + step if i < num_threads - 1 else height

        thread = threading.Thread(
            target=apply_blur_filter, args=(image, start_row, end_row, results[i])
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Combina los resultados de cada hilo
    final_result = Image.new("RGB", (width, height))
    for result in results:
        final_result.paste(result, (0, 0), result)

    return final_result

if __name__ == "__main__":
    input_image_path = "./input_image.jpg"
    output_image_path = "./output_image_blur.jpg"

    original_image = Image.open(input_image_path)

    processed_image = parallel_process(original_image)

    processed_image.save(output_image_path)
