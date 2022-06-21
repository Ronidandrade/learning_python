# Associar valores de listas
def associar(lista1, lista2):
    return list(zip(lista1, lista2))

# Definindo as listas
nomes = ['Jose', 'Joaquim', 'Pedro', 'Felipe']
notas = [10, 8, 5.5, 7]

# Intercalando as listas
boletim = list(zip(nomes, notas))

print('O boletim dos alunos:')
for nomeNota in boletim:
    print(f'    {nomeNota}')

# Melhor exibição
print('\nBoletim formatado:')
for nomeNota in boletim:
    print(
        '    {:<8} {:<4}'.format(nomeNota[0], nomeNota[1])
        )
