preco = float(input("Digite o preço do produto: R$ "))

print("\nEscolha a condição de pagamento:")
print("1 - À vista em dinheiro ou Pix (10% de desconto)")
print("2 - À vista no cartão de crédito (5% de desconto)")
print("3 - Em duas vezes (sem juros)")
print("4 - Em três vezes (com 10% de juros)")

codigo = int(input("Digite o código da condição de pagamento: "))

if codigo == 1:
    valor_final = preco * 0.90
    print(f"Valor a pagar com 10% de desconto: R$ {valor_final:.2f}")
elif codigo == 2:
    valor_final = preco * 0.95
    print(f"Valor a pagar com 5% de desconto: R$ {valor_final:.2f}")
elif codigo == 3:
    parcela = preco / 2
    print(f"Pagamento em 2x de R$ {parcela:.2f} (sem juros)")
elif codigo == 4:
    valor_final = preco * 1.10
    parcela = valor_final / 3
    print(f"Pagamento em 3x de R$ {parcela:.2f} (com juros)")
    print(f"Valor total com 10% de juros: R$ {valor_final:.2f}")
else:
    print("Código inválido. Tente novamente.")
