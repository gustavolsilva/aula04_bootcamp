lista_de_numeros: list = [40,50,60,70,0,-408593,1,50]

# [40,50,60,0,-408593,1,50]
# [50,60,,700,-408593,1,50]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nove_lista_de_numeros = numeros.copy()
    for i in range(len(nove_lista_de_numeros)):
        for j in range(i+1,len(nove_lista_de_numeros)):
            if nove_lista_de_numeros[i] > nove_lista_de_numeros[j]:
                nove_lista_de_numeros[i], nove_lista_de_numeros[j] = nove_lista_de_numeros[j], nove_lista_de_numeros[i]
    return nove_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print(nova_lista)