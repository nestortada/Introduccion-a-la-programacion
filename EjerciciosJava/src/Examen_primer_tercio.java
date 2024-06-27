import javax.swing.*;

public class Examen_primer_tercio {
    public static void main(String[] args){
        int rep,contr,contt,totalr,est,suma,total,menor;
        JOptionPane.showMessageDialog(null,"LLegada a la U");
        est = Integer.parseInt(JOptionPane.showInputDialog("Cuantos estudiantes llegan a la U"));
        contr=0;
        suma=0;
        total=0;
        totalr=0;
        menor=0;
        for(rep=0;rep<est;rep++){
            contt= Integer.parseInt(JOptionPane.showInputDialog("Cuanto se demora en llegar el estudiante # "+(rep+1)));
            if(rep==0){
                menor = contt;
            }
            if (contt<30){
                suma = suma+1;
            }
            if (contt>60){
                contr = contr+1;
                totalr = totalr+contt;
            }
            total=total+contt;
            if(contt<menor){
                menor = contt;
            }
        }
        JOptionPane.showMessageDialog(null,"el promedio que los estudiantes se demoran en llegar es de "+(total/est)+" minutos");
        JOptionPane.showMessageDialog(null, "El numero de estudiantes que se demoran antes de los 30 minutos son"+suma);
        JOptionPane.showMessageDialog(null, "El promediode de tiempo de los estudiantes que se demoran mas de 60 minutos es"+(totalr/contr));
        JOptionPane.showMessageDialog(null, "El estudiante que llega mas rapido a la U es "+menor+" minutos");

    }
}
