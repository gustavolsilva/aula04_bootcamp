from typing import Dict, Optional

produto_01: Dict[str, int, float, bool]


import json

lista: list = ["Sapato", 39, 10.38, True] # O que é isso?

produto_01: dict = {
    "nome": "Sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "Televisao",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)

#Json é o "dicionário do Java Script"