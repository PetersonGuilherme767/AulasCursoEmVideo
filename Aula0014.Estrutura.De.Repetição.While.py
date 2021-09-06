
# O programa vai parar só quando o usuário gititar 0
n = 1
while n != 0:
    n = int(input('Digite um valor:'))
print('Fim')

# Digitando 'S' o usuário continua...
r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')


# Quantos números pares e impar o usuário digitou até digitar o 0

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números Pares e {} números Impar'.format(par, impar))