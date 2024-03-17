#%%
'''
idade = 30 # variavel do tipo int
altura = 1.75 # variavel do tipo float
nome = "Alice" # variavel do tipo str
is_estudante = True # variavel do tipo bool
# No python não precisamos tipar. É por inferencia.
# Ou seja, ele em tempo de execução entende o tipo.
# Tipagem Dinâmica.

# Logo usando o type hint, o código fica
'''
idade: int = 30 
altura: float = 1.75 
nome: str = "Alice"
is_estudante: bool = True

# A partir da versão 3.5
#%%
2 + "2"
#%%
idade = input("Digite sua idade: ")
print(type(idade))
# <class 'str'>

#%%
# O Type Hint não exime de você fazer o cast e validação de instancia 
idade: int = int(input("Digite sua idade: "))
if isinstance(idade, int):
    pass
print(type(idade))
# <class 'int'>
#%%
produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []
produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)

#%%
produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []
produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

# Se quero retirar o último produto que entrou
produtos.pop()

print(produtos)

#%%
numeros = []
numeros.extend(range(0,5))
print(numeros)

#%%
# Numa lista, vc tem a estrutura meio que desorganziada, 
# não sabendo do que se trata o item colocado
import json

lista: list = ["Sapato", 39, 10.38, True]

produto_01: dict = {
    "nome": "Sapato",
    "quantidade":39,
    "preco": 10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "Televisão",
    "quantidade":10,
    "preco": 70.38,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)

carrinho_json: json = json.dumps(carrinho)
print(carrinho_json)