'''frase = "Cabeça orelha corpo olhos nariz boca labios"
      print (frase)
      print (frase)
      print (frase)
      print (frase)'''
'''palavra_1 = "Hello"
palavra_2 = "World"
frase = palavra_1 + palavra_2
print(frase)
frase = frase + "bom dia flor do dia"
print (frase)'''
'''frase = input("Escreva uma palavra: ")
print(frase)
frase = frase + input("Diga outra palavra: ")
print (frase)'''
a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))

'''Serve para identificar o tipo da variavel'''
'''print (type(b))
Serve para fazer textos "bonitos"
print(f"A soma é {a+b}")'''

'''Serve para diferenciar números de maior menor, maleavel a resposta'''
'''O f antes do texto identifica as variaveis no texto printado'''
'''print(f"A operação {a} > {b} resulta em {a>b}")
print(f"A operação {a} < {b} resulta em {a<b}")
print(f"A operação {a} + {b} resulta em {a+b}")
print(f"A operação {a} * {b} resulta em {a*b}")
print(f"A operação {a} == {b} resulta em {a==b}")'''
'''O "and"  retorna a constante lógica True quando ambos os operandos forem verdadeiros'''
c = int(input("Digite outro numero: "))
d = int(input("Digite um ultimo numero:"))

print(f"A operação {a} != {b} é {c} == {d}, ou seja {a!=b} é {c==d}, da {a!=b and c==d}")

'''o "OR" retorna verdadeiro quando pelo menos um dos operandos for verdadeiro'''
print(f"A operação {a} > {b} é {c} < {d}, ou seja {a>b} é {c<d}, da {a>b or c<d}")

'''If serve para verificar uma condição e executar um bloco de código se ela for verdadeira'''
if a<b or c>d:
    print("Boa gorila")

'''**PARTE 2**'''

idade = int(input("Digite a sua idade: "))
'''é uma estrutura condicional que permite executar um bloco de código se uma condição for verdadeira'''
if idade >= 18:
    print(f"Aoobaa 🍻🍻🍻🍻🍻")
else:
     print("Perdeu perdeu 👮‍♂️👮‍♂️👮‍♂️👮‍♂️")
'''else é usada para executar um bloco de código quando a condição do if é falsa'''

idoso= input("Vocé e idoso MACACO?????")
cartaozinho = input("vOCE TEM O CARTÃOZINHO MANO??????????")
if idoso == 'sim' and cartaozinho == 'sim':
    print("Estaciona ae parsa ❤️❤️❤️❤️")
else:
    print("Folgado pra caralho filha da puta🖕🖕🖕🖕🖕")

    idoso = input("Voce e idoso?????")
    deficiente = input ("Vocé e deficiente???")
    if idoso == 'sim' or deficiente == 'sim':
        print("JOIA LIXO HUMANO 🥶🥶🥵🥵🥵🥵🥶🥶🤪🤪🤪")
    else:
        print("SAI CARALHO 👺💀💀💀👻👻👻👻")

'''**PARTE 3**'''

letra = input("Escreva uma letra: ")
if letra in 'aeiouAEIOU':
    print("A sua letra e uma vogal")
else:
    print("A sua letra e uma consoante")

    '''O "in" serve para verificar se um valor está presente em uma sequência'''

time = input("Diga seu time: ")
if time == "São paulo":
    print("O maior do brasil,trimundial")
elif time == "Corinthians":
    print("Tem serie B, 2005 foi roubado, eu gosto de cheirar craque")
elif time == "Palmeiras":
    print("Sem mundial, bi rebaixado, 2 serie B")
elif time == "Santos":
    print("Baixa taxa de natalidade, lixo de time")
'''Elif serve para economizar tempo No Python, a instrução elif é usada para verificar condições adicionais após a instrução if. Elif é uma abreviação de "else if". '''

'''**PARTE4**'''

salario = int(input("Digite o seu salario: "))
conta1 = salario - salario * 7.5/100
conta2 = salario - salario * 15/100
conta3 = salario - salario * 22.5/100
conta4 = salario - salario * 27.5/100
if salario <= 1904:
    print(f"Voce vai receber 100% do seu salario totalizando {salario}")
elif salario <= 2826:
    print(f"Seu salario tem uma taxa de 7,5%, vc tera um desconto de {salario * 7.5/100} recebendo {conta1}")
elif salario <= 3751:
    print(f"Seu salario tem uma taxa de 15%, vc tera um desconto de {salario * 15/100} recebendo {conta2}")
elif salario <= 4664:
    print(f"Seu salario tem uma taxa de 22.5%, vc tera um desconto de {salario * 22.5/100} recebendo {conta3}")
elif salario > 4664:
    print(f"Seu salario tem uma taxa de 27.5%, vc tera um desconto de {salario * 27.5/100} recebendo {conta4}")