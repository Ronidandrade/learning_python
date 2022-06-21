# Definindo uma função diretamente do input
definicao = input('\n> Qual a definição de sua função polinomial em x? ')

# Montando a função no Python
exec(f'def f(x): return {definicao}')

print(
    '\nTESTES',    
    f'A função definida foi "f(x) = {definicao}" e as avaliações são:',
    f'f(10) = {f(10)}',
    f'f(-1) = {f(-1)}',
    sep='\n'
    )
