#Condições:
'''ex 1'''

nome = str(input('Qual é o seu nome?')).upper().strip()
if nome == 'GUSTAVO':
    print('Que nome lindo você tem!')
    print('Bom dia {}'.format(nome))
else:
    print('Seu nome é normal')
    print('Bom dia {}'.format(nome))

'''ex 2'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Parabéns, você foi aprovado!')
else:
    print('infelizmente você foi reprovado')



