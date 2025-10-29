codigos = []
veiculos = []
acidentes = []

for i in range(5):
    print(f"\nCidade {i+1}:")
    codigo = input("Código da cidade: ")
    num_veiculos = int(input("Número de veículos de passeio (1999): "))
    num_acidentes = int(input("Número de acidentes com vítimas (1999): "))
    
    codigos.append(codigo)
    veiculos.append(num_veiculos)
    acidentes.append(num_acidentes)

media_veiculos = sum(veiculos) / 5

maior_acidente = max(acidentes)
menor_acidente = min(acidentes)
cidade_maior = codigos[acidentes.index(maior_acidente)]
cidade_menor = codigos[acidentes.index(menor_acidente)]

acidentes_menor_2000 = [
    acidentes[i] for i in range(5) if veiculos[i] < 2000
]

if acidentes_menor_2000:
    media_acidentes_menor_2000 = sum(acidentes_menor_2000) / len(acidentes_menor_2000)
else:
    media_acidentes_menor_2000 = 0

print("\n===== RESULTADOS =====")
print(f"Média de veículos nas 5 cidades: {media_veiculos:.2f}")
print(f"Maior índice de acidentes: {maior_acidente} (Cidade: {cidade_maior})")
print(f"Menor índice de acidentes: {menor_acidente} (Cidade: {cidade_menor})")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menor_2000:.2f}")
