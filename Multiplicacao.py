print("Seja bem vindo ao calculator.")
nome = input("Como você se chama: ")
print("Seja bem vindo(a) ", nome)
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
print("Digite se a operação que você quer é Multiplicação ou Divisão: ")
resolucao = input("Digite M para multiplicação e D para Divisão: ")

if 'm' == resolucao.lower():
    multiplicacao = num1 * num2
    print("A multiplicação é {0}".format(multiplicacao))
elif 'd' == resolucao.lower():
    divisao = num1 / num2
    print("A Divisão é {0}".format(divisao))
