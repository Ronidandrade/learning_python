# Filtrando os pares de uma lista
def par(x):
    return x % 2 == 0

# Definindo a lista de numeros
numeros = list(range(10))

# Filtrando os pares
pares = list(filter(par, numeros))

print(
    '\nTESTES',    
    'Os pares da lista',
    f'    {numeros}',
    'são',
    f'    {pares}',
    sep='\n\n',
    end='\n\n'
    )
