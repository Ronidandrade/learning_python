# Somando os numeros não divisíveis por 5 entre 0 a 100
# até que se some mais que 50
soma = 0
for num in range(0, 101):
    if num%5 == 0:
        continue # Volte ao "for" e pegue o próximo "num"
                 # (Ignorando todo codigo abaixo)

    elif soma > 50:
        break # Pare e saia do "for"
              # (Ignorando todo codigo, dentro do "for", abaixo)

    else:
        pass # Não faça nada
             # (Siga o código abaixo)

    # Realizando a soma
    soma += num

print(
    "\nTESTES",
    f"O ultimo número do 'for' foi {num}",
    f"A soma terminou com {soma}",
    sep='\n'
    )
