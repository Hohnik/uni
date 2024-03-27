package Volumenberechner;

import Volumenberechner.Flaechenberechner;

public class Main {
    public static void main(String[] args){
//        for (String arg : args) {
//            System.out.println(arg);
//        }
        switch (args.length) {
            case 1:
                Flaechenberechner.kreis(args[0]);
                break;
            case 2:
                Flaechenberechner.pyramide(args[0], args[1]);
                break;
            case 3:
                Flaechenberechner.quader(args[0], args[1], args[2]);
                break;
            default:
                Flaechenberechner.help();
        }
    }
}
