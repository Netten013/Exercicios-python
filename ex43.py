moeda_1 = int(input("Quantidade de moedas de 1 centavo: "))
moeda_5 = int(input("Quantidade de moedas de 5 centavos: "))
moeda_10 = int(input("Quantidade de moedas de 10 centavos: "))
moeda_25 = int(input("Quantidade de moedas de 25 centavos: "))
moeda_50 = int(input("Quantidade de moedas de 50 centavos: "))
moeda_1real = int(input("Quantidade de moedas de 1 real: "))

total_reais = (
    moeda_1 * 0.01 +
    moeda_5 * 0.05 +
    moeda_10 * 0.10 +
    moeda_25 * 0.25 +
    moeda_50 * 0.50 +
    moeda_1real * 1.00
)

print(f"Valor total economizado: R$ {total_reais:.2f}")
