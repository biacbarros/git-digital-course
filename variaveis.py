# 2 - Aula - Variáveis

# 1. Variáveis 
idade = 25 # Criando uma variável em que idade recebe 26
print(idade)
nome = 'Bianca Barros'
print(nome)

"""
Tipos de variáveis
1. INT: Números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
2. FLOAT: Números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
3. STRING OU STR: Cadeias de caracteres, ou seja, dados textuais.
4. BOOLEANO OU BOLL: Valores lógicos (booleanos): True ou False

O Python é Case Sensitive, então terá diferença se você digitar True e true(dá erro)
"""

idade = 25
altura = 1.68
nome = 'Bianca Barros'
estudando = True

print('Idade é do tipo:',type(idade))
print('Altura é do tipo:',type(altura))
print('Nome é do tipo:',type(nome))
print('Estudando é do tipo:',type(estudando))

#Obtendo dados de um usuário
linguagem = input('Qual a linguagem que você está estudando?')
print('A linguagem que você está estudando é', linguagem)
