#Condições aninhadas

#ELIF

nome = str(input('Qual é o seu nome?'))
if nome == 'gustavo':
    print('Que nome lindo!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ana claudia jessica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))