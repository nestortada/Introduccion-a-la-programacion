import javax.swing.*;

public class reunion {
    public static void main(String[] args){
        int edad, suma, cont, sigue,menor =0;
        JOptionPane.showMessageDialog(null, "Promedio de edad en la reunion");
        suma=0;
        cont=0;
        sigue = 1;
        while (sigue == 1){
            edad=Integer.parseInt(JOptionPane.showInputDialog("Diga su edad"));
            while (edad<0 || edad>120){
                edad=Integer.parseInt(JOptionPane.showInputDialog("La edad es invalida, diga de nuevo su edad"));
            }
            suma =suma + edad;
            cont = cont +1;
            JOptionPane.showMessageDialog(null, "Si hay mas personas escriba 1 y si no hay mas escriba dos");
            sigue = Integer.parseInt(JOptionPane.showInputDialog("Siguen mas personas en la reunion"));
            while (sigue !=1 && sigue!=2){
                sigue=Integer.parseInt(JOptionPane.showInputDialog("la respuesta es invalida, siguen mas personas si(1)/no(2)"));
            }
            if(cont==1){
                menor=edad;
            }
            if(menor>edad){
                menor =edad;

            }

        }
        JOptionPane.showMessageDialog(null, "La edad promedio de los que estan en la reunion es"+(suma/cont));
        JOptionPane.showMessageDialog(null, "La menor edad en la reunion es de "+menor);
    }
}
