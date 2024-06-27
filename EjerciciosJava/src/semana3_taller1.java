import javax.swing.JOptionPane;

public class semana3_taller1 {
    public static void main(String[] args){
        float nota;
        nota = Float.parseFloat(JOptionPane.showInputDialog("Diga la nota del semestre"));
        if (nota >= 3.5f) {
            JOptionPane.showMessageDialog(null,"Usted aprobo la materia con "+nota);
        }
        if (nota < 3.5f){
            JOptionPane.showMessageDialog(null, "usted no aprobo la materia y su definitiva quedo en "+ nota);
        }
    }
}
