import javax.swing.JOptionPane;

public class Semana_3_tarea1 {
    public static void main(String [] args){
        float a,b,c;
        JOptionPane.showMessageDialog(null, "Identificar cual tipo de triangulo es");
        a = Float.parseFloat(JOptionPane.showInputDialog("diga cuanto vale el lado de un trinagulo "));
        b = Float.parseFloat(JOptionPane.showInputDialog("diga cuanto vale el lado de un trinagulo "));
        c = Float.parseFloat(JOptionPane.showInputDialog("diga cuanto vale el lado de un trinagulo "));

        if(a == b && b == c){
            JOptionPane.showMessageDialog(null, "Los valores de "+a+", "+b+", "+c+" corresponden a un triangulo equilatero");
        }
        else{
            if (a == b || b==c || a==c ){
                JOptionPane.showMessageDialog(null, "Los valores de "+a+", "+b+", "+c+" corresponden a un triangulo isoceles ");
            }
            else{
                JOptionPane.showMessageDialog(null, "Los valores de "+a+", "+b+", "+c+" corresponden a un triangulo escaleno");
            }
        }
        float h, k ,l;
        JOptionPane.showMessageDialog(null, "Puntos que pertenezcan al intervalo");
        h = Float.parseFloat(JOptionPane.showInputDialog("Diga un valor"));
        k = Float.parseFloat(JOptionPane.showInputDialog("Diga un valor"));
        l = Float.parseFloat(JOptionPane.showInputDialog("Diga un valor"));
        if( k<h && h<=l){
            JOptionPane.showMessageDialog(null, "El punto "+ h+ "  pertenece a los puntos entre ("+k+","+l+"]");
        }
        else{
            JOptionPane.showMessageDialog(null, "el punto "+h+" no pertenece a los puntos entre ("+k+","+l+"]");
        }

    }


}
