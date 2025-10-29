numero = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print(f"\n{numero}! = ", end="")
for i in range(numero, 0, -1):
    print(f"{i}", end="." if i > 1 else f" = {fatorial}")
