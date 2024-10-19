/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio.pkg2.netbeans;

import java.util.Scanner;

/**
 *
 * @author Samuel
 */
public class Ejercicio2NetBeans {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println("Introduce el primer numero: ");
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        System.out.println("Introduce el segundo numero: ");
        int num2= sc.nextInt();
        System.out.println("El producto es: " + (num1*num2));
    }
}