todos = []
pares = []
impares = []

print("Digite 20 números inteiros:")

for i in range(1, 21):
    numero = int(input(f"Número {i}: "))
    todos.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nVetor com todos os números:")
print(todos)

print("\nVetor com números pares:")
print(pares)

print("\nVetor com números ímpares:")
print(impares)
