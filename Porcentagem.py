print("Seja bem vindo ao calculator.")
nome = input("Como você se chama: ")
print("Seja bem vindo(a) ", nome)
valor_percentual = float(input("Digite o valor percentual: "))
valor_total = float(input("Digite o valor total: "))

porcentagem = (valor_total * valor_percentual) / 100
print(f'O resultado da porcentagem é de {porcentagem:,.2f}')