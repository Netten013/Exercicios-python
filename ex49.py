valor_dolar = float(input("Digite o valor em dólar (US$): "))

cotacao = float(input("Digite a cotação do dólar (R$): "))

valor_real = valor_dolar * cotacao

print(f"Valor convertido em reais: R$ {valor_real:.2f}")
