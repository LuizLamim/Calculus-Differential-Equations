#elevar
puts "=== Calculadora de Potenciação ==="
print "Digite o número base: "
base = gets.chomp.to_f

print "Digite o expoente: "
expoente = gets.chomp.to_f

# O operador ** é a forma nativa do Ruby para exponenciação
resultado = base ** expoente