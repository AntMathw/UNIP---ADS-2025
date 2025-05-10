#Estrutura para saber qual número é maior

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print('O primero valor é maior')
else:                                #Se caso o primeiro bloco não for True, o Else e executado
    print('O segundo valor é maior')


#Estrutura para saber se tem idade para votar
from datetime import date

ano = int(input('Digite o ano de nascimento'))
hoje = date.today().year
sub = hoje - ano           #Utilizando a biblioteca date, para saber o ano atual e subtrair com o ano de nascimento

if sub > 16:
  print('Ela tem idade para votar')
else:
  print('Ainda não possui a idade necessária')

#Estrutura das notas

nota = 75 
 
if nota >= 90: 
    print("Nota A") 
elif nota >= 80: 
    print("Nota B") 
elif nota >= 70:        #Como a nota é 70, ele executara esse bloco da estrutura
    print("Nota C") 
else: 
    print("Nota D")

#Estrutura se a pesso tem CNH

idade = int(input('Digite sua idade: '))
cnh = True

if idade >= 18:
    if cnh:
        print('Tem idade e possui CNH')
    else:
        print('Não dirigi sem a carteira')
else:
    print('Não tem carteira por ser menor de idade')
    
#Empréstimo para comprar uma casa de acordo com salário do funcionário

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Salário do comprador?  '))
ano = int(input('Quantos anos ele vai pagar? '))
emprestimo = casa / (ano * 12)
pmensal = emprestimo * 100 / salario
print('Para pagar uma casa de R${} em {:.0f} anos, a prestação será de R${:.2f}'.format(casa, ano, emprestimo, pmensal))

if emprestimo <= 0.30 * salario:
    print('\033[1;32mEmpréstimo CONCEDIDO!\033[m ')
elif emprestimo > 0.30 * salario:
    print('\033[1;31mEmpréstimo NEGADO!\033[m ')

#Conversor de número para hexadecimal, octal e binário

numero = int(input('Digite um número para ser convertido: '))
escolhido = int(input('Escolha uma conversão: \n[ 1 ]CONVERSOR NÚMERO BINARIO \n[ 2 ]CONVERSOR NÚMERO OCTAL'
                     '\n[ 3 ]CONVERSOR NÚMERO HEXADECIMAL\nDigite aqui: '))
if escolhido == 1:
    print(int(input('A conversão do número {} para binário é {}'.format(numero, bin(numero)[2:]))))
elif escolhido == 2:
    print(int(input('A conversão do numero {} para octal é {}'.format(numero, oct(numero)[2:]))))
elif escolhido == 3:
    print(int(input('A conversão do número {} para hexadecimal é {}'.format(numero, hex(numero)[2:]))))

#Analisar se a pessoa pode se alistar no exército

from datetime import date

nascimento = int(input('Em que ano você nasceu? '))
hoje = date.today().year

if nascimento == hoje:
    print('O ano de {}, você obrigatoriamente tem que se alistar! '.format(date.today().year))
elif hoje - nascimento > 18:
    print('O ano de {}, alistamento ja ocorreu, mas se não se alistou, FAÇA!'.format(nascimento + 18))
else:
    print('O seu alistamento ainda não chegou. Ele vai acontecer em {}'.format(nascimento + 18))

#Média de uma prova

prova1 = float(input('Nota da primeia prova: '))
prova2 = float(input('Nota da segunda prova: '))
resultado = (prova1 + prova2) / 2

if resultado >= 7:
    print('A nota {} e {}, a média do aluno vai ser {}\n\033[1;36mAPROVADO\033[m'.format(prova1, prova2, resultado))
elif resultado < 5.0:
    print('A nota {} e {}, a média do aluno vai ser {}\n\033[1;31mREPROVADO\033[m'.format(prova1, prova2, resultado))
elif resultado == 5.9 or 6.9:
    print('A nota {} e {}, a média do aluno vai ser {}\nRECUPERAÇÃO'.format(prova1, prova2, (resultado)))

#Júnior, Pleno e Sênior

from datetime import date

idade = int(input('Digite sua idade ou ano de nascimento: '))
anoatual = date.today().year
subtrai = anoatual - idade

