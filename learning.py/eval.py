# Converter um valor diretamente do input
idade = eval(input('\n> Digite sua idade: '))
altura = eval(input('> Digite sua altura: '))

print(
    '\nTESTES',
    f'A altura digitada foi {altura} e seu tipo é {type(altura)}',
    f'A idade digitada foi {idade} e seu tipo é {type(idade)}',
    sep='\n'
    )
