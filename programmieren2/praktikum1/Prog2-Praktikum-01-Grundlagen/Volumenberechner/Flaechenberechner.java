package Volumenberechner;

public class Flaechenberechner {

    public static void help(){
        System.out.println("Verfügbare Berechnungen:");
        System.out.println("Kugel: Radius");
        System.out.println("Pyramide: Grundseite Höhe");
        System.out.println("Länge Breite Höhe");
    }
    public static void kreis(String radius){
        System.out.println(4.0/3*Math.PI*Math.pow(Float.parseFloat(radius),3));
    }
    public static void pyramide(String grundseite, String height){
        System.out.println(1.0 / 3.0 * Math.pow(Float.parseFloat(grundseite),2) * Float.parseFloat(height));
    }

    public static void quader(String length, String width, String height){
        double l = Double.parseDouble(length);
        double w = Double.parseDouble(width);
        double h = Double.parseDouble(height);
        System.out.println(l*w*h);
    }
}
