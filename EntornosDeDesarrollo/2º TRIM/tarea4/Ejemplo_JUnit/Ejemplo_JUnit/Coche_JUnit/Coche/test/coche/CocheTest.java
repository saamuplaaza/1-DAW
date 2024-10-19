/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit3TestClass.java to edit this template
 */
package coche;

import junit.framework.TestCase;

/**
 *
 * @author Samuel
 */
public class CocheTest extends TestCase {
    
    public CocheTest(String testName) {
        super(testName);
    }


    /**
     * Test of comprar method, of class Coche.
     */
    /**public void testComprar() throws Exception {
        System.out.println("comprar");
        int cantidad = 0;
        Coche instance = new Coche();
        instance.comprar(cantidad);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }*/
    
    public void testComprarValido() throws Exception {
        System.out.println("Test de prueba para Comprar un número positivo de coches.");
        int cantidad = 100;
        try{
            Coche coche1 = new Coche("Ford", 12000, 300);
            coche1.comprar(cantidad);
            assertTrue(coche1.obtenerStock()==400);
        } catch (Exception e){
            fail ("Se ha producido una excepción no esperada: " + e);
        }
    }
    
    public void testComprarNoValidoNegativo() throws Exception {
        System.out.println("Test de prueba para Comprar un número negativo de coches.");
        int cantidad = -100;
        Coche coche1 = new Coche("Ford", 12000, 300);
        try{
            coche1.comprar(cantidad);
            fail ("Intento de comprar un número negativo de coches.");
        } catch (Exception e){
            System.out.println(e);
            assertTrue(coche1.obtenerStock()==300);
        }
    }

    public void testVenderValido() throws Exception {
        System.out.println("Test de prueba para vender un número positivo y menor que el stock de coches.");
        int cantidad = 200;
        Coche coche1 = new Coche("Ford", 12000, 300);
        try{
            coche1.vender(cantidad);
            assertTrue(coche1.obtenerStock()==100);
        } catch (Exception e){
            fail("Se ha producido una excepción no esperada: "+e);
        }
    }
    
    public void testVenderNoValidoNegativo() throws Exception {
        System.out.println("Test de prueba para vender un número negativo de coches.");
        int cantidad = -200;
        Coche coche1 = new Coche("Ford", 12000, 300);
        try{
            coche1.vender(cantidad);
            fail("Intento de vender un número negativo de coches.");
        } catch (Exception e){
            System.out.println(e);
            assertTrue(coche1.obtenerStock()==300);
        }
    }
        
    public void testVenderNoValidoMayor() throws Exception {
        System.out.println("Test de prueba para vender un número positivo pero mayor que el stock de coches.");
        int cantidad = 400;
        Coche coche1 = new Coche("Ford", 12000, 300);
        try{
            coche1.vender(cantidad);
            fail("Intento de vender más coches de los que hay en stock.");
        } catch (Exception e){
            System.out.println(e);
            assertTrue(coche1.obtenerStock()==300);
        }    
    }
}
