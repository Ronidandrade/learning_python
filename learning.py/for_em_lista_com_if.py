# Montar uma lista com os cubos de um range
# para os numéros maiores que 5
cubos = [x**3 for x in range(10) if x > 5]

print(
    "\nTESTES",
    f"A lista do cubo dos numeros do range maiores que 5: {cubos}",
    sep='\n'
    )
