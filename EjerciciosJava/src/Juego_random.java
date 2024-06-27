import javax.swing.*;
import java.util.Random;

public class Juego_random {
    public static void main(String[]args){
        int numsecreto,num, cont;
        cont=1;
        Random rnd = new Random();
        numsecreto = rnd.nextInt(100);
        num= Integer.parseInt(JOptionPane.showInputDialog("El juego se tarta de adivinar un numero que esta dentro del uno al cien, ¿ Diga un numero?"));
        while(numsecreto != num){
            if(num<numsecreto){
                JOptionPane.showMessageDialog(null, "El numero que usted dijo es menor al numero que toca adivinar");
                num= Integer.parseInt(JOptionPane.showInputDialog("Diga un numero mayor al que acaba de decir"));
            }
            else {
                JOptionPane.showMessageDialog(null, "El numero que usted dijo es mayor  al numero que toca adivinar");
                num = Integer.parseInt(JOptionPane.showInputDialog("Diga un numero menor para adivinaar"));
            }
            cont=cont+1;

        }
        if (num == numsecreto){
            if(3>cont){
            JOptionPane.showMessageDialog(null, "Felicitaciones eres muy suertudo el numero era "+num+" Usted dijo el numero en "+(cont)+" intentos");
        }
            else{
                if (6>cont){
                    JOptionPane.showMessageDialog(null,"Felicitaciones te demorates un poco pero lo lograste, el numero era "+num+" Usted dijo el numero en "+(cont)+" intentos");
                }
                else{
                    if(10>cont){
                        JOptionPane.showMessageDialog(null, "Felicitaciones casi que no logras adivinar el numero era "+num+" Usted dijo el numero en "+(cont)+" intentos");
                    }
                }
            }
        }

    }
}
