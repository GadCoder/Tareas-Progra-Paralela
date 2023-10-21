/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javacv;
import java.util.concurrent.*;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.*;
import java.util.Random;
/**
 *
 * @author Stefano HB
 */
public class ImageTask implements Callable<Mat>{
    
    Mat _imagenOG;
    int _inicioFila;
    int _finalFila;
    
    
    public ImageTask (Mat imagenOG, int inicioFila, int finalFila){
        this._imagenOG = imagenOG;
        this._inicioFila = inicioFila;
        this._finalFila = finalFila;
    }
    
    @Override
    public Mat call() throws Exception{
        Mat imagenParcial = new Mat(_imagenOG, new Rect(0, _inicioFila, _imagenOG.cols(), _finalFila-_inicioFila));
        
        Imgproc.GaussianBlur(imagenParcial, imagenParcial, new Size(3,3),_inicioFila);
        Imgproc.applyColorMap(imagenParcial, imagenParcial, new Random().nextInt(10));
        Imgproc.Canny(imagenParcial, _imagenOG, 5.5, 4.5);
        return imagenParcial;
    }
    
}
