import javax.swing.*;

public class Suma {
    public static void main(String[] args){
        float suma, n1;
        suma =0;
        n1=1;
        JOptionPane.showMessageDialog(null, "Para parar la suma digite cero(0)");
        while (n1 !=0){
            n1=Float.parseFloat(JOptionPane.showInputDialog("Digite un numero"));
            suma = n1+suma;
        }
        JOptionPane.showMessageDialog(null,"La suma de los numeros dados son"+suma);
    }
}
