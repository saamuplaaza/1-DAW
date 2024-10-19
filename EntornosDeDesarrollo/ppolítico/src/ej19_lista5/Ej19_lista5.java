package ej19_lista5;

import java.util.Random;
import java.util.Scanner;

public class Ej19_lista5 {

    public static void main(String[] args) {
        // TODO code application logic here
        Random rnd = new Random();
        Scanner sc = new Scanner(System.in);
        Scanner scs = new Scanner(System.in);
        String provincia;
        boolean encontrado;

        String prov[] = {"ALMERIA", "CADIZ", "CORDOBA", "GRANADA",
            "HUELVA", "JAEN", "MALAGA", "SEVILLA"};
        int p1[] = new int[prov.length];
        int p2[] = new int[prov.length];

        for (int i = 0; i < prov.length; i++) {
            p1[i] = rnd.nextInt(10000);
            p2[i] = rnd.nextInt(10000);
        }
        int opcion = 0;
        do {
            System.out.println("---------- MENU -----------");
            System.out.println("1.- Mostrar resultados");
            System.out.println("2.- Mostrar el número de votos "
                    + "de una provincia");
            System.out.println("3.- Partido político ganador");
            System.out.println("4.- Salir");
            System.out.println("Introduce una opción:");
            opcion = sc.nextInt();
            switch (opcion) {
                case 1:
                    System.out.printf("%10s", " ");
                    for (int i = 0; i < prov.length; i++) {
                        System.out.printf("%10s", prov[i]);
                    }
                    System.out.printf("\n%10s", "P1");
                    for (int i = 0; i < prov.length; i++) {
                        System.out.printf("%10d", p1[i]);
                    }
                    System.out.printf("\n%10s", "P2");
                    for (int i = 0; i < prov.length; i++) {
                        System.out.printf("%10d", p2[i]);
                    }
                    System.out.println("");
                    break;
                case 2:
                    System.out.println("Introduce la provincia: ");
                    provincia = scs.nextLine();
                    int pos = encontrarProvincia(prov, provincia);
                    if (pos != -1) {
                        System.out.printf("Votos p1=%d p2=%d, total: %d\n", p1[pos], p2[pos], p1[pos] + p2[pos]);
                    } else {
                        System.out.println("Esta provincia no existe.");
                    }
                    /*encontrado = false;
                    for (int i = 0; i < prov.length && !encontrado;i++) {
                        if (provincia.equalsIgnoreCase(prov[i])) {
                            encontrado = true;
                            System.out.printf("Votos p1=%d p2=%d, total: "
                                    + "%d\n", p1[i], p2[i], p1[i] + p2[i]);
                        }
                    }
                    if (!encontrado) {
                        System.out.println("Esta provincia no existe");
                    }*/
                    break;
                case 3:
                    int acu1 = 0,
                     acu2 = 0;
                    for (int j = 0; j < p1.length; j++) {
                        acu1 += p1[j];
                        acu2 += p2[j];
                    }
                    System.out.printf("P1 obtuvo %d votos mientras "
                            + "P2 obtuvo %d\n", acu1, acu2);
                    if (acu1 > acu2) {
                        System.out.println("El ganador es P1");
                    } else if (acu1 < acu2) {
                        System.out.println("El ganador es P2");
                    } else {
                        System.out.println("Ambos empatan");
                    }
                    break;
                case 4:
                    System.out.println("Hasta luego");
                    break;
                default:
                    System.out.println("Opción incorrecta");
                    break;
            }

        } while (opcion != 4);
    }

    public static int encontrarProvincia(String prov[], String provincia) {
        int posicion = -1;
        for (int i = 0; i < prov.length; i++) {
            if (provincia.equalsIgnoreCase(prov[i])) {
                posicion = i;

            }
        }
        return posicion;

    }

}
