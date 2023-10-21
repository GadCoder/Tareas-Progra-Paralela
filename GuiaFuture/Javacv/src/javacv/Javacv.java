/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javacv;
 
/**
 *
 * @author Stefano HB
 */
import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import java.util.concurrent.*;
import java.util.*;
import org.bytedeco.opencv.opencv_core.IplImage;
import org.bytedeco.javacv.*;


public class Javacv {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws InterruptedException, ExecutionException{
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        String directorioActual = System.getProperty("user.dir");
        String imagenPath = directorioActual + "\\src\\img\\image.png";
        Mat imagenOG = Imgcodecs.imread(imagenPath);
        
        int numThreads = Runtime.getRuntime().availableProcessors();
        int filasxThread = imagenOG.rows()/numThreads;
        ExecutorService executorService = Executors.newFixedThreadPool(numThreads);
        
        List<Future<Mat>> futures = new ArrayList<>();
        
        for (int i = 0; i<numThreads; ++i){
            int inicioFila = i*filasxThread;
            int finalFila = (i == numThreads-1) ? imagenOG.rows() : (i+1) * filasxThread;
            Future<Mat> future = executorService.submit(new ImageTask(imagenOG.clone(), inicioFila, finalFila));
            futures.add(future);
        }
       
        Mat imagenFinal = new Mat(imagenOG.size(), imagenOG.type());
        try{
            for (int i=0; i<numThreads; ++i){
                int inicioFila = i*filasxThread;
                int finalFila = (i == numThreads-1) ? imagenOG.rows() : (i+1) * filasxThread;
                Mat resultadoParcial = futures.get(i).get();
                resultadoParcial.copyTo(imagenFinal.rowRange(inicioFila,finalFila).colRange(0,imagenFinal.cols()));
            }
        } catch (InterruptedException | ExecutionException e){
            e.printStackTrace();
        }
        
        mostrarImagen("Original", imagenOG);
        mostrarImagen("Prueba", imagenFinal);
        System.out.println(Core.VERSION);
        executorService.shutdown();
        // TODO code application logic here
    }
    
    public static void mostrarImagen(String titulo, Mat imagen){
        CanvasFrame canvas = new CanvasFrame(titulo,1);
        canvas.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
        OpenCVFrameConverter.ToMat convertidor = new OpenCVFrameConverter.ToMat();
        canvas.showImage(convertidor.convert(imagen));
    }
    
}


