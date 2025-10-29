while True:
    nome = input("\nDigite o nome do atleta (ou pressione Enter para encerrar): ")
    if nome == "":
        break

    saltos = []
    for i in range(1, 6):
        distancia = float(input(f"{i}º salto: "))
        saltos.append(distancia)

    print(f"\nAtleta: {nome}")
    print(f"Primeiro Salto: {saltos[0]} m")
    print(f"Segundo Salto: {saltos[1]} m")
    print(f"Terceiro Salto: {saltos[2]} m")
    print(f"Quarto Salto: {saltos[3]} m")
    print(f"Quinto Salto: {saltos[4]} m")

    melhor = max(saltos)
    pior = min(saltos)

    saltos.remove(melhor)
    saltos.remove(pior)

    media = sum(saltos) / len(saltos)

    print(f"\nMelhor salto: {melhor} m")
    print(f"Pior salto: {pior} m")
    print(f"Média dos demais saltos: {media:.1f} m")
