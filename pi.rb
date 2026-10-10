# Carrega as bibliotecas necessárias para alta precisão
require 'bigdecimal'
require 'bigdecimal/math'

# Definimos a precisão para 21 dígitos significativos:
# 1 dígito antes da vírgula (3) + 20 casas decimais.
precisao = 21

# Calcula o Pi com a precisão desejada
pi_com_precisao = BigMath.PI(precisao)

# Exibe o resultado formatado em ponto fixo
puts "Valor de Pi com 20 casas decimais:"
puts pi_com_precisao.to_s('F')