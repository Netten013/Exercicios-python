latas_350ml = int(input("Quantidade de latas de 350ml: "))
garrafas_600ml = int(input("Quantidade de garrafas de 600ml: "))
garrafas_2l = int(input("Quantidade de garrafas de 2 litros: "))

total_litros = (latas_350ml * 0.35) + (garrafas_600ml * 0.6) + (garrafas_2l * 2)

print(f"Total de refrigerante comprado: {total_litros:.2f} litros")