notas = []

print("Digite 4 notas:")
for i in range(1, 5):
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas informadas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

print(f"\nMédia das notas: {media:.2f}")
