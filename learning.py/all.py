# Verifica se há valores nulos na lista ou tupla
def temNulos(lista):
    return not all(lista)

# Montando listas exemplo
l1 = [1,2,3,4]
l2 = (-1,0,5)

print(
    '\nTESTES',    
    f' {"Nome":<6} {"Valor":<20} {"Valores Nulos":^5}',
    ' ' + 41*'-',
    f' {"l1":<6} {str(l1):<20} {temNulos(l1)}',
    f' {"l2":<6} {str(l2):<20} {temNulos(l2)}',
    sep='\n'
    )
