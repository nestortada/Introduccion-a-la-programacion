import javax.swing.JOptionPane;

public class volumen {
    public static void main(String[] args){
        float r, h ;
        JOptionPane.showMessageDialog(null, "Determionar cual de los dos recipientes esferico o cilindrico tiene mayot capacidad");
        r = Float.parseFloat(JOptionPane.showInputDialog("Digite el valor del radio"));
        h = Float.parseFloat(JOptionPane.showInputDialog("Digite la altura del cilindro"));
        if ((4*3.14f*r*r*r)/3>= 3.14f*r*r*h){
            JOptionPane.showMessageDialog(null, "La esfera con valor de radio"+r+"es tiene mayor capacidad que el cilindro");

        }
        else{
            if((4*3.14f*r*r*r)/3 == 3.14f*r*r*h){
                JOptionPane.showMessageDialog(null, "El cilindro y la esfera tienen la misma capacidad con altura y radio"+h+" "+r);
            }
            else{
                JOptionPane.showMessageDialog(null, "El cilindro tiene mayor capacidad que la esfera con altura "+h+" y radio"+r);
            }
        }
    }
}
