soma = 0

print("Digite os números (digite -999 para encerrar):")

while True:
    numero = int(input("Número: "))
    if numero == -999:
        break
    soma += numero

print(f"\nA soma dos números digitados é: {soma}")
