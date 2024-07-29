import csv

path: str = "/home/gustavo/Projects/Python/aula04_bootcamp/exemplo.csv"

arq_csv: list = []

# With é o Gerenciador de contexto.
with open(file=path, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    # intera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        arq_csv.append(linha)

print(arq_csv)