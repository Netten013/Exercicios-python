numeros = []

print("Digite 20 números:")

for i in range(1, 21):
    numero = int(input(f"Numero {i}: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)

print(f"\nMenor número informado: {menor}")
print(f"Maior número informado: {maior}")
