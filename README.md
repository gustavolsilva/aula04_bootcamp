# aula04_bootcamp
## Type hint, Tipos Complexos (Dicionários)
No python não precisamos tipar. É por inferencia, ou seja, ele em tempo de execução entende o tipo. Isso é chamado de Tipagem Dinâmica. <br>
*Type Hint:* É uma dica de Tipagem <br>

### Tipagem Forte e Tipagem Fraca
O Python tem uma tipagem forte. Logo, tentando fazer uma operação
```2 + "2"``` nos trará um erro, pois ele não conseguirá entender um int somando com uma str

Ao contrário do JavaScript, que você consegue fazer a junção deste tipo de valores
![Meme_JS](https://preview.redd.it/v65crolks8f01.png?width=640&crop=smart&auto=webp&s=39374c71d7272d7c0efd82fb6545849335546ee1)

E o Python também tem a *Tipagem Estática* <br>

Logo, o que temos que ter ciência, é que o Type Hint, não altera nada em relação ao tipo de Dados, é tão somente, uma dica sobre qual dado está naquela variável. <br>

Por falar em Hint, *Dica*: O Python é uma linguagem interpretada, logo, se você utilizar o comando no terminal ```python -i seuarquivo.py```, ele abre o modo interativo do python, pondendo até você fazer uma alteração nas variáveis, criando outras e realmente interagindo com o programa. Para sair, basta digitar ```exit()``` <br>

## Listas e Dicionários
Conseguimos atribuir conjuntos dos tipos primitivos. <br>
Exemplo: Quando vamos num site de e-commerce, e adicionamos os itens que queremos comprar é como uma List.

### Listas
São Objetos de Tipagem Complexa para armazenamento sequencial de dados de tipagem diversas.<br>
Em uma lista as ações como ```lista.append()```, para adicionar. ```lista.pop()```, para a retirada do último item adicionado e ```lista.remove(nomedoitem)``` que remove o item determinado da lista, são de comum uso.<br>

[Doc Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

### Dicionario
É uma estrutura em Chave: Valor. Isso é legal, pois podemos criar uma estrutura de dados que pode ser o meu produto.
```
produto: dict =
{
    "nome":"Sapato",
    "quantidade": 39,
    "preco": 10.38
    "disponibilidade": True
}
```