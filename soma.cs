using System;

namespace SomaDeDoisNumeros
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("--- Program de Soma de 2 Números ---");

            // Solicita o primeiro número
            Console.Write("Digite o primeiro número: ");
            double numero1 = Convert.ToDouble(Console.ReadLine());

            // Solicita o segundo número
            Console.Write("Digite o segundo número: ");
            double numero2 = Convert.ToDouble(Console.ReadLine());

            // Realiza a soma
            double soma = numero1 + numero2;

            // Exibe o resultado
            Console.WriteLine($"\nA soma de {numero1} + {numero2} é igual a: {soma}");
        }
    }
}