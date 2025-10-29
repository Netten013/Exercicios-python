qnt_n = int(input("Quantos números você deseja informar? "))

numeros = []

for i in range(qnt_n):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
