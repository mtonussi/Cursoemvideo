val = float(input('Digite o valor do produto: R$'))
desc = float(input('Digite o valor do desconto em porcentagem sem o %: '))
va = val - ((val*desc) / 100)
print('O valor do produto com desconto de {}% é de: R${:.2f}'.format(desc,va))

