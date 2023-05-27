# > Funções

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente ...

# print() # Imprime uma mensagem (Int, Float, Str) no console (terminal,cmd)
# input() # Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
# len() # Recebe uma lista e retorna o tamanho da lista
# max() # Retorna o maior valor de uma lista

# 2. Criação de Funções

# Função inicial

def saudacao(): #Declarando a função
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte deste curso!')

saudacao()
saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome,curso): #Declarando a função
    print(f'Seja bem-vinda(o),{nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')
saudacao('Bianca','Python')
saudacao('Aline','JavaScript')

# Função com parâmetros default
def saudacao(nome,curso='Python'): #Declarando a função
    print(f'Seja bem-vinda(o),{nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')
saudacao('Bianca')
saudacao('Bianca','C++')

# Funções com retornos
def soma(num1,num2):
    return num1 + num2 #Depois que coloca um return, a função acaba

resultado = soma(5,7)
print('O resultado da soma é', resultado)

def calculadora(num1,num2,operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    
resultado1 = calculadora(10,20)
resultado2 = calculadora(10,20,'-')
resultado3 = calculadora(10,20,'*')
resultado4 = calculadora(10,20,'/')

print(resultado1,resultado2,resultado3,resultado4)