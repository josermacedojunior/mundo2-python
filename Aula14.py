'''validacao de dados
sexo = str(input('Informe seu sexo no formato: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informacao errada, por favor, digite seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
'''
import math

'''
Jogo da adivinhacao 2.0

palpite = 1
from random import randint
numero = int(input('Digite um numero entre 0 e 10: '))
computador = randint(0, 10)
while numero != computador:
    numero = int(input('Voce errou, tente outra vez: '))
    palpite += 1
print('Voce acertou, foram necessarios {} palpites.'.format(palpite))
'''
'''
MENU DE OPCOES COM IF
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('{} e {} sao os valores que voce escolheu.'.format(n1, n2))
opcao = int(input('''#Escolha uma opcao:
#[1] SOMA
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
'''))
if opcao==1:
    print('{} + {} = {}'.format(n1, n2, (n1 + n2)))
elif opcao == 2:
    print('{} * {} = {}'.format(n1, n2, (n1 * n2)))
elif opcao == 3:
    lista = [n1, n2]
    print('O maior valor é {}'.format(max(lista)))
elif opcao == 4:
    n1 =int(input('Escolha um novo número: '))
    n2 =int(input('Selecione um outro número: '))
    print('Seus novos números sao: {} e {}'.format(n1, n2))
else:
    print('Saindo do programa.')
'''
'''MENU DE OPCOES COM WHILE
from time import sleep
n1 = int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))
print('{} e {} sao os valores que voce escolheu.'.format(n1, n2))
opcao = 0
while opcao != 5:
    opcao = int(input('''#Escolha uma opcao:
#[1] SOMA
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
'''))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
        print('{} * {} = {}'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        lista = [n1, n2]
        print('O maior valor é {}'.format(max(lista)))
    elif opcao == 4:
        n1 = int(input('Escolha um novo número: '))
        n2 = int(input('Selecione um outro número: '))
        print('Seus novos números sao: {} e {}'.format(n1, n2))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
print('Fim do programa.')
'''
'''
CÁLCULO DE FATORIAL COM MATH.FACTORIAL

from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
count = 1
while count <= numero:
    count += numero
    resultado = math.factorial(numero)

print('{}! = {}'.format(numero, resultado))
'''
'''
CÁLCULO DE FATORIAL COM WHILE
numero = int(input('Escolha um número para calcular seu fatorial: '))
count = numero
f = 1
while count > 0:
    print('{} '.format(count), end='')
    print('X ' if count > 1 else '= ', end='')
    f *= count
    count -= 1
print('{}'.format(f))
'''
'''
 GERADOR DE PA COM WHILE
print('Gerador de PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = n1
count = 1
while count <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    count += 1
print('FIM')
print('-=-' * 10)
'''
'''
PROGRESSAO ARITMÉTICA MELHORADA

print('Gerador de PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = n1
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print('Progressao finalizada com {} termos'.format(total))
print('-=-' * 10)
'''
'''
SEQUENCIA DE FIBONACCI

print('-=-' * 30)
termo = int(input('Quantos termos voce quer mostrar? '))
soma = termo
count = 3
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
while count <= termo:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('-> FIM')
print('~' * 30)
'''
'''
TRATANDO VALORES MAIORES SOLUCAO 1
n = 0
soma = 0
count = 0
while n != 999:
    n = int(input('Digite um número [999 PARA PARAR]: '))
    if n == 999:
        soma = soma + n - 999
    else:
        count += 1
        soma = soma + n
print('Voce digitou {} números e a soma deles é {}'.format(count, soma), end='')
'''
'''
TRATANDO VALORES MAIORES SOLUCAO 2

numero = 0
count = 0
soma = 0
numero = int(input('Digite um número [999 PARA PARAR]: '))
while numero != 999:
    soma += numero
    count += 1
    numero = int(input('Digite um número [999 PARA PARAR]: '))
print('Voce digitou {} números e a soma entre eles foi: {}'.format(count, soma))
'''
'''
MAIOR E MENOR COM WHILE

resp = 'S'
media = soma = quantidade = maior = menor = 0
while resp in 'Ss':
    n1 = int(input('Digite um número: '))
    soma += n1
    quantidade += 1
    if quantidade == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resp = str(input('Voce quer continuar>?[S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Voce digitou {} números e a média entre eles é de {}.'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
'''