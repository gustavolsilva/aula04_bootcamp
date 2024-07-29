# Aula 4 - Typing, listas e dicionários

## 1. Type Hint

Python não precisa tipar. É por inferencia, ou seja, em tempo de execução, ele entende os tipos de dados nas variáveis.
Logo estamos falando de...

### Tipagem Dinâmica vs. Tipagem estática
* *Tipagem Estática:* Java e C++. Como exigencia cada variável precisa declarar explicitamente no momento da compilação.

* *Tipagem Estática:* Python. Como colocamos acima, os tipos são inferidos em tempo de execução e não precisam ser declarados explicitamente. Vantagens: Flexibilidade e rapidez no desenvolvimento, mas pode aumentar o risco de erros de tipo que só serão detectados em tempo de execução.

Type Hint é uma boa prática. E foi implementada do Python 3.5 e acima através do PEP 484.

### Tipagem Forte vs Tipagem Fraca
* *Tipagem Forte:* No Python, que tem esse tipo de tipagem, mma variável após a atribuição de a um tipo, não pode ser automaticamente tratada como outro tipo sem uma conversão explícita. Logo, se variáveis de tipos diferentes tentarem fazer operações tomará um erro

```
2 + "2" # Erro de tipos diferentes, um int com uma str
```
* *Tipagem Fraca:* Um exemplo é o Javascript que tem maior flexibilidade de operações e fazendo conversões implícitas. E geram operações que são até comparadas com memes famosos na Internet.<br>

![meme](image.png) <br>

Em resumo, Type Hint, nada mais é que uma dica para auxiliar os demais desenvolvedores.

## 2. Listas e Dicionários

### Importância na Engenharia de Dados

Listas e dicionários são estruturas de dados versáteis que permitem armazenar e manipular coleções de dados de forma eficiente. Na engenharia de dados, essas estruturas são fundamentais para organizar dados coletados de diversas fontes, facilitando operações como filtragem, busca, agregação e transformação de dados.


Listas: https://docs.python.org/3/tutorial/datastructures.html#

### Lista
Conjunto de elementos

### Dicionario
Chave : Valor
Dicionario: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## 3. Lendo Arquivos
No módulo nativo do Python existe uma maneira para ler arquivos .csv. Através da combinação de '''with open ''' é possível essa ação


## 4. Funções
Muito importante em Pyhton, pois com Funções é possível modularizar e reutilizar códigos. Assim facilita o processamento e analise de grandes conjuntos de dados. Em Engenharia, usamos para encapsular lógicas de transformação, limpeza, agregação e analise de dados. Com isso, mantemos código organizado e qualificado.

Funções são abstrações. Tornam o código mais legível. Também pode ser conhecido como um míni-programa.

