
valor_total = float(input("Digite o valor total da conta: R$ "))

parte_maria = int(valor_total // 3)
parte_gabriel = parte_maria

parte_willian = round(valor_total - (parte_maria + parte_gabriel), 2)

print(f"Maria deve pagar: R$ {parte_maria:.2f}")
print(f"Gabriel deve pagar: R$ {parte_gabriel:.2f}")
print(f"Willian deve pagar: R$ {parte_willian:.2f}")