if idade <= 9 or subtrai <= 9:
    print('Categoria será MIRIM.')
elif idade <= 14 or subtrai <= 14:
    print('Cateoria será INFANTIL.')
elif idade <= 19 or subtrai <= 19:
    print('Categoria será JÚNIOR.')
elif idade <= 25 or subtrai <= 25:
    print('Categoria será SÊNIOR.')
elif idade > 25:
    print('Categoria será MASTER.')

#Equilátero, Isósceles e Escaleno

r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
    print('Seu triangulo pode se um ISOSCELES, possui dois lados iguis mas um é diferente')
elif r1 == r2 == r3:
    print('Seu triangulo pode ser um EQUILATERO, possui todos lados iguais')
elif r1 != r2 != r3 and r2 != r1 != r3 and r3 != r1 != r2:
    print('Seu triangulo pode ser um ESCALENO, possui todos lados diferentes')

#Cálculo de IMC de uma pessoa

peso = float(input('Qual é seu peso? '))
altura = float(input('Qual sua altura? '))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print('Seu IMC {:.1f}, está abaixo do peso.'.format(IMC))
elif IMC == 18.5 or IMC < 25:
    print('Seu IMC {:.1f}, está no peso ideal.'.format(IMC))
elif IMC == 25 or IMC == 30:
    print('Seu IMC {:.1f}, está em sobrepeso'.format(IMC))
elif IMC > 30 or IMC < 40:
    print('Seu IMC {:.1f}, está em caso de OBESIDADE'.format(IMC))
elif IMC > 40:
    print('Seu IMC {:.1f}, está em caso de OBESIDADE MÓRBIDA'.format(IMC))

#Simulador de pagamento de uma loja

print('{:.^40}'.format(' Lojas Sousa '))
preco = float(input('Digite o preço do produto: '))
forma = int(input('Escolha o método de pagamento:\n[ 1 ] - À vista. 5% de desconto.\n[ 2 ] - Em até 2x'
                   ' no cartão. Preço formal.\n[ 3 ] - 3x ou mais no cartão. 20% de juros.'
                   '\nDigite aqui: '))
if forma == 1:
    print('O valor do produto receberá 5% de desconto, totalizando: R${:.2f}'.format(preco * 0.95))
elif forma == 2:
    print('O valor do produto poderá ser parcelado em 2 vezes sem alteração no valor'
          ' ,totalizando: R${:.2f} e cada parcela custando: R${:.2f}'.format(preco, preco/2))
else:
    nvezes = int(input('Digite o número de parcelas (minímo: 3, máximo: 12): '))
    if nvezes < 3 or nvezes > 12:
        print('Tal número de meses \033[1;31mNÂO\033[m é permitido!')
    else:
        print('O valor do produto será parcelado em {} vezes, o preço total sofrerá juros de'
              ' 20%, fazendo com que cada parcela custe: R${:.2f}, \ne o total a ser pago: R${:.2f}'
              .format(nvezes, (preco / nvezes) * 1.2, preco * 1.2))

#Jogo de JOKENPÔ

from time import sleep
import random


jogador = int(input('SUAS OPÇÕES:\n[ 1 ]PEDRA\n[ 2 ]TESOURA\n[ 3 ]PAPEL\nQual sua jogada? '))
computador = random.randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 20)
print('O jogador escolheu {}'.format(jogador))
print('O computador escolheu {}'.format(computador))
print('-=-' * 20)

if computador == 1:
    if jogador == 2:
        print('Computador ganhou')
if jogador == 1:
    if computador == 3:
        print('Computador GANHOU')
if jogador == 2:
    if computador == 1:
        print('Computador GANHOU')
if jogador == 3:
    if computador == 2:
        print('Computador GANHOU')
if jogador == 1:
    if computador == 2:
        print('Jogador GANHOU')
if jogador == 3:
    if computador == 1:
        print('Jogador GANHOU')
if jogador == 2:
    if computador == 3:
        print('Jogador GANHOU')
else:

    if jogador == 2:
        if computador == 2:
            print('EMPATE')
    if jogador == 3:
        if computador == 3:
            print('EMPATE')


















