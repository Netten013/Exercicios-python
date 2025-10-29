numeros = []

print("Digite 5 números inteiros:")
for i in range(1, 6):
    numero = int(input(f"Número {i}: "))
    numeros.append(numero)

print("\nNúmeros informados:")
for num in numeros:
    print(num)
