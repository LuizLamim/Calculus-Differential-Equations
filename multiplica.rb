# Função para multiplicar dois números
def multiplicar(a, b)
  a * b
end

# Solicitando os números ao usuário
print "Digite o primeiro número: "
num1 = gets.chomp.to_f

print "Digite o segundo número: "
num2 = gets.chomp.to_f

# Calculando e exibindo o resultado
resultado = multiplicar(num1, num2)
puts "O resultado da multiplicação é: #{resultado}"