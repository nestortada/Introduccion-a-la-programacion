import javax.swing.JOptionPane;

public class semana2_tarea1 {
    public static void main(String[] args){
        float a1, a2, t1, ra, rt;
        a1= Integer.parseInt(JOptionPane.showInputDialog("Digite el ancho del rectangulo en M"));
        a2 = Integer.parseInt(JOptionPane.showInputDialog("Digite el largo del ractangulo M "));
        ra = a1 * a2;
        JOptionPane.showMessageDialog(null,"El area del rectangulo dado por ancho "+a1+" y el largo "+a2+" es "+ra+" M al cuadrado");
        t1= Integer.parseInt(JOptionPane.showInputDialog("Digite la temperatura en grados celcius"));
        rt = (t1*9/5)+32;
        JOptionPane.showMessageDialog(null, " "+t1+" a Fahrenheit es "+rt);
    }
}
