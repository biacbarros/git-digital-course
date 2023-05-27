#Contar a variável de 0 até 9
print('Contar a variável de 0 até 9')
for variavel in range(10):
    print(variavel)

#Contar a variável de 1 até 4, ele sempre vai até o valor menor.
print('Contar a variável de 1 até 4, ele sempre vai até o valor menor')
for variavel in range(1,5):
    print(variavel)

#Contar a variável de 1 até menor que 12, pulando de 3 em 3   
print('Contar a variável de 1 até menor que 12, pulando de 3 em 3 ') 
for variavel in range(1,12,3):
    print(variavel)

soma = 0

for i in range(1,4):
    nota = float(input(f'Informe sua nota {i}: '))
    soma = soma + nota
print(soma/3)