'''co = float(input('Qual o comprimento do catato oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa deve medir {}'.format(hip))'''

import math
co = float(input('Qual o comprimento do catato oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hip = math.hypot(co,ca)
print('A hipotenusa deve medir {:.2f}'.format(hip))

