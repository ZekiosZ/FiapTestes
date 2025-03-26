'''Exercicio Número 1'''
Numero1=int(input("Escreva um Número:"))
Numero2=int(input("Escreva outro Número:"))
if Numero1<Numero2:
    print(f"O Número {Numero2} e o Maior")
elif Numero1>Numero2:
    print(f"O Número {Numero1} e o Maior ")

'''Exercicio Número 2'''
print("Bem-vindo ao sistema governamental de verificação de idade")
idade=int(input("Quantos anos vôce tem?"))
if idade<16:
    print("Voce ainda não esta com idade suficiente para votar, volte quando tiver mais de 16 anos")
else:
    print("Voce tem idade suficiente para votar, Obrigado")

'''Exercicio Número 3'''
senha=int(input("Escreva a sua senha:"))
if senha==1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

'''Exercicio 4'''
maçavalor12=0.25
maçavalor11=0.30
compradas=int(input("Quantas maças vão ser compradas?"))
conta1=0.25*compradas
conta2=0.30*compradas
if compradas<12:
    print(f"Voce comprou {compradas} maças pelo valor de 0,30 cada totalizando {conta2} reais")
else:
    print(f"Voce comprou {compradas} maças pelo valor de 0,25 cada totalizando {conta1} reais")
'''Exercicio 5'''
a=int(input("Escreva um Número"))
b=int(input("Escreva outro Número"))
c=int(input("Escreva outro Número"))
if a>b:
    a=b
if a>c:
    a=c
if b>c:
    b=c
print("Os valores em ordem crescente ficam", a, b, c)

'''Exercicio 6'''
sexo=int(input("Qual e o seu sexo? digite 1 se for femenino e 2 se for masculino"))
altura=float(input("Qual a sua altura"))
Femenino= 62.1*altura-44.7
Masculino= 72.7*altura-58
if sexo==1:
    print(f"O seu peso ideal é {Femenino} kg")
else:
    print(f"O seu peso ideal e {Masculino} kg")

'''Exercicio 7 e 8'''
lados=int(input("Escreva o Número de lados do seu poligono regular:"))
if lados<3 or lados>5:
    print("Poligono não identificado")
medidas=float(input("Escreva as medidas dos lados do poligono em cm:"))
if lados==3:
    print(f"O seu poligono e um triangulo e tem um perimetro de {medidas*3} cm")
elif lados==4:
    print(f"O seu poligono e um Quadrado e tem um perimetro de {medidas*4} cm")
elif lados==5:
    print(f"O seu poligono e um Pentagono e tem um perimetro de {medidas*5} cm")

'''Exercicio 9'''
a=int(input("Escreva um Número"))
b=int(input("Escreva outro Número"))
c=int(input("Escreva outro Número"))
if a<b:
    a=b
if a<c:
    a=c
if b<c:
    a=c
    print("O maior Número e", a)

'''Exercicio 10'''
medida1=int(input("Escreva a medida do primeiro lado"))
medida2=int(input("Escreva a medida do segundo lado"))
medida3=int(input("Escreva a medida do terceiro lado"))
if medida1==medida2==medida3:
    print("O seu triangulo e Equilatero")
elif medida1==medida2!=medida3:
    print("O seu triangulo e Isosceles")
elif medida1!=medida2!=medida3:
    print("O seu triangulo e Escaleno")

'''Exercicio 11'''
medida1=int(input("Escreva o angulo do primeiro lado"))
if medida1>180:
    print("Valor invalido")
medida2=int(input("Escreva o angulo do segundo lado"))
if medida2>180:
    print("Valor invalido")
medida3=int(input("Escreva o angulo do terceiro lado"))
if medida1+medida2+medida3>180:
    print("Valores de angulo invalidos, um triangulo não pode ter angulos que somados são maiores a 180 graus")
elif medida3>180:
    print("Valor invalido")
elif medida1==90 or medida2==90 or medida3==90:
    print("O seu triangulo é um triangulo retangulo")
elif medida1>90 or medida2>90 or medida3>90:
    print("O seu triangulo é um Obtusangulo")
elif medida1<90 and medida2<90 and medida3<90:
    print("O seu triangulo e um Acutangulo")






