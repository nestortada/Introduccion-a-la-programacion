import javax.swing.*;

public class examenprimeraparte {
    public static void main(String[] args){
        float x,y,b0,b1,suma1,suma2,suma3,suma4,suma5,suma6,mult,mult1,mult2,mult3,suma7,suma8,suma9,suma10,suma11,mult4;
        int n1,rep,n2;
        suma1=0;
        suma2 = 0;
        suma3 = 0;
        suma4=0;
        suma5=0;
        suma6=0;
        suma7=0;
        suma8=0;
        suma9=0;
        suma10=0;
        suma11=0;
        x = Float.parseFloat(JOptionPane.showInputDialog("Cual quieres que sea el valor de X"));
        y = Float.parseFloat(JOptionPane.showInputDialog("Cual quieres que sea el valor de y"));
        n1 = Integer.parseInt(JOptionPane.showInputDialog("Cual quieres que sea el valor de n para la cordenada del origen"));
        for(rep=0;rep<n1+1;rep++){
            suma1= suma1 + y;
            mult=x*x;
            suma2 =suma2 +mult;
            suma3 = suma3 +x;
            mult1=x*y;
            suma4=suma4 +mult1;
            mult2= x*x;
            suma5= suma5+mult2;
            suma6=suma6+x;
        }
        b0= ((suma1*suma2)-(suma3*suma4))/((n1*suma5)-(suma6*suma6));
        n2=Integer.parseInt(JOptionPane.showInputDialog("Diga un numero para el valor de n para la pendiente"));
        for (rep = 0;rep<n2+1;rep++){
            mult3 =x*y;
            suma7 = suma7 + mult3;
            suma8= suma8 + x;
            suma9= suma9 +y;
            mult4= x*x;
            suma10= suma10+mult4;
            suma11=suma11+x;
        }
        b1=((n2*suma7)-(suma8*suma9))/((n2*suma10)-(suma11*suma11));
        JOptionPane.showMessageDialog(null,"la formula de la pendiente es Y ="+b0+" + "+b1+"x");











    }
}
