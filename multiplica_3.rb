# Programa interativo para multiplicar 3 números
puts "--- Calculadora de Multiplicação ---"

puts "Digite o primeiro número:"
num1 = gets.chomp.to_f

puts "Digite o segundo número:"
num2 = gets.chomp.to_f

puts "Digite o terceiro número:"
num3 = gets.chomp.to_f

resultado = num1 * num2 * num3

puts "O resultado da multiplicação é: #{resultado}"