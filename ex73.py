candidatos = {
    1: "Bruno",
    2: "João",
    3: "Rafaela",
    4: "Ahmed"     
}

votos = {1: 0, 2: 0, 3: 0, 4: 0}
nulos = 0
brancos = 0
total_votos = 0

print("Digite os votos (1 a 4 para candidatos, 5 para nulo, 6 para branco, 0 para encerrar):")

while True:
    voto = int(input("Código do voto: "))
    if voto == 0:
        break
    elif voto in votos:
        votos[voto] += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Código inválido. Tente novamente.")
        continue
    total_votos += 1

print("\n===== RESULTADOS DA ELEIÇÃO =====")
for codigo, nome in candidatos.items():
    print(f"{nome}: {votos[codigo]} voto(s)")

print(f"\nVotos nulos: {nulos}")
print(f"Votos em branco: {brancos}")

if total_votos > 0:
    perc_nulos = (nulos / total_votos) * 100
    perc_brancos = (brancos / total_votos) * 100
    print(f"\nPercentual de votos nulos: {perc_nulos:.2f}%")
    print(f"Percentual de votos em branco: {perc_brancos:.2f}%")
else:
    print("\nNenhum voto foi registrado.")
