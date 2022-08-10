'''
Empréstimo Bancário para casa

vcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos =int(input('Em quantos anos voce quer pagar o empréstimo? '))
meses = anos * 12
# parcelames tem q ser >=30% do salario ou será negado
parcelames = (vcasa / meses)
if parcelames > salario * (30 / 100):
    print('Seu empréstimo foi negado, o valor da sua parcela seria R${:.2f}, '
          'e a parcela máxima mensal disponível para voce é de R${:.2f}.'.format(parcelames, salario * (30 / 100)))
elif parcelames == salario * (30 / 100):
    print('Seu empréstimo foi aprovado, o valor da sua parcela será R${:.2f} e será pago em {:.0f} meses, '
          'essa é a maior parcela mensal disponível para o seu salário.'.format(parcelames, meses))
else:
    print('Seu empréstimo foi aprovado, o valor da sua parcela será R${:.2f} e será pago em {:.0f} meses'.format(
        parcelames, meses))
'''

'''
Conversor de bases numéricas

numero = int(input('Digite um número inteiro: '))
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opcao inválida. Tente novamente.')
'''

'''
Comparando números

n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha mais um número: '))
print('{} e {}'.format(n1,n2))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
#elif n1 == n2:
 #   print('Nao existe valor maior, os dois sao iguais.')
else:
    print('Nao existe valor maior, os dois sao iguais.')
'''

'''
Alistamento militar

from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? '))
alistamento = int(input('Voce já realizou o alistamento? Para SIM digite 1 e para NAO digite 2: '))
anoatual = date.today().year
idade = anoatual - nascimento
if alistamento == 2:
    if idade < 18:
        print('Voce ainda vai se alistar no exercito, faltam {} anos para o alistamento.'.format(18-idade))
    elif idade > 18:
        print('Já passou do tempo do alistamento, tempo em atraso {} anos.'.format(idade-18))
    else:
        print('Voce está na idade correta para se alistar')
else:
    print('Voce já realizou o alistamento militar.')
'''

'''
Média escolar com if, elif e else

n1 = float(input('Primeira avaliacao: '))
n2 = float(input('Segunda avaliacao: '))
media = (n1+n2)/2
print(media)
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERACAO')
else:
    print('APROVADO')
'''

'''
Categoria dos atletas

from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano do seu nascimento? '))
idade = atual-nascimento
if idade <= 9:
    print('Voce tem {} anos, sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Voce tem {} anos, sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Voce tem {} anos, sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos, sua categoria é SENIOR'.format(idade))
else:
    print('Voce tem {} anos, sua categoria é MASTER'.format(idade))
'''

'''
Analisando triangulos 2.0

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and b + c > a and c + a > b:
    print('Os segmentos {}, {} e {} podem formar um triangulo'.format(a,b,c))
    if a == b and b == c and a == c:
        print('Eles formam um triangulo EQUILATERO')
    elif a != b and b != c and a != c:
        print('Eles formam um triangulo ESCALENO')
    else:
        print('Eles formam um triangulo ISOSCELES')
else:
    print('Os segmentos {}, {} e {} nao podem formar um triangulo'.format(a,b,c))
'''

'''
IMC

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros:'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce está abaixo do peso')
elif imc <= 25:
    print('Voce está no peso ideal')
elif imc <= 30:
    print('Voce está com sobrepeso')
elif imc <= 40:
    print('Voce está obeso')
else:
    print('Voce está com obesidade mórbida')
'''

'''
Gerenciador de pagamentos

valorp = float(input('Qual o valor do produto? R$'))
print('O valor do produto é R${:.2f}'.format(valorp))
pagamento = int(input('''#Qual será o método de pagamento?
#A vista DINHEIRO/CHEQUE digite: 1
#A vista CARTAO digite: 2
#Em até 2x digite: 3
#Em 3x ou mais digite: 4
'''))
print(pagamento)
if pagamento == 1:
    print('O valor do produto é R${}'.format(valorp - (valorp * 10 / 100)))
elif pagamento == 2:
    print('O valor do produto é R${}'.format(valorp - (valorp * 5 / 100)))
elif pagamento == 3:
    print('O valor do produto é R${}'.format(valorp))
else:
    print('O valor do produto é R${}'.format(valorp + (valorp * 20 / 100)))
'''

'''
PEDRA X PAPEL X TESOURA

from time import sleep
from random import randint
itens = ['Pedra','Papel', 'Tesoura']
computador = randint(0, 2)
print('''#Suas opcoes:
#[ 0 ] PEDRA
#[ 1 ] PAPEL
#[ 2 ] TESOURA
''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=-' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=-' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        PRINT('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA.')
'''

