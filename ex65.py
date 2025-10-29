valor_divida = float(input("Digite o valor da dívida: R$ "))

tabela_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

print("\n{:<20} {:<20} {:<25} {:<20}".format("Valor da Dívida", "Valor dos Juros", "Quantidade de Parcelas", "Valor da Parcela"))
print("-" * 85)

for parcelas, juros in tabela_juros.items():
    valor_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas
    print("R$ {:<17.2f} R$ {:<17.2f} {:<25} R$ {:<17.2f}".format(valor_total, valor_juros, parcelas, valor_parcela))
