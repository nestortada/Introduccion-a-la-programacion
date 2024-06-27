import javax.swing.JOptionPane;
public class Ejemplo {
    public static void main (String[] args){
        String persona;
        int edad;

        JOptionPane.showMessageDialog(null,"Bienvenido al Ejemplo");
        persona = JOptionPane.showInputDialog("Diga su nombre");
        edad = Integer.parseInt(JOptionPane.showInputDialog("Diga su edad"));
        JOptionPane.showMessageDialog(null,persona+" tu edad es de "+ edad + " años");
    }
}
