"""
listas são mutáveis
tuplas são imutáveis
"""

# imprimindo um array de numeros
lista01 = [0, 1, 2, 3, 4]
print(lista01)

lista02 = [5, 6, 7, 8]
print(lista02)

# concatenando listas
lista = lista01 + lista02
print(lista)

# pegando parte de uma lista
parte_da_lista = lista[2:9]
print(parte_da_lista)

# lista mix
mix = ["Helder", 1, 6.3, [1, 4, 5, "Santos"]]
print(mix)

# usando append
mix.append("Martins")
print(mix)

# a funcao remove, remove o primeiro valor da lista
lista01.remove(0)
print(lista01)

# a funcao del, deleta pelo número do índice
del (lista[7])
print(lista)