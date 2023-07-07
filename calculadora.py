# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

# 1 - Soma
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


def calculadora(n1, n2, operando):
    if operando == '1':
        return n1 + n2
    elif operando == '2':
        return n1 - n2
    elif operando == '3':
        return n1 * n2
    elif operando == '4':
        return n1 / n2
    else:
        return 0

n1 = int(input('Digite o primeiro valor:\n'))
n2 = int(input('Digite o segundo valor:\n'))
operando = input('Digite o número de acordo com o operando desejado:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n')

resultado = calculadora(n1, n2, operando)  # Corrigido: chamando a função calculadora com os argumentos corretos
print(resultado)
