# Definindo uma função rapidamente
f = lambda x: x**2
g = lambda x,y: x**2 + y
meuDivmod = lambda a,b: (a//b, a%b)

# Fixando um parametro de função
meuDivmodPor2 = lambda a: meuDivmod(a, 2)

print(
    "\nTESTES",
    f'Aplicando a função "f" à lista {list(range(10))}:',
    f'    {list(map(f, range(10)))}\n',
    f'Aplicando a função "g" à lista {list(range(5,16))}:',
    f'    {list(map(f, range(5, 16)))}\n',
    'Aplicando a função "meuDivmod":',
    f'    meuDivmod(10,5) = {meuDivmod(10,5)}',
    f'    meuDivmod(6,4) = {meuDivmod(6,4)}',
    f'    meuDivmodPor2(10) = {meuDivmodPor2(10)}',
    f'    meuDivmodPor2(7) = {meuDivmodPor2(7)}',
    sep='\n'
    )
