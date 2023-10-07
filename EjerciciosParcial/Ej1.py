# 1. Implementa un programa en Python que realice el 
# procesamiento paralelo de una imagen utilizando hilos. 
# Divide la imagen en secciones y permite que cada hilo aplique
# un filtro o manipulación a su sección antes de combinar los resultados. 

from PIL import Image, ImageFilter #Modulo "Piloow"
import threading #Modulo para lograr el procesamiento paralelo 
import time

class ImageProcessor(threading.Thread): 
    def __init__(self, section): 
        threading.Thread.__init__(self) 
        self.section = section 

    def run(self): 
        self.section = self.section.filter(ImageFilter.BLUR) 


def parallel_image_processing(image_path):
    img = Image.open(image_path) 

    
    width, height = img.size
    sections = [img.crop((w, 0, w + width//4, height)) for w in range(0, width, width//4)]

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

    new_img.save('imagen_procesada.jpg')

start_time = time.time()

parallel_image_processing('img/tom-jerry.jpg')

end_time = time.time()

print(f'Tiempo de ejecución: {end_time - start_time} segundos')