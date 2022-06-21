# Verifica se o iterável (string, lista ou tupla) possui
# elementos ou não
def vazio(iteravel):
    return not any(iteravel)

# Montando listas exemplo
i1 = []
i2 = ''
i3 = tuple()
i4 = 's'

print(
    '\nTESTES',    
    f' {"Nome":<6} {"Valor":<20} {"Vazio":^5}',
    ' ' + 41*'-',
    f' {"i1":<6} {str(i1):<20} {vazio(i1)}',
    f' {"i2":<6} {str(i2):<20} {vazio(i2)}',
    f' {"i3":<6} {str(i3):<20} {vazio(i3)}',
    f' {"i4":<6} {str(i4):<20} {vazio(i4)}',
    sep='\n'
    )
