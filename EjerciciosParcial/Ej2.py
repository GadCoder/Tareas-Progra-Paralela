#2. Implementa un programa en Python que realice el 
# procesamiento paralelo de una imagen utilizando Paralelismo de Datos. 

import cv2
import numpy as np
import os
from multiprocessing import Pool, Manager
import time

def procesar_imagen_paralela(args):
    imagen, i , global_list = args
    array = np.ones((250,250,3),dtype='uint8')*10
    alto, ancho = imagen.shape[:2]
    if i % 2 == 0:
        imagen_procesada = cv2.GaussianBlur(imagen, (17,1),0)
        imagen_procesada = cv2.addWeighted(imagen_procesada, 0.6, array,0.4,20)
        matriz_rotacion = cv2.getRotationMatrix2D((ancho//2,alto//2), 90*i,1)
        imagen_procesada = cv2.warpAffine(imagen_procesada, matriz_rotacion, (ancho,alto))
    else:
        imagen_procesada = cv2.medianBlur(imagen, 5)
        imagen_procesada = cv2.subtract(imagen_procesada, array)
        matriz_rotacion = cv2.getRotationMatrix2D((ancho//2,alto//2), 90*i,1)
        imagen_procesada = cv2.warpAffine(imagen_procesada, matriz_rotacion, (ancho,alto))

    global_list.append(imagen_procesada)




if __name__ == '__main__':
    direct_path = r".\img" #cambiar path para pruebas

    nombre_imagenes = [nombre_imagen for nombre_imagen in os.listdir(direct_path)]
    imagenes = []
    for nombre_imagen in nombre_imagenes:
        imagen = cv2.imread(f'{direct_path}\\{nombre_imagen}')
        
        if imagen is not None:
            imagen = cv2.resize(imagen, (250,250))
            imagenes.append(imagen)


    
    manager = Manager()
    global_list = manager.list()
    
    start_time = time.time()
    with Pool(processes=4) as pool:
        args = [(imagen, i ,global_list) for i, imagen in enumerate(imagenes)]
        pool.map(procesar_imagen_paralela, args)
    
    end_time = time.time()
    time_execution = end_time-start_time
    filas = []
    
    for i in range(0,len(global_list),2):
        fila = np.hstack(global_list[i:i+2])
        filas.append(fila)
    matriz_imagenes = np.vstack(filas)

    cv2.imshow("imagenes",matriz_imagenes)
    cv2.waitKey(0)
    print("Time execution: {}".format(time_execution))