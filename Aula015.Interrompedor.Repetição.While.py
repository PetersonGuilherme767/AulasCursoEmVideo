cont = 1
while cont <= 10:
    print(cont, end=' ')
    cont += 1
print('Acabou')

#while Treu:
'''executa o programa para sempre'''

#comando Break
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
#O comando vai parar e não vai somar o valor 999.

#F string ex:
print(f'A soma vale {s}')
ou
nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos.')








