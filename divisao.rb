puts "=== Calculadora de Divisão ==="

# Solicita os números ao usuário
print "Digite o primeiro número (dividendo): "
dividendo = gets.chomp.to_f

print "Digite o segundo número (divisor): "
divisor = gets.chomp.to_f

# Verifica se o divisor é zero para evitar erro
if divisor == 0
  puts "Erro: Não é possível realizar divisão por zero!"
else
  resultado = dividendo / divisor
  puts "O resultado de #{dividendo} ÷ #{divisor} é: #{resultado}"
end