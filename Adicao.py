print("Seja bem vindo ao calculator.")
nome = input("Como você se chama: ")
print("Seja bem vindo(a) ", nome)
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
print("Digite se a operação que você quer é Adição ou Subtração: ")
resolucao = input("Digite A para adição e S para Subtração: ")

if 'a' == resolucao.lower():
    soma = num1 + num2
    print("A soma é {0}".format(soma))
elif 's' == resolucao.lower():
    subtracao = num1 - num2
    print("A subtração é {0}".format(subtracao))
