using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o número base: ");
        double baseNum = Convert.ToDouble(Console.ReadLine());

        Console.Write("Digite o expoente: ");
        double expoente = Convert.ToDouble(Console.ReadLine());

        // O método Math.Pow realiza o cálculo de elevação
        double resultado = Math.Pow(baseNum, expoente);

        Console.WriteLine($"{baseNum} elevado a {expoente} é igual a {resultado}");
    }
}