# 1. Implementa un programa en Python que realice el
# procesamiento paralelo de una imagen utilizando hilos.
# Divide la imagen en secciones y permite que cada hilo aplique
# un filtro o manipulación a su sección antes de combinar los resultados.

from PIL import Image, ImageFilter  # Modulo "Piloow" para manipular las imagenes
import threading  # Modulo para lograr el procesamiento paralelo
import time


IMG_FOLDER = 'static/'


class ImageProcessor(threading.Thread):
    def __init__(self, section):
        threading.Thread.__init__(self)
        self.section = section

    def run(self): 
        self.section = self.section.filter(ImageFilter.BLUR) 


def parallel_image_processing(image_path):
    img = Image.open(image_path) 

    
    width, height = img.size
    sections = [img.crop((w, 0, w + width//4, height))
                for w in range(0, width, width//4)]

    threads = []  
    for section in sections: 
        thread = ImageProcessor(section) 
        thread.start() 
        threads.append(thread) 

    
    for thread in threads: 
        thread.join() 

    
    new_img = Image.new('RGB', (width, height)) 
    for i, thread in enumerate(threads): 
        new_img.paste(thread.section, (i * width//4, 0)) 

<<<<<<< HEAD:EjerciciosParcial/Ej1.py
    new_img.save('imagen_procesada.jpg')
#Realizaremos el proceso tomando el tiempo para ver su rendimiento.
start_time = time.time()

parallel_image_processing('img/tom-jerry.jpg')

end_time = time.time()

print(f'Tiempo de ejecución: {end_time - start_time} segundos')
=======
    return new_img


def threads_process(img_extension):
    img_path = IMG_FOLDER + "upload_image." + img_extension
    # Registra el tiempo de inicio
    start_time = time.time()
    # Llama a la función con la ruta de tu imagen
    processed_img = parallel_image_processing(image_path=img_path)
    # Registra el tiempo de finalización
    end_time = time.time()
    output_path = IMG_FOLDER + "threads_processed_image." + img_extension

    processed_img.save(output_path)

    parallel_time = round(end_time - start_time, 4)

    return parallel_time
>>>>>>> 396168d4916467452c80d7a92fee670ead313494:EjerciciosParcial/filters/threads.py
