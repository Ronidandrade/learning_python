# Verificando se um número é maior que 5 ou não
def maiorQue5(numero):
    return (True if numero > 5 else False)

print(
    "\nTESTES",
    'Verificando se os numeros a seguir são maiores que 5:',
    f'4 {"" if maiorQue5(4) else "não "}é maior que 5',
    f'10 {"" if maiorQue5(10) else "não "}é maior que 5',
    f'-5 {"" if maiorQue5(-5) else "não "}é maior que 5',
    sep='\n'
    )
