# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

import datetime

ano_atual = datetime.date.today().year


while True:
    nome = input('Nome completo:\n')
    ano_nasc = int(input('Digite aqui o ano do seu nascimento:\n'))
  
    try:

        if 1922 <= ano_nasc <= 2021:
            idade = ano_atual - ano_nasc
            print(f'Nome: {nome}\nIdade: {idade}')
            break
        else:
            print('Ano de nascimento inválido. Tente novamente.')  

    except ValueError:
      print('Entrada Inválida')   
