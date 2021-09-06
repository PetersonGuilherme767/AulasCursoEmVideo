import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

#importando todos os modos

import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil (raiz)))

#math.ceil para arredondamento p/ cima


from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor (raiz)))

#Importando apenas modos a serem utilizados

#A clase random gera números aleatórios ex:

import random
num = random.randint(1, 10)
print(num)
import random
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))






