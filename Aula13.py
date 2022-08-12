
'''
CONTAGEM REGRESSIVA

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOW!')
'''

'''
CONTAGEM DE PARES

for n in range(2, 51, 2):
    print(n, end=' ')
'''

'''
SOMA ÍMPARES MULTIPLOS DE 3

soma = 0
count = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        count = count + 1
print('A soma de todos os {} valores é {}'.format(count, soma))
'''

'''
TABUADA 2.0

num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
'''

'''
SOMA DOS PARES

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(('Digite o {} valor: '.format(c))))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voce informou {} números PARES e a soma foi {}'.format(cont, soma))
'''

'''
PROGRESSAO ARITMÉTICA

primeiro = int(input('Qual é o primeiro termo? '))
r = int(input('Qual é a razao? '))
decimo = primeiro + (10 - 1) * r
for c in range(primeiro, decimo, r):
    print('{}'.format(c), end=' -> ')
'''
'''
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('É por isso que ele é primo')
else:
    print('É por isso que ele nao é primo')
'''

'''
Detector de Palindromo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada nao é um palindromo')
'''

'''
Grupo da maioridade

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('No total tivemos {} pessoas maiores de idade.'.format(totalmaior))
print('No total tivemos {} pessoas menores de idade'.format(totalmenor))
'''

'''
Maior e menor da sequencia

maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {} pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
'''

'''
Analisador completo

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
'''
