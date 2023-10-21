// GUIA 104.1 : Utilizando Future y ExecutorService en Java
// Tarea: Implemente la suma de los elementos de un vector utilizando los mecanismos mencionados en la guia. 

/* ARRAY DE 10_000_000 ELEMENTOS */

import java.util.concurrent.*;

// Clase principal que implementa la suma secuencial y paralela de un vector

public class Main {
    private static final int NUM_EXECUTIONS = 100; //Ejecutar 100 veces
    private static final int NUM_ELEMENTS = 10_000_000;
    private static final int NUM_THREADS = 2;

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        long[] sequentialTimes = new long[NUM_EXECUTIONS];
        long[] parallelTimes = new long[NUM_EXECUTIONS];

        //Ejecucion 100 veces 
        for (int i = 0; i < NUM_EXECUTIONS; i++) {
            int[] array = generateArray(NUM_ELEMENTS);

            long start = System.nanoTime();
            Integer sequentialSum = sequentialSum(array);
            long end = System.nanoTime();
            sequentialTimes[i] = (end - start) / 1_000; //Convierte a microsegundos

            start = System.nanoTime();
            Integer parallelSum = parallelSum(array);
            end = System.nanoTime();
            parallelTimes[i] = (end - start) / 1_000; //Convierte a microsegundos

            assert sequentialSum.equals(parallelSum);
        }

        //Duracion Promedio
        long averageSequentialTime = average(sequentialTimes);
        long averageParallelTime = average(parallelTimes);

        System.out.println("Tiempo secuencial promedio: " + averageSequentialTime + " microsegundos");
        System.out.println("Tiempo paralelo promedio: " + averageParallelTime + " microsegundos");

        double efficiency = (double) averageSequentialTime / averageParallelTime;
        System.out.println("\nEficiencia: " + efficiency);

        //Calculo del trabajo: Suma de los tiempos de las 100 ejecuciones
        long sequentialWork = sum(sequentialTimes);
        long parallelWork = sum(parallelTimes);
        System.out.println("\nTrabajo secuencial: " + sequentialWork + " microsegundos");
        System.out.println("Trabajo paralelo: " + parallelWork + " microsegundos");
    }

    private static int[] generateArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = i;
        }
        return array;
    }

    private static Integer sequentialSum(int[] array) {
        Integer sum = 0;
        for (int value : array) {
            sum += value;
        }
        return sum;
    }

    private static Integer parallelSum(int[] array) throws ExecutionException, InterruptedException {
        ExecutorService executor = Executors.newFixedThreadPool(NUM_THREADS);

        Future<Integer> future1 = executor.submit(() -> sequentialSum(slice(array, 0, array.length / 2)));
        Future<Integer> future2 = executor.submit(() -> sequentialSum(slice(array, array.length / 2, array.length)));

        Integer sum = future1.get() + future2.get();

        executor.shutdown();

        return sum;
    }

    private static int[] slice(int[] array, int start, int end) {
        int[] slice = new int[end - start];
        System.arraycopy(array, start, slice, 0, slice.length);
        return slice;
    }

    private static long average(long[] times) {
        long sum = sum(times);
        return sum / times.length;
    }

    private static long sum(long[] times) {
        long sum = 0;
        for (long time : times) {
            sum += time;
        }
        return sum;
    }
}