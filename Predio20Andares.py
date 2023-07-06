
# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13. Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Ordem Decrescente;

for j in range(20,0,-1):
  if j != 13:
    print(j)

#Ordem Decrescente:
num = 20
while num > 0:
  if num != 13:
    print(num)
  num -= 1

#Ordem Descrescente:
num = 21
for i in range(20, 0, -1):
  num -= 1
  if num ==13:
    continue
  print(num)  
