numeros = []

print("Digite 10 números reais:")
for i in range(1, 11):
    numero = float(input(f"Número {i}: "))
    numeros.append(numero)

print("\nNúmeros na ordem inversa:")
for num in reversed(numeros):
    print(num)
