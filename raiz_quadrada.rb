# Programa para calcular a raiz quadrada em Ruby

puts "Digite um número para calcular a raiz quadrada:"
entrada = gets.chomp.to_f

if entrada >= 0
    resultado = Math.sqrt(entrada)
    puts "A raiz quadrada de #{entrada} é #{resultado}"
else