numeros = []
soma = 0

print("Digite 5 números:")

for i in range(1, 6):
    numero = float(input(f"Número {i}: "))
    numeros.append(numero)
    soma += numero

media = soma / 5

print(f"\nSoma dos números: {soma}")
print(f"Média dos números: {media}")
