import javax.swing.*;

public class notas {
    public static void main(String[]args){
        float nota,suma,def;
        int capro,rest,rnot;
        JOptionPane.showMessageDialog(null, "Algoritmo INTRO");
        capro=0;
        for(rest=0;rest<4;rest++){
            suma=0;
            for(rnot = 0;rnot<3;rnot++){
                nota = Float.parseFloat(JOptionPane.showInputDialog("Diga nota "+(rnot+1)+" de estudiante # "+(rest+1)));
                suma = suma+nota;

            }
            def = suma/3;
            JOptionPane.showMessageDialog(null, "El estediante # "+ (rest+1)+"tiene una def de "+def);
            if (def>2.95f){
                capro =capro+1;
            }

        }
        JOptionPane.showMessageDialog(null, "Aprobaron"+capro+" Estudiantes ");
    }
}
