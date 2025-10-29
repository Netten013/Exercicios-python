numero = int(input("Digite um número para ver sua tabuada: "))
print(f"\nTabuada de {numero}:")
i = 1
while i <= 10:
    print("{} x {} = {}".format(numero, i, numero * i))
    i += 1