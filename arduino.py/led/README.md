~~~python
# O OBJETIVO DESSE PROGRAMA É FAZER O LED CONECTADO AO ARDUÍNO UNO ACENDER E APAGAR POR UM TEMPO INDETERMINADO. OBSERVAÇÂO: EVITE USAR A PORTA '13 DIGITAL PWM', POIS PODE HAVER CONFUSÃO ENTRE AS 'PISCADAS' PROGRAMADAS E AS 'PISCADAS' QUE ELA FAZ AO CARREGAR UM NOVO PROGRAMA.

# IMPORTANDO O MÓDULO DE COMUNICAÇÃO E CONVERSÃO PARA O ARDUÍNO.
from pyfirmata import Arduino, util

# IMPORTANDO OUTROS MÓDULOS.
import time

# Nessa linha cria a variável 'uno' para fazer a conexão com o Arduíno, entre parentes fica a porta USB que está conectado o arduíno uno.
uno = Arduino('COM5')

# Comando que fará o programa repetir as ações pra sempre.
while True:

	# Esse comando faz a porta '12 Digital PWM' do arduino ligar(emitir energia) e printar na tela do Python a mensagem LED LIGADO.
    uno.digital[12].write(1)
    print('LED LIGADO')

	# Esse comando faz o python esperar 0.5 segundos antes de executar o pŕoximo comando.
    time.sleep(0.5)

	# Esse comando faz a porta '12 Digital PWM' do arduino desligar(parar de emitir energia) e printar na tela do Python a mensagem LED DESLIGADO.
    uno.digital[12].write(0)
    print('LED DESLIGADO')

	# Esse comando faz o python esperar 1 segundos antes de executar o pŕoximo comando.
    time.sleep(1)
~~~
