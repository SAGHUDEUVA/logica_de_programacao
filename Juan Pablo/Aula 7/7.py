# Clean code Aula 7
# Para que Usar?
# Como usar?
# print("Clean Code - Aula 7")
# aula = 7
# print(f"Estamos na aula {aula} de Clean code")

# def obter_saudacao_gamer(nick, nivel):
#     """
#     Formata a mensagem de perfil do jogador.
#     Princípio: Funções pequenas e com propósito único.
#     """
#     return f"O jogador {nick} está no nível {nivel} e pronto para a partida!"

# def main():
  
#     nick_jogador = input("Digite o nick do jogador: ")
#     nivel_jogador = input("Digite o nível atual: ")
    
  
#     mensagem = obter_saudacao_gamer(nick_jogador, nivel_jogador)
#     print(mensagem)

# if __name__ == "__main__":
#     main()




# print("Valor ganho semanal")
# valor_ganho = float(input("Qual é o valor ganho?"))
# total_mes = valor_ganho *4
# print(f"O valor total ganho esse mês foi {total_mes}")


# manipular_texto = "python é Muito legal, porem...estressante"
# print(manipular_texto.strip().upper()) #"PYTHON"
# print(manipular_texto.strip().lower()) #"python"
# print(manipular_texto.strip().startswith("A")) #começar com letra inicial

# print(manipular_texto.strip().capitalize())
# print(manipular_texto.strip().title())
# print(manipular_texto.strip().replace(" ","_"))
# print(manipular_texto.strip().split())


# frase_usuario = input("Digite uma frase")
# print(frase_usuario.strip().lower())

#manipular arquivos:
#Escrevendo
# with open("notas.txt","w", encoding="utf-8") as texto:
#     texto.write("Estudar python hoje!")
#     texto.write("\nLer sobre clean code.")
#     texto.write("\n Estamos evoluindo.")

# with open("notas.txt","w", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON") # Contar a palavra "Python"
#     contagem = conteudo.lower().count("python")
#     print(f"A contagem de palavras {contagem} é de...")

import os 


os.mkdir("Pretinho Uva")



os.rename("Pretinho Uva", "Minha_Pasta")


# os.rmdir("Minha_Pasta")