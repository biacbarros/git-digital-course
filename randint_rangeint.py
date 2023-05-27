"""Na documentação da função randint(), há uma nota técnica dizendo que a função randint(start, stop) é somente um alias, ou seja, um apelido ou um atalho para o uso da função randrange(start, stop + 1).

Portanto o funcionamento das duas funções é o mesmo, a diferença se dá somente a forma que você passa os parâmetros."""

import random
x0 = x1 = x2 = x3 = x4 = x5 = 0
y0 = y1 = y2 = y3 = y4 = y5 = 0


for i in range(101):
    x = random.randint(0, 5)
    y = random.randrange(0, 6, 1)
    if x == 0:
        x0 += 1
    elif x == 1:
        x1 += 1
    elif x == 2:
        x2 += 1
    elif x == 3:
        x3 += 1
    elif x == 4:
        x4 += 1
    elif x == 5:
        x5 += 1

    if y == 0:
        y0 += 1
    elif y == 1:
        y1 += 1
    elif y == 2:
        y2 += 1
    elif y == 3:
        y3 += 1
    elif y == 4:
        y4 += 1
    elif y == 5:
        y5 += 1


print(f'x = 0 = {x0}\nx = 1 = {x1}\nx = 2 = {x2}\nx = 3 = {x3}\nx = 4 = {x4}\nx = 5 = {x5}')
print('-=' * 5)
print(f'y = 0 = {y0}\ny = 1 = {y1}\ny = 2 = {y2}\ny = 3 = {y3}\ny = 4 = {y4}\ny = 5 = {y5}')