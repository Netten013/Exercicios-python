idades = []
alturas = []

print("Digite a idade e a altura de 5 pessoas:")
for i in range(1, 6):
    idade = int(input(f"Idade da pessoa {i}: "))
    altura = float(input(f"Altura da pessoa {i} (em metros): "))
    idades.append(idade)
    alturas.append(altura)

print("\nDados na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Pessoa {5 - i}: Idade = {idades[i]}, Altura = {alturas[i]:.2f} m")
