import random
numero_sorteado = random.randint(1,20)
numero_tentativas = 1
numero_escolhido = int(input('Informe um número entre 1 e 20:'))
"""
if numero_sorteado == numero_escolhido:
    print('Você acertou!')
else:
    print('Você errou, o número sorteado é: ',numero_sorteado)
"""
"""Refazendo o código utilizando um laço de repetição, While = Enquanto"""

while numero_sorteado != numero_escolhido:
    print('Você errou, tente novamente...')
    numero_tentativas = numero_tentativas + 1
    numero_escolhido = int(input('Informe um número entre 1 e 20:'))

print('Parabéns, você acertou, número de tentativas:',numero_tentativas)

#Exemplo 2: Estrutura com contador

contador = 0

while contador < 5:
    print('contador')
    contador = contador + 1