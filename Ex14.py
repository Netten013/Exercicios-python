conta = input("Número da conta: ")
saldo = float(input("Saldo: "))
debito = float(input("Débito: "))
credito = float(input("Crédito: "))

saldo_atual = saldo - debito + credito

print(f"Saldo atual: R$ {saldo_atual:.2f}")

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
