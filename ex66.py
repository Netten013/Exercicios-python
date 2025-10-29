populacao_a = 80000
populacao_b = 200000

taxa_a = 0.03  # 3%
taxa_b = 0.015  # 1.5%

anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")
print(f"População final de A: {int(populacao_a)} habitantes")
print(f"População final de B: {int(populacao_b)} habitantes")
