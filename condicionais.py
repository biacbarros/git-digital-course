# > Estruturas condicionais

idade = 20

if idade >=18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


"""
Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""
media = float(input('Informe a média do estudante:'))

if media >= 7:
    print('Você foi aprovado!!')
elif media >= 5:
    print('Recuperação, boa sorte')
else:
    print('Você foi reprovado')

""" Caso queira colocar para o aluno ser aprovado uma frequencia nas aulas e a média maior que 7, o código ficará como abaixo:
"""

media2 = 8
presenca = 60

if media2 >= 7 and presenca >=70:
    print('Aprovado!')
else:
    print('Reprovado')
