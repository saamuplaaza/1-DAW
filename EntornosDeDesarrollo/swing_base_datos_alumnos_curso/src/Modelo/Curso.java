/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo;

/**
 *
 * @author Anabel
 */
public class Curso {
    private int codigo;
    private String nombre;
    private String centro;
    private int costeMatrícula;

    public Curso(int codigo, String nombre, String centro, int costeMatrícula) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.centro = centro;
        this.costeMatrícula = costeMatrícula;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCentro() {
        return centro;
    }

    public void setCentro(String centro) {
        this.centro = centro;
    }

    public int getCosteMatrícula() {
        return costeMatrícula;
    }

    public void setCosteMatrícula(int costeMatrícula) {
        this.costeMatrícula = costeMatrícula;
    }


    
}
