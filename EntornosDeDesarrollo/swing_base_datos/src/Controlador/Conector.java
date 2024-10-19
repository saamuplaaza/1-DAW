/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controlador;

import Modelo.Departamento;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Anabel
 */
public class Conector {

    private final String bd = "empresa";
    private final String url = "jdbc:mysql://localhost/";
    private Connection conn = null;
    private final String login = "root";
    private final String password = "";
    private Statement myStmt = null;
    private PreparedStatement myPreStmt = null;
    private ResultSet myRs = null;

    public Connection getConexion() {
        return conn;
    }

    public void close() {
        try {
            if (conn != null) {
                conn.close();
            }
        } catch (SQLException exc) {
            exc.printStackTrace();
        }
    }

    //conectar con la bbdd
    public void conectar() {
        try {
            conn = DriverManager.getConnection(url + bd, login, password);
        } catch (SQLException exc) {
            exc.printStackTrace();
        }
    }

    //alta Departamento
    public int altaDepartamento(String nombre, String localidad) {

        int contador = 0;

        try {

            //Prepara statement con parámetros de entrada
            myPreStmt = conn.prepareStatement("insert into departamentos values(0, ?, ?)");

            //Establecer los parámetros
            myPreStmt.setString(1, nombre);
            myPreStmt.setString(2, localidad);

            //Ejecuta un query SQL, ejecuta una consulta determinada; executeQuery solo se utiliza para
            //consultas y executeUpdate() para el resto.
            contador = myPreStmt.executeUpdate();

        } catch (SQLException ex) {
            ex.printStackTrace();
        } finally {
            cerrarHerramientas(null, myPreStmt, myStmt);
        }
        return contador;

    }

    //borrar Detalle
    public int EliminarEmpleado(int emp_no) {
        int contador = 0;

        try {

            myPreStmt = conn.prepareStatement("delete from empleados where emp_no = ?");
            //Establecer los parámetros
            myPreStmt.setInt(1, emp_no);

            contador = myPreStmt.executeUpdate();

        } catch (SQLException ex) {
            ex.printStackTrace();
        } finally {
            cerrarHerramientas(null, myPreStmt, null);

        }
        return contador;
    }

    //devuelve una lista de departamentos
    public ArrayList<Departamento> listar() {
        ArrayList<Departamento> lista = new ArrayList<>();

        try {

            //Procesa el result set (especie de cursor donde están almacenadas todas las filas que cumplen
            //la condición de la consulta). Se recorre con un bucle while e invocar al método next (que retorna
            //una fila completa), cuando se llega al final del result set el método next retorna false. Para poder
            //acceder a cada uno de los campos de la fila con la que estemos trabajando, se invocan a los métodos get
            //del result set y el tipo de atributo del que se trate procesa los resultados de la consulta
            myStmt = conn.createStatement();
            myRs = myStmt.executeQuery("select * from departamentos");

            while (myRs.next()) {
                Departamento d = new Departamento(myRs.getInt("dept_no"), myRs.getString("dnombre"), myRs.getString("loc"));

                lista.add(d);
            }
        } catch (SQLException ex) {
            Logger.getLogger(Conector.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            cerrarHerramientas(myRs, null, myStmt);
        }

        return lista;
    }

    public void cerrarHerramientas(ResultSet myRs, PreparedStatement myPreStmt, Statement myStmt) {
        try {
            if (myRs != null) {
                myRs.close();
            }

            if (myPreStmt != null) {
                myPreStmt.close();
            }

            if (myStmt != null) {
                myStmt.close();
            }

        } catch (SQLException exc) {
            exc.printStackTrace();
        }
    }
}
