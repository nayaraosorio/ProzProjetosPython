# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

n1 = int(input('Digite o primeiro valor:\n'))
n2 = int(input('Digite o segundo valor:\n'))
operando = input('Digite o número de acordo com o operando desejado;\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n')

if operando == '1':
  soma = n1 + n2
  print(f'{n1} + {n2} = {soma}')
elif operando == '2':
  subt = n1 - n2
  print(f'{n1} - {n2} = {subt}')
elif operando == '3':
  multi = n1 * n2
  print(f'{n1} * {n2} = {multi}')  
elif operando == '4':
  divisao = n1 / n2
  print(f'{n1} / {n2} = {divisao}')    
else:
  print('0')      
