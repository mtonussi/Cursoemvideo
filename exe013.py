sal = float(input('Qual é o sálario do funcionário? R$'))
aum = float(input('Qual o aumento em porcentagem sem o símbolo? '))
nsal = sal + ((sal* aum)/100)
print('O novo sálario do funcionário é de R${:.2f}'. format(nsal))
