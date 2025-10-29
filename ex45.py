nascimento = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))

idade_anos = atual - nascimento

idade_meses = idade_anos * 12
idade_dias = idade_anos * 365  
idade_semanas = idade_dias // 7

print(f"\nIdade em anos: {idade_anos} anos")
print(f"Idade em meses: {idade_meses} meses")
print(f"Idade em dias: {idade_dias} dias")
print(f"Idade em semanas: {idade_semanas} semanas")
