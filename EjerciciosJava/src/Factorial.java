import javax.swing.*;

public class Factorial {
    public static void main(String[] args){
        int cont1;
        int mult= 1;
        JOptionPane.showMessageDialog(null, "Calculadora del numero factorial");
        cont1 = Integer.parseInt(JOptionPane.showInputDialog("Escriba un valor"));
        for(int total = cont1; total > 0; total--){
            mult = mult*total;

        }
        JOptionPane.showMessageDialog(null, "El valor es que usted escojio es de"+cont1+"y el factorial es "+mult);
        
    }
}








