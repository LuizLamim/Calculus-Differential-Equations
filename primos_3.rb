require 'prime'

# Calcula os 3 primeiros números primos
primeiros_primos = Prime.first(3)

puts "Os 3 primeiros números primos são: #{primeiros_primos.join(', ')}"