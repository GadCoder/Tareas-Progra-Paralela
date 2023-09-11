#include <stdio.h>       //Para el uso de la función printf
#include <stdlib.h>      //Para el uso de la función rand
#include <time.h>        //Para el uso de la función time
#include <omp.h>         //Para el uso de las funciones de omp
#define NUM_PUNTOS 10000 // Definimos la cantidad de puntos totales que habrán dentro del cuadrado
double monteCarloSecuencial()
{
    int ptsCirculo = 0; // Contador de Puntos
    srand(time(NULL));  // Establece la semilla de aleatoriedad determinista
    for (int i = 0; i < NUM_PUNTOS; i++)
    {
        double x = (double)rand() / RAND_MAX; // Se crean N (N = NUM_PUNTOS) valores distintos para las abcisas
        double y = (double)rand() / RAND_MAX; // Se crean N (N = NUM_PUNTOS) valores distintos para las ordenadas
        if (x * x + y * y <= 1.0)
        {                 // Se verifica qué puntos pertenecen (están dentro) a la circunferencia {x^2+y^2<=radio^2}
            ptsCirculo++; // Se incrementa el contador para puntos dentro de la circunferencia }
        }
        return 4.0 * ptsCirculo / NUM_PUNTOS; // El resultado aproximado para PI sería la dada en la fórmula establecida
    }
    // Se sigue la misma base para la función que crea hilos
}
double monteCarloParalelo()
{
    int ptsCirculo = 0;
// Se establece el bloque en el que se aplicará el paralelismo
#pragma omp parallel
    {
        unsigned int semilla = time(NULL) + omp_get_thread_num(); // Se asigna una semilla aleatoria para cada hilo (por ello se le suma el N° del hilo)
        srand(semilla);
        // Aquí se define que el paralelismo actuará en un bloque for
        // Además, el reduction indica una operación de reducción en base al incremento de la variable ptsCirculo
        // Esto es que cada hilo paralelo sumará su propia contribución a ptsCirculo, y al final de la región paralela,
        // se sumarán todas estas contribuciones para obtener el resultado final en ptsCirculo. #pragma omp for reduction(+:ptsCirculo)
        for (int i = 0; i < NUM_PUNTOS; i++)
        {
            double x = (double)rand() / RAND_MAX;
            double y = (double)rand() / RAND_MAX;
            if (x * x + y * y <= 1.0)
            {
                ptsCirculo++;
            }
        }
    }
    return 4.0 * ptsCirculo / NUM_PUNTOS;
} // Se obtiene la aproximación de PI }

int main()
{
    double piSequencial, piParalelo; // Definimos 2 variables: Una para el PI del algor. Secuencial y otra para el PI del algor. Paralelo
    // Medimos el tiempo para el algor. Secuencial
    double tiempo_inicio = omp_get_wtime();
    piSequencial = monteCarloSecuencial();
    double tiempo_final = omp_get_wtime();
    printf("pi - secuencial: %lf\n", piSequencial);
    printf("Tiempo: %lf segundos\n", tiempo_final - tiempo_inicio);
    // Medimos el tiempo para el algor. Paralelo
    tiempo_inicio = omp_get_wtime();
    piParalelo = monteCarloParalelo();
    tiempo_final = omp_get_wtime();
    printf("pi - paralelo: %lf\n", piParalelo);
    printf("Tiempo: %lf segundos\n", tiempo_final - tiempo_inicio);
    return 0;
}
