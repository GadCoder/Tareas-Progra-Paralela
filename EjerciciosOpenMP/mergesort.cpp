#include <iostream>
#include <omp.h>
#include <stdlib.h>
#include <time.h>
#include <iomanip>
#include <vector>
using array = std::vector<int>;
array mergeSortSecuencial(array numbers);
array mergeSecuencial(array numbersA, array numbersB);
array mergeSortParalelo(array numbers);
array mergeParalelo(array numbersA, array numbersB);
void mostrarValores(array);
int getRandomInt();
int main()
{
    int ARRAY_SIZE = 300000;
    array numbers;
    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        int number = getRandomInt();
        numbers.push_back(number);
    }
    double startSecuencial, endSecuencial;
    double startParalelo, endParalelo;
    startParalelo = omp_get_wtime();
    array sortedParalelo = mergeSortParalelo(numbers);
    endParalelo = omp_get_wtime();
    std::cout << "\nTiempo paralelo: " << std::fixed << std::setprecision(6) << endParalelo - startParalelo << " segundos" << std::endl;
    std::cout << "Valores Paralelo\n: ";
    startSecuencial = omp_get_wtime();
    array sortedNumbers = mergeSortSecuencial(numbers);
    endSecuencial = omp_get_wtime();
    std::cout << "Tiempo secuencial: " << std::fixed << std::setprecision(6) << endSecuencial - startSecuencial << " segundos" << std::endl;
    // // std::cout<<"Valores secuencial\n: ";
    // mostrarValores(sortedNumbers); //mostrarValores(sortedParalelo);
    return 0;
}
void mostrarValores(array resultado)
{
    for (int i = 0; i < resultado.size(); i++)
    {
        std::cout << resultado[i] << " ";
    }
}
int getRandomInt()
{
    int randomInt = rand() % 50 + 1;
    return randomInt;
}
array mergeSortParalelo(array numbers)
{
    int size = numbers.size();
    if (size <= 1)
        return numbers;
    array firstHalf;
    array secondHalf;
    int middle = size / 2;
#pragma omp parallel sections
    {
#pragma omp section
        {
            for (int i = 0; i < middle; i++)
            {
                firstHalf.push_back(numbers[i]);
            }
            firstHalf = mergeSortParalelo(firstHalf);
        }
#pragma omp section
        {
            for (int i = middle; i < size; i++)
            {
                secondHalf.push_back(numbers[i]);
            }
            secondHalf = mergeSortParalelo(secondHalf);
        }
    }
    return mergeParalelo(firstHalf, secondHalf);
}
array mergeParalelo(array numbersA, array numbersB)
{
    array tempArray;
    while (!numbersA.empty() && !numbersB.empty())
    {
        if (numbersA[0] > numbersB[0])
        {
            tempArray.push_back(numbersB[0]);
            numbersB.erase(numbersB.begin());
        }
        else
        {
            tempArray.push_back(numbersA[0]);
            numbersA.erase(numbersA.begin());
        }
    }
    while (!numbersA.empty())
    {
        tempArray.push_back(numbersA[0]);
        numbersA.erase(numbersA.begin());
    }
    while (!numbersB.empty())
    {
        tempArray.push_back(numbersB[0]);
        numbersB.erase(numbersB.begin());
    }
    return tempArray;
}
array mergeSortSecuencial(array numbers)
{
    int size = numbers.size();
    if (size <= 1)
        return numbers;
    array firstHalf;
    array secondHalf;
    int middle = size / 2;
    for (int i = 0; i < middle; i++)
    {
        firstHalf.push_back(numbers[i]);
    }
    for (int i = middle; i < size; i++)
    {
        secondHalf.push_back(numbers[i]);
    }
    firstHalf = mergeSortSecuencial(firstHalf);
    secondHalf = mergeSortSecuencial(secondHalf);
    return mergeSecuencial(firstHalf, secondHalf);
}
array mergeSecuencial(array numbersA, array numbersB)
{
    array tempArray;
    while (!numbersA.empty() && !numbersB.empty())
    {
        if (numbersA[0] > numbersB[0])
        {
            tempArray.push_back(numbersB[0]);
            numbersB.erase(numbersB.begin());
        }
        else
        {
            tempArray.push_back(numbersA[0]);
            numbersA.erase(numbersA.begin());
        }
    }
    while (!numbersA.empty())
    {
        tempArray.push_back(numbersA[0]);
        numbersA.erase(numbersA.begin());
    }
    while (!numbersB.empty())
    {
        tempArray.push_back(numbersB[0]);
        numbersB.erase(numbersB.begin());
    }
    return tempArray;
}
