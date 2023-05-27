# > Listas
# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9,9.7,8.2]

# Criando listas
lista = []
lista2 = list()
lista3 = [26,'Bianca',3.14156, False]
lista_de_listas = [10,[1,2,3]]

# Indexação e Slices (fatiamento)
lista = [10, 'Walisson',3.1415,True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) #Imprime o último elemento da lista


# Slices (Pedaços)
lista = [10,20,30,40,50,60,70,80,90]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2]) # Percorrer a lista pulando de 2 em 2

# > Iterações com o FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices 
print('Comprimento da lista',len(lista))

#Imprimir as posições da minha lista
for i in range(len(lista)):
    print(i)

#Imprimir o conteúdo da minha lista
for i in range(len(lista)):
    print(lista[i])

# Métodos de listas
lista = [1,3,12,8,2]
# append - insere elementos ao final da lista
print('Antes do append: ',lista)
lista.append(3)
print('Depois do append: ',lista)

#Insert - insere elementos na lista na posição informada
lista.insert(2,10) # Inserir o valor 10 no índice 2 da lista
print('Depois do insert: ',lista)

#Extend - Juntar 2 listas
lista2 = [1,2,3]
lista.extend(lista2) 
print('Depois do extend:', lista)

#pop - Remover um item da lista, passando o índice
lista.pop() # Remover o último item da lista
print('Depois do pop:', lista)
lista.pop(0) # Remover o primeiro item da lista
print('Depois do pop:', lista)

#remove - Passar o elemento que quero remover
lista.remove(3) # Remover o primeiro 3 que ele encontrar
print('Depois do remove:', lista)

#count - Contar quantas vezes um elemento aparece na lista
print('Quantidade de 2 na lista:', lista.count(2))

#index
print('Indice do elemento 12:',lista.index(12))

#sort - ordenar a lista em forma crescente
lista.sort
print(lista)
lista.sort(reverse=True)
print(lista)

#Funções para listas
#len
print(len(lista))
#sum
print(sum(lista))
#max
print(max(lista))
#min
print(min(lista))
