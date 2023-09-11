#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <omp.h>
#include <malloc.h>
#define N 20000
void llenarLista(int listaPrimos[N])
{
    for (int i = 0; i < N; i++)
        listaPrimos[i] = true;
}
void mostrarPrimos(int listaPrimos[])
{
    printf("Numeros primos menores a %d:\n", N);
    for (int i = 2; i < N; i++)
    {
        if (listaPrimos[i])
            printf("%d ", i);
    }
}
void cribaEratostenes(int listaPrimos[])
{
    double inicio, duracion;
    inicio = omp_get_wtime();
    for (int i = 2; i * i < N; i++)
    {
        if (!listaPrimos[i])
            continue;
        for (int noPrimo = 2; noPrimo * i < N; noPrimo++)
        {
            listaPrimos[noPrimo * i] = false;
        }
    }
    duracion = omp_get_wtime() - inicio;
    // mostrarPrimos(listaPrimos);
    printf("\nLa duracion es (Secuencial) = %lf segundos\n", duracion);
}
void cribaEratostenesParalela(int listaPrimos[])
{
    double inicio, duracion;
    listaPrimos[0] = false;
    listaPrimos[1] = false;
    int limit = (int)sqrt(N);
    int hilos = (int)sqrt(limit);
    inicio = omp_get_wtime();
#pragma omp parallel num_threads(hilos)
    {
#pragma omp for
        for (int i = 0; i < hilos; i++)
        {
            if (!listaPrimos[i])
                continue;
            for (int noPrimo = 2; noPrimo * i < N; noPrimo++)
            {
                int index = noPrimo * i;
                if (!listaPrimos[index])
                    continue;
                listaPrimos[index] = false;
            }
        }
    }
    duracion = omp_get_wtime() - inicio;
    // mostrarPrimos(listaPrimos);
    printf("\nLa duracion es (Paralelo) = %lf segundos\n", duracion);
}
int main()
{
    int *listaPrimos = malloc(N * sizeof(int));
    llenarLista(listaPrimos);
    cribaEratostenesParalela(listaPrimos);
    llenarLista(listaPrimos);
    cribaEratostenes(listaPrimos);
    free(listaPrimos);
    return 0;
}
