larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
ar = larg * alt
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, ar))
tin = ar / 2
print('Para pintar sua parede, será necessário {}l de tinta'.format(tin))

