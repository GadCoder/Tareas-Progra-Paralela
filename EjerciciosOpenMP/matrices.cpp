#include <iostream>
#include <vector>
#include <omp.h>
#include <random> // Incluye la biblioteca para números aleatorios

using namespace std;

// Función para la multipliacion en paralelo
void multiparalela(const vector<vector<int>> &A, const vector<vector<int>> &B, vector<vector<int>> &result)
{
    int N = A.size(); // Le damos a N el valor del tamaño del vector A.

#pragma omp parallel for // Aqui realizamos la multipliacion por filas.
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            int sum = 0;
            for (int k = 0; k < N; ++k)
            {
                sum += A[i][k] * B[k][j]; // Aqui se muliplica.
            }
            result[i][j] = sum; // Aqui le damos el valor al resultado.
        }
    }
}

// Función para la mutiplicacion secuencial
void multisecuencial(const vector<vector<int>> &A, const vector<vector<int>> &B, vector<vector<int>> &result)
{
    int N = A.size(); // Le damos a N el valor del tamaño del vector A.

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            int sum = 0;
            for (int k = 0; k < N; ++k)
            {
                sum += A[i][k] * B[k][j]; // Aqui se multiplica.
            }
            result[i][j] = sum; // Aqui le damos el valor al resultado
        }
    }
}

// Función para llenar una matriz con valores aleatorios en un rango específico
void llenadomatrizrandom(vector<vector<int>> &matrix, int minValue, int maxValue)
{
    int N = matrix.size();
    random_device rd;                                      // Generador de números aleatorios
    mt19937 gen(rd());                                     // Motor de números aleatorios
    uniform_int_distribution<int> dis(minValue, maxValue); // Distribución uniforme

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            matrix[i][j] = dis(gen); // Llena cada elemento con un valor aleatorio
        }
    }
}

int main()
{
    int N = 100;                                      // Tamaño de las matrices cuadradas
    vector<vector<int>> matrixA(N, vector<int>(N));   // Llena la matriz A con valores de ejemplo
    vector<vector<int>> matrixB(N, vector<int>(N));   // Llena la matriz B con valores de ejemplo
    vector<vector<int>> result(N, vector<int>(N, 0)); // Matriz resultante

    double startTime, endTime;

    // Llena matrixA y matrixB con valores aleatorios en el rango de 1 a 100
    llenadomatrizrandom(matrixA, 1, 100);
    llenadomatrizrandom(matrixB, 1, 100);

    // Multiplicación secuencial
    startTime = omp_get_wtime();
    multisecuencial(matrixA, matrixB, result);
    endTime = omp_get_wtime();

    cout << "Tiempo de ejecución secuencial: " << (endTime - startTime) << " segundos" << endl;

    // Reiniciamos la matriz resultante para hacer el metodo en paralelo a continuacion.
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            result[i][j] = 0;
        }
    }

    // Multiplicación en paralelo
    startTime = omp_get_wtime();
    multiparalela(matrixA, matrixB, result);
    endTime = omp_get_wtime();

    cout << "Tiempo de ejecución en paralelo: " << (endTime - startTime) << " segundos" << endl;

    return 0;
}