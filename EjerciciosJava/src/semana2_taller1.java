import javax.swing.JOptionPane;

public class semana2_taller1 {
    public static void main(String[] args){
        float num1, num2, respS, respM, respMod, repsRe;
        num1= Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        num2= Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        respS = num1 + num2;
        respM = num1 * num2;
        respMod = (num1 % num2);
        repsRe = num1 - num2;
        JOptionPane.showMessageDialog(null, "El primer numero que digitaste fue "+ num1 + " y el segundo fue "+ num2);
        JOptionPane.showMessageDialog(null, "La suma de esos dos numeros es "+ respS);
        JOptionPane.showMessageDialog(null,"La mulltiplicacion de esos dos numeros es "+ respM);
        JOptionPane.showMessageDialog(null, "El modulo de "+ num1+" sobre "+num2+" es "+respMod);
        JOptionPane.showMessageDialog(null, "La resto de "+num1+" menos "+ num2+" es "+ repsRe);

    }
}
