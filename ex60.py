numero = int(input("Digite um número entre 1 e 10 para ver sua tabuada: "))

if 1 <= numero <= 10:
    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 10.")
