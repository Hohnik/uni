package Einmaleins;

import java.util.Scanner;

public class Einmaleins {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Wieviele Aufgaben wollen Sie rechnen?: ");
        int problemCount = scanner.nextInt();
        int correctNumber = 0;
        for (int i = 0; i < problemCount; i++) {
            correctNumber += ProblemGenerator.easy();
        }

        int percentile = (int) ((double) correctNumber / (double) problemCount) * 100;
        System.out.printf("%d von %d Aufgaben korrekt (%d)", correctNumber, problemCount, percentile);
        String grats = "";
        if  (percentile >= 99) grats += "Besser gehts nicht!";
        else if  (percentile >= 90) grats += "Fast perfekt!";
        else if  (percentile >= 75) grats += "Weiter so!";
        else if  (percentile >= 50) grats += "Du wirst immer besser!";
        else if  (percentile >= 25) grats += "Guter anfang!";
        else grats += "Versuchs nochmal!";
        System.out.println(grats);

    }

    public static class ProblemGenerator {
        public static int easy() {
            int rnd1 = (int)(Math.random()*10.0d);
            int rnd2 = (int)(Math.random()*10.0d);
            System.out.printf("Was ist %d * %d?%n", rnd1, rnd2);
            Scanner scanner = new Scanner(System.in);
            int input = scanner.nextInt();
            if (input == rnd1 * rnd2) {
                System.out.println("Richtig!");
                return 1;
            } else {
                System.out.println("Falsch");
                return 0;
            }
        }
    }
}

