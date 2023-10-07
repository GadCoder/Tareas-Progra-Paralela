# 1. Implementa un programa en Python que realice el 
# procesamiento paralelo de una imagen utilizando hilos. 
# Divide la imagen en secciones y permite que cada hilo aplique
# un filtro o manipulación a su sección antes de combinar los resultados. 

from PIL import Image, ImageFilter #Modulo "Piloow" para manipular las imagenes
import threading #Modulo para lograr el procesamiento paralelo
import time

class ImageProcessor(threading.Thread):
    def __init__(self, section):
        threading.Thread.__init__(self)
        self.section = section

    def run(self):
        # Aplica un filtro a la sección de la imagen
        self.section = self.section.filter(ImageFilter.BLUR)


def parallel_image_processing(image_path):
    # Abre la imagen
    img = Image.open(image_path)

    # Divide la imagen en secciones
    width, height = img.size
    sections = [img.crop((w, 0, w + width//4, height)) for w in range(0, width, width//4)]

    # Crea y comienza los hilos
    threads = []
    for section in sections:
        thread = ImageProcessor(section)
        thread.start()
        threads.append(thread)

    # Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()

    # Combina las secciones procesadas
    new_img = Image.new('RGB', (width, height))
    for i, thread in enumerate(threads):
        new_img.paste(thread.section, (i * width//4, 0))

    # Guarda la imagen procesada
    new_img.save('processed_image.jpg')

# Registra el tiempo de inicio
start_time = time.time()

# Llama a la función con la ruta de tu imagen
parallel_image_processing('img/agumon.jpg')
# Registra el tiempo de finalización
end_time = time.time()

# Imprime el tiempo de ejecución
print(f'Tiempo de ejecución: {end_time - start_time} segundos')