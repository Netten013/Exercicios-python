nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12: 
	print(nome,"Criança")
elif idade >=13 and idade <= 17:
	print(nome,"Adolescente")
elif idade >=18 and idade <= 59:
	print(nome,"Adulto")
elif idade >= 60:
	print(nome,"Velho")

	