import javax.swing.*;

public class Promedio_notas {
    public  static void main(String[] args){
        int rep,conta,contr, mayore;
        float notas, sumaa,sumap,mayor;
        conta =0;
        contr =0;
        sumaa =0;
        sumap=0;
        mayor =0;
        mayore = 0;
        JOptionPane.showMessageDialog(null, "Promedio de notas ");
        for(rep= 0;rep<5;rep++){
            notas = Float.parseFloat(JOptionPane.showInputDialog("Diga la definitiva del estudiante #"+(rep+1)));
            while(notas<0 || notas> 5){
                notas = Float.parseFloat(JOptionPane.showInputDialog("Nota invalida vuelva a digitar la nota del estudiante #"+(rep+1)));

            }
            if (rep == 0){
                mayor = notas;
            }
            if(notas>mayor){
                mayor = notas;
                mayore = rep+1;

            }
            if(notas >= 3.0f){
                conta= conta +1;
                sumaa= sumaa+notas;
            }
            else{
                contr = contr +1;
                sumap = sumap + notas;

            }
        }
        if(conta>0) {
            JOptionPane.showMessageDialog(null, "La nota promedio de los alumnos aprobados es de " + (sumaa / conta));
        }
        else{
            JOptionPane.showMessageDialog(null, "No aprobo ningun estudiante");
        }
        if(contr>0) {
            JOptionPane.showMessageDialog(null, "La nota promedio que reprobaron es de " + (sumap / contr));
        }
        else{
            JOptionPane.showMessageDialog(null, "No reprobo ningun estudiante");
        }
        JOptionPane.showMessageDialog(null, "La mejor nota es del esrudiante # "+ mayore +1 );


    }
}
