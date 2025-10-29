caracteres = []
consoantes = []

vogais = ['a', 'e', 'i', 'o', 'u']

print("Digite 10 caracteres (letras):")
for i in range(1, 11):
    letra = input(f"Caractere {i}: ").lower()
    caracteres.append(letra)
    if letra.isalpha() and letra not in vogais:
        consoantes.append(letra)

print(f"\nQuantidade de consoantes lidas: {len(consoantes)}")
print("Consoantes digitadas:")
for c in consoantes:
    print(c)
