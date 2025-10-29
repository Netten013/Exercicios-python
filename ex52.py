quantidade = 0

print("Digite os números (digite -1 para encerrar):")

while True:
    numero = int(input("Número: "))
    if numero == -1:
        break
    quantidade += 1

print(f"\nQuantidade de números digitados: {quantidade}")
