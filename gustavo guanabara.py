#int: inteiro
#float : real
#bool : True, False
# ** : potencia
# // Resultado da divisao
# () : parenteses sempre calculam primeiro
# % : resto da divisão




#nm1 = float (input("Digite um valor"))
#nm2 = float(input("Digite um valor"))

#r = nm1 + nm2

#print("a soma do {}com {} resulta em {}".format(nm1, nm2, r))

# desafio 5
#nm1 = int(input("digite o valor inteiro"))
#ant = nm1 -1 
#suc = nm1 + 1

#print("o Antecessor do numero q digitou é {} e seu numero sendo {} o seu sucessor vai ser {}".format(ant, nm1, suc))

# desafio 7

#nt1 = float(input("Digite o valor da nota do aluno"))
#nt2 = float(input("Digite 0 valor da nota do aluno"))

#r= (nt1 + nt2 )/2

#print("o resultado da media das 2 notas do aluno é {}".format(r))


# desafio 9

#nm = int(input("Digite o valor "))

#r = nm * 1, nm * 2, nm * 3, nm * 4, nm *5, nm * 6, nm * 7, nm * 8, nm * 9, nm * 10

#print(r)


#desafio 10

#calculdora


#nm1 = float(input("digite o valor "))
#nm2 = float(input("insira o valor "))
#print("Escolha a condição, + soma, - subtrção, * multiplicação, / divisao")

#condicao = input("escolha + - * /: ")

#if condicao == "+":
#    r = nm1 + nm2
#   print("a soma é de: {}".format(r))

#if condicao == "-":
#    r = nm1 - nm2 
#    print("a subtração é: {}".format(r))

#if condicao == "*":
#    r = nm1 * nm2 
#    print ("A multiplcação resultou em: {}".format(r))

#if condicao == "/":
#    r = nm1 / nm2 
#    print("o resultado da divisão é: {}".format(r))

'''
nm1 = int(input("Me diga um numero  "))
r = nm1 % 2

if r == 0:
    print("o numero é par")

else:
    print("o numero é impar")
'''
#desafio 28
'''
from random import randint

pc = randint (1,5)

us = int(input("Tente acertar o valor de 1 a 5 em que estou pensando  "))


if us == pc:
    print("voce acertou!!!!!!!")

else:
    print("voce errou!!!!!")
'''


#desafio 29
'''
velo = float(input("Digite a velocidade do carro  "))
if velo <= 80:
    print("Good boy")

else:
    m = (velo - 80) *7
    print("multinha claro cidadao de mal, presentin para pagar na loterica R$:{}".format(m))'''


# desaio 30
'''
nm = int(input("digite um valor  "))
r = nm % 2
if r ==0:
    print("par")

else:
    print("impar")'''

'''
nm1 = int(input("digiite  pri "))
nm2 = int(input("digite seg num "))
operacao =  input("digite o operador ")

if operacao == "+":
    r = nm1 + nm2
    print(r)
elif operacao == "-":
    r = nm1 - nm2 
    print(r)
elif operacao == "*":
    r = nm1 * nm2 
    print(r)
elif operacao == "/":
    r = nm1 / nm2 
    print(r)

else:
    print("n a nada q possamos fazer")'''


#for : para repetir 
# c variavel, para mostrar o resultado exiba o c
# in fds
#range a distancia(obs: sempre conta 1 a mais para terminar no numero q qr)
# para pular numero poem , na frente do range, para ir de tras pra frente alem de inverter poem ,-1
# 

#for c in range(0,7, 2):
#    print(c)

#print("fim")        

#from time import sleep
#for contagem in range(10, 0, -1):
#    sleep(1)
#    print(contagem)
#print("booooooooooooooooooooooooooom!!!!!!!!!!!!!!!!!!!!!!!!")
soma = 0
cont = 0
for contagem in range (6):
    nm = int(input("Digite um valor 6 vezes"))
    if nm %2 == 0:
        soma += nm
        cont = cont + 1
    print(soma)
    











