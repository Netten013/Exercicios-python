nome = input("Digite o nome da pessoa: ").strip()
sexo = input("Digite o sexo (M/F): ").strip().upper()
estado_civil = input("Digite o estado civil: ").strip().upper()

if sexo == "F" and estado_civil == "CASADA":
    anos = int(input("Há quantos anos está casada? "))
    msg = f"{nome} está casada há {anos} anos."
else:
    msg = f"{nome} não se enquadra na condição de mulher casada."

print(msg)