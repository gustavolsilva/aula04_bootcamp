#%%
# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista: list = [1,2,3,4,5,6,7,8,9,10]

for num in lista:
    print(num**2)

# %%
# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista: list = ["Python", "Java", "C++", "JavaScript"]
print(f"A lista Atual é: {lista}")
item_remover = "C++"
lista.remove(item_remover)
print(f"O item {item_remover} foi removido da lista!")
item_adicionar = "Ruby"
lista.append(item_adicionar)
print(f"O item {item_adicionar} foi incluido na lista")
print(f"A lista final é: {lista}")

# %%
# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# from typing import Dict, Any

# livro: Dict[str, Any] = {
#     "Titulo": "Game of Thrones",
#     "Autor": "Estagiario",
#     "Ano": 2005
# }

# lista_de_elementos: list = livro.items()

# for elemento in lista_de_elementos:
#     print(elemento)


lista_de_livros_usando_dict: dict = {
    "livro_01": {"Titulo": "Game of Thrones", 
                 "Autor": "Estagiario",
                 "Ano": 2005},
    "livro_02": {"Titulo": "Game of Thrones 2",
                 "Autor": "Estagiario",
                 "Ano": 2007}
}

print(lista_de_livros_usando_dict["livro_01"]["Titulo"])

# %%
# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
palavra: str = "Aviao sem asa"

dicionario_letras: dict = {}

for char in palavra:
    if char in dicionario_letras:
        dicionario_letras[char] += 1
    else:
        dicionario_letras[char] = 1

for char, count in dicionario_letras.items():
    print(f"'{char}': {count}"
          )
    
# %%
# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compra: list = ["maçã", "banana", "cereja"]
preco_fruta: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total = 0

for fruta in lista_compra:
    if fruta in preco_fruta:
        preco_total+= preco_fruta[fruta]
    else:
        print(f"A fruta '{fruta}' não está no dicionario de preços")

print(f"Preço total da lista de compras: R${preco_total: .2f}")

# %%
# 6) Dada uma lista de emails, remover todos os duplicados.
emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos: list = list(set(emails))

print(emails_unicos)
# %%
# 7) Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades: list = [22, 15, 30, 17, 18]
idades_validas: list = [idade for idade in idades if idade >= 18]

print(idades_validas)

# %%
# 8) Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas: list = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

# %%
# 9) Dado um conjunto de números, calcular a média.
numeros: list = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Media: ", media)

# %%
# 10) Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores: list = [1,2,3,4,5,6,7,8,9,10]
pares: list = [valor for valor in valores if valor % 2 == 0]
impares: list = [valor for valor in valores if valor % 2 != 0]

print("Pares: ", pares)
print("Ímpares: ", impares)

# %%
# 11) Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos: list = [
    {"id": 1, "nome": "Teclado", "preco": 100},
    {"id": 2, "nome": "Mouse", "preco": 80},
    {"id": 3, "nome": "Monitor", "preco": 300}
]

for produto in produtos:
    if produto["id"] == 2:
        produto["preco"] = 90

print(produtos)

# %%
# 13) Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo: dict = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# %%
# 14) Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario: dict = {"a": 1, "b": 2, "c": 3}
chave = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves: ", chave)
print("Valores: ", valores)


# %%
# 15) Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto: str = "engenharia de dados"
frequencia: dict = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1 

print(frequencia)
