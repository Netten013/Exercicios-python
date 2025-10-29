cardapio = {
    1: ("Bife acebolado", 15.00),
    2: ("Lasanha", 25.00),
    3: ("Frango grelhado", 18.50),
    4: ("Peixe ao molho", 22.00),
    5: ("Salada completa", 12.00),
    6: ("Macarronada", 20.00)
}

print("===== CARDÁPIO =====")
for codigo, (prato, preco) in cardapio.items():
    print(f"{codigo} - {prato} - R$ {preco:.2f}")

escolha = int(input("\nDigite o número do prato desejado: "))

if escolha in cardapio:
    prato_escolhido, preco = cardapio[escolha]
    print(f"\nVocê escolheu: {prato_escolhido} - R$ {preco:.2f}")
    
    gorjeta = input("Aceita pagar a gorjeta do garçom (10%)? (S/N): ").strip().upper()
    
    if gorjeta == "S":
        total = preco * 1.10
        print(f"Valor final com gorjeta: R$ {total:.2f}")
    else:
        print(f"Valor final sem gorjeta: R$ {preco:.2f}")
else:
    print("Opção inválida. Por favor, escolha um prato do cardápio.")
