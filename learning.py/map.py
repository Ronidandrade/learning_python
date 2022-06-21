# Aplicando uma função matemática a todos os valores
# de uma lista
def cubo(x):
    return x**3

def exponencial(x, y):
    return x**y

# Definindo a lista de numeros
numeros = list(range(10))
expoentes = 10*[3] # Esteremos aplicando a exponenciação
                   # de todos os numeros por 3

# Calculando os cubos
cubos = list(map(cubo, numeros))
exponenciacoes = list(map(exponencial, numeros, expoentes))

print(
    '\nTESTES',
    'O cubo dos valores da lista',
    f'{numeros}',
    'é',
    f'{cubos}\n',
    'A exponenciação dos valores da lista',
    f'{numeros}',
    'por 3 é ',
    f'{exponenciacoes}',
    sep='\n',
    )
