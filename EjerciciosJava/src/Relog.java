

import javax.swing.JOptionPane;

public class Relog {
    public static void main(String[]argd){
        int rhor, rmin, rseg;
        JOptionPane.showMessageDialog(null, "Algoritmo relog digital");
        for(rhor=0;rhor < 24;rhor++){
            for(rmin = 0;rmin<60;rmin++){
                for(rseg = 0;rseg< 60;rseg++){
                    JOptionPane.showMessageDialog(null, " "+rhor+":"+rmin+":"+rseg);
                }
            }
        }
    }
}


