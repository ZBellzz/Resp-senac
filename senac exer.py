import math

# Atividade 1 exercicio 1
#Escreva um algoritmo que calcule a área de um retângulo. Para isso, defina as variáveis base e altura como números inteiros e use um operador aritmético para calcular a área.


#base = int(input("Digite a base "))
#altura = int(input("Digite a altura"))

#r = base * altura 

#print("a area deve ser {}".format(r))

#Atividade 1 exercicio 2

#Crie um algoritmo que converta uma temperatura dada em graus Celsius para Fahrenheit. Utilize uma variável do tipo real para armazenar a temperatura e constantes para os valores fixos da fórmula de conversão.

#tc = float(input("Digite a temperatura em Celsius"))
#c1 = 1.8
#c2 = 32


#tf = tc * c1 + c2

#print("a temperatura em celsius foi de {}convertida em fh {}".format(tc, tf))


#Atividade 1 exercicio 3

#Desenvolva um algoritmo que calcule a média aritmética de três notas. Use variáveis do tipo real para armazenar as notas e o resultado da média.

#nota2 = float(input("Digite o valor das 2 notas"))
#nota3 = float(input("Digite o valor das 3 notas"))


#media = (nota1 + nota2 + nota3) /3


#print("a media das notas {} {} {} resultou na media de {}".format(nota1, nota2, nota3, media))


#Atividade 1 exercicio 4

#Escreva um algoritmo que receba um número inteiro e calcule o dobro e a metade desse número. Use operadores aritméticos e variáveis para armazenar os resultados.

#print("Selecione a operação desejada sendo * para o dobro e / para metade")

#operacao = input("selecione a operação")
#nm = int(input("Digite o numero"))


#if operacao == "*":
    #r = nm * 2
    #print("o dobro é: {}".format(r))


#if operacao == "/":
    #r = nm /2
    #print("a metade é: {}".format())

#atividade 1 exercicio 5
#valor_original = float(input("digite o valor a ser descontado"))
#desconto = valor_original / 10
#valor_final = valor_original - desconto

#print("O valor original do produto sendo {}, foi aplicado o desconto de 10% resultando: {}".format(valor_original, valor_final))


#atividade 2 exercicio 1

#print("Hello, World!")

#atividade 2 exercicio 2

#nome = input("digite o seu nome")

#print("Olá {}, é um prazer te conhecer! ".format(nome))

#nome = input("Digite o seu nome")
#wsalario = input("digite o seu salario")

#print("O(a) Funcionario(a) {} tem um salario de R$:{} nesse mês".format(nome, salario))


#atividade 2 exercicio 4

#nm = int(input("digite o valor "))
#ante = nm - 1
#suc = nm + 1

#print("o seu numero {} tem de antecessor {} e sendo o seu sucessor {}".format(nm, ante, suc))


#atividade 2 exercicio 5 
#real = float(input("digite o valor em reais a quantia que queira converter"))
#cotacao = 5.60
#dolar = real / cotacao

#
# print("o valor convertido da cotação de real para dolar é: {}".format(dolar))

#atividade 2 exercicio 6

#altura = float(input("digite o valor da altura"))
#base = float(input("digite o valor da base"))
#lata = base * altura / 2

#print("a quantidade de latas necessarias para a pintura da parede deve ser de  {}".format(lata))

#atividade 3 exercicio 1

#lado = float(input("digite o valor de um dos lados do quadrado"))
#peri = lado * 4

#print("o perimetro do quadrado q deseja calcular é de : {}".format(peri))


#atividade 3 exercicio 2

#km = float(input("digite o valor em quilometros para ser convertido em metros"))
#metros = km * 1000


#print("a quilometagem convertida em metros e a de {}".format(metros))


#ativiadage 3 exercicio 3

#valor_inicial = float(input("digite o valor inicial para ser aplicado o desconto : "))
#por = float(input("digite a porcentagem para ser aplicada"))
#desconto = valor_inicial * por /100
#valor_final = valor_inicial - desconto


#print("o valor do produto oferecido é de R${}, O desconto aplicado em % é de :{}%, então o desconto foi de R$:{}, sendo o valor final de R$:{}".format(valor_inicial, por, desconto,valor_final))


#atividade 3 exercicio 4


#peso1 = int(input("De o valor do peso1:  "))
#peso2 = int(input("De o valor do peso2:  "))
#peso3 = int(input("De o valor do peso3:  "))
#nota1 = float(input("De a primeira nota: "))
#nota2 = float(input("De a segunda nota:  "))
#nota3 = float(input("De a terceira nota: "))
#media_a = peso1 * nota1 + peso2 * nota2 + peso3 * nota3
#media_b = peso1 + peso2 + peso3 
#media_p = media_a / media_b

#print("o pesos da notas sendo os seguintes {}, {}, {}, e as notas sendo {}, {},{}, teve como resultado a media ponderada de{}".format(peso1,peso2,peso3,nota1,nota2,nota3,media_p))

#desafio 1

'''
nm1 = float(input("digite o valor "))
nm2 = float(input("insira o valor "))
print("Escolha a condição, + soma, - subtrção, * multiplicação, / divisao")

condicao = input("escolha + - * /: ")

if condicao == "+":
    r = nm1 + nm2
    print("a soma é de: {}".format(r))

if condicao == "-":
    r = nm1 - nm2 
    print("a subtração é: {}".format(r))

if condicao == "*":
    for c range(nm1 +1):
        nm1 + 1

    print ("A multiplcação resultou em: {}".format(r))

if condicao == "/":
    r = nm1 / nm2 
    print("o resultado da divisão é: {}".format(r))'''


""" desafio 2  """
""" 
v1 = int(input("Valor 1: "))

if v1 % 2 == 0:
    print("ERRO: número par")
else:
    v2 = int(input("Valor 2: "))

    if v2 % 2 == 0:
        print("ERRO: número par")
    else:
        r = v1 + v2
        print("O valor é de {}".format(r))
     """

""" desafio 1  """



n1 = int(input("Digite o primeiro valor"))
n2 = int(input("Digite o segundo valor"))
operacao = input("Digite um operador")
c = 0
pre = 0


if operacao == "+":
    r = n1 + n2
    print("O resultado é {}".format(r))


elif operacao == "-":
    r = n1 - n2
    print("O resultado é {}".format(r))


elif operacao == "*":
    c != n2
    
        pre = n1 + pre
        c + 1
        print(pre)






