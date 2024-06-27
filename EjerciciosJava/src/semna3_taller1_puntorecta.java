import javax.swing.JOptionPane;

public class semna3_taller1_puntorecta {
    public static void main(String[] args) {
        float y,x,b,m;
        JOptionPane.showMessageDialog(null, "El valor de la recta es Y= Mx+B");
        y = Float.parseFloat(JOptionPane.showInputDialog("Agrega el valor el y"));
        b = Float.parseFloat(JOptionPane.showInputDialog(("Agrega el valor del punto de Corte (b)")));
        m = Float.parseFloat(JOptionPane.showInputDialog(("Agregar el valor de y la pendiente (m)")));
        x = Float.parseFloat(JOptionPane.showInputDialog(("Agrega el valor de x")));
        if(y == (m*x)+b) {
            JOptionPane.showMessageDialog(null, "Los valores x,y pertenece a la recta ");
        }
        else{
                JOptionPane.showMessageDialog(null, "Los valores x,y no pertenecen a la recta");

            }
    }
}
