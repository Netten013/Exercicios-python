contador_50 = 0

print("Digite os números inteiros (digite 0 para encerrar):")

while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    if numero == 50:
        contador_50 += 1

print(f"\nO número 50 foi digitado {contador_50} vezes.")
