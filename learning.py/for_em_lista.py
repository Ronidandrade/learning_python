# Montar uma lista com os cubos de um range
cubos = [x**3 for x in range(10)]

# Fazendo uma cópia da lista cubos
cubosCopia = cubos.copy()

# Remover os 5 ultimos elementos da lista cubos
removidos = [cubosCopia.pop() for cont in range(5)] # A variável "cont"
                                                    # só será usada
                                                    # internamente pelo
                                                    # python para conta-
                                                    # bilizar as remoções
                                                    
print(
    "\nTESTES",
    f"A lista de cubos original: {cubos}",
    f"A lista de cubos após a remocao: {cubosCopia}",
    f"A lista dos removidos: {removidos}",
    sep='\n'
    )
