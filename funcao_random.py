"""A função random() gera números reais (float) entre 0 (incluído) e 1 (não incluído) que podem representar a problabilidade de um evento acontecer:
"""
import random

x = random.random()

print(x)
"""
As funções randrange() e randint() geram aleatoriamente um número inteiro dentro de um intervalo dado pelo usuário. Semelhantemente a função random(), o limite inferior do intervalo é incluído, mas o superior não.
"""
x = random.randint(1,52)

print(x)

x = random.randrange(1,52)

print(x)

