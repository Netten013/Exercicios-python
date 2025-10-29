medias = []
aprovados = 0

for i in range(1, 11):
    print(f"\nAluno {i}:")
    soma = 0
    for j in range(1, 5):
        nota = float(input(f"Nota {j}: "))
        soma += nota
    media = soma / 4
    medias.append(media)
    if media >= 7.0:
        aprovados += 1

print("\nMédias dos alunos:")
for i, media in enumerate(medias, start=1):
    print(f"Aluno {i}: Média = {media:.2f}")

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}")
