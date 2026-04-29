# exemplo 1
# for lote in range(1,6):
#     print(f"processando lote númerico {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("produção do dia finalizada!")


# exemplo 2
# for n in range(10):
#     print(f"Quantidade total {b} foi....")

# exemplo 3
# for vinil in range (1,21):
#     print(f"produção de {vinil}, diária")

# exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo" "Prego", "Chave de Fenda"]
# itempecas = ["cilindrica", "duplo", "cônica", "prego", "orelha", "redondo", "phillips", "Universal"]


# for item in pecas:
#     print(f"item em estoque: {item} e {itempecas}")

# exemplo 5 
# imagine a seguinte situação gostaria de ter um menu onde eu pudesee perguntar qual opção você deseja e a partir da seleção ele listar os produtos 

# produtos = {
#     '1': {'nome': 'Notebook', 'preco': 3500.00},
#     '2': {'nome': 'Smartphone', 'preco': 1500.00},
#     '3': {'nome': 'Tablet', 'preco': 800.00},
#     '4': {'nome': 'Headset', 'preco': 150.00}
# }

# def exibir_menu():
#     print("\n" + "="*30)
#     print("      MENU DE PRODUTOS")
#     print("="*30)
#     print("1. Notebook")
#     print("2. Smartphone")
#     print("3. Tablet")
#     print("4. Fone de Ouvido")
#     print("0. Sair")
#     print("="*30)

# def listar_produtos():
#     while True:
#         exibir_menu()
#         opcao = input("Qual opção você deseja? (1-4, ou 0 para sair): ")

#         if opcao == '0':
#             print("Encerrando o sistema. Até logo!")
#             break
        
       
#         if opcao in produtos:
#             produto = produtos[opcao]
#             print(f"\n[SELECIONADO] Produto: {produto['nome']} - R${produto['preco']:.2f}")
#         else:
#             print("\n[ERRO] Opção inválida! Tente novamente.")


# if __name__ == "__main__":
#     listar_produtos()
