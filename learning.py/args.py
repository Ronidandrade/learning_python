# Definindo uma função que soma e outra que realiza
# o produto todos os números passados como parâmetro
def somaNumeros(*numeros):
    return sum(numeros)

def produtoNumeros(*numeros):
    produto = 1
    for num in numeros:
        produto *= num
    return produto

print(
    "\nTESTES",
    "Realizando as operações:",
    f"    10 + 5 - 1 + 50 - 20 = {somaNumeros(10, 5, -1, 50, -20)}",
    f"    10*5*-1*50*-20 = {produtoNumeros(10, 5, -1, 50, -20)}",
    sep='\n'
    )
