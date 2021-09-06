#Escreva 'Olá' 5 vezes e escreva 'Fim' no final:
for c in range(0, 6):
    print('Olá')
print('Fim')
#Faça uma contagem de 1 até 6:
for c in range(1, 7):
    print(c)
#Faça uma contagem ao contrario de 6 até 0:
for c in range(6, 0, -1):
    print(c)
#Faça uma contagem de 0 até 6 pulando de 2 em 2:
for c in range(0, 7, 2):
    print(c)
#leia um número qualquer e faça uma contagem de 0 até ele:
n = int(input('Digite um Número:'))
for c in range(0, n):
    print(c)
'''Complete a sequeência até o número exato (0, n+1)'''
#Leia 3 números utilizando For:
for c in range(0, 3):
    n = int(input('Digite um valor:'))
print('fim')

#Faça a soma de 4 valores:
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
