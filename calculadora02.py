# // Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# // 1: Soma 2: Subtração 3: Multiplicação 4: Divisão 0: Sair

# // Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# // Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# // É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

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
        return None

while True:
  print('[1] - Soma:\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[0] - Sair')

  operando = input('Digite o número da operação desejada:\n')

  if operando == '0':
    print('Programa Encerrado.')
    break

  if operando not in ['1', '2', '3', '4']:
    print('Ocorreu um erro de operação.Tente novamente.\n')
    continue

  n1 = float(input('Digite o primeiro valor:\n'))
  n2 = float(input('Digite o segundo valor:\n'))

  resultado = calculadora(n1, n2, operando)

  if resultado is not None:
    print(f'{n1} {operando} {n2} = {resultado}')
  else:
    print('Operação Inválida. Tente Novamente.\n')      
