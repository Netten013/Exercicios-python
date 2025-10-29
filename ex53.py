quantidade_impares = 0

print("Digite os números (digite 999 para encerrar):")

while True:
    numero = int(input("Número: "))
    if numero == 999:
        break
    if numero % 2 != 0:
        quantidade_impares += 1

print(f"\nQuantidade de números ímpares digitados: {quantidade_impares}")
