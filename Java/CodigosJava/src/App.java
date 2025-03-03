import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite um numero: ");
        int numero = scanner.nextInt();

        System.out.println("Tabuada do nº " + numero + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + " x " + i + " : " + (numero*i));
        }

    }
}
