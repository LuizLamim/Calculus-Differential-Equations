import java.util.Scanner;

public class PotenciaPi {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número base: ");
        double base = scanner.nextDouble();

        // Eleva o número digitado à potência de Pi
        double resultado = Math.pow(base, Math.PI);

        System.out.println("Valor de Pi (π): " + Math.PI);
        System.out.printf("%.2f elevado a π é igual a: %.6f%n", base, resultado);

        scanner.close();
    }
}