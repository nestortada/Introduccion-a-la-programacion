import javax.swing.*;

public class Variabledimension {
    public static void main(String[] args){
        int identidad[][];
        int repf,repc;
        String acum;
        identidad= new int[10][10];
        acum = "-";
        for(repf = 0;repf<10;repf ++){
            acum = acum + "\n";
             for(repc = 0; repc<10;repc++){
                 if(repc == repf){
                     identidad[repf][repc]=1;
                 }
                 else{
                     identidad[repf][repc]= 0;
                 }
                 acum = acum + identidad[repf][repc]+"-";
            }
        }
        JOptionPane.showMessageDialog(null, acum);
    }   
}
