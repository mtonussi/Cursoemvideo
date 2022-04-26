import math
ang = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('Para o ângulo informado, temos os valor de: ')
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tg))
