import javax.swing.*;

public class Ejercicio_en_clase {
    public static void main(String[] args){
        float num_e,rep,notamax,notamin;
        String nombres_e,mejor_e,peor_e;
        notamax=0;
        notamin=5;
        mejor_e="pepe";
        peor_e="pepe";
        for(rep=0;rep<6;rep++){
            nombres_e= JOptionPane.showInputDialog("Digite el nombre estudiante #"+(rep+1));
            num_e=Float.parseFloat(JOptionPane.showInputDialog("digite la nota de "+nombres_e));
            if(num_e>notamax){
                notamax=num_e;
                mejor_e=nombres_e;
            }
            if (num_e<notamin){
                notamin=num_e;
                peor_e=nombres_e;
            }

        }
        JOptionPane.showMessageDialog(null,"El mejor estudiante es "+mejor_e+" con "+notamax);
        JOptionPane.showMessageDialog(null,"el peor estudiante es "+peor_e+" con "+notamin);

    }
}
