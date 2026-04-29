#print = "função de saida de dados para o console"
#input = "função de entrada de dados do usuario via teclado"
#if = "estrutura de decisão para executar código condicionalmente"
#    elif = "Combinação de else + if para verificar múçtiplas condições"
    #  else = "para opcional de umif que executa código quando a condição do if é falsa"
# for = "laço de repetição para iterar sobre uma sequência de elementos"
# while = "laço de repetição para executar um codigo enquanto a condição for verdadeira"

# Exemplo 1
# nome = input ("Digite sue nome: ")
# print(f"olá, {nome}! Bem Vindo á aula de python para Desenvolvimento de Sistemas!")

# Exemplo 2

# nota = float (input("Digite a nota do aluno: "))
# if nota >= 7:
#     print("Aluno aprovado!")
# elif nota >= 5:
#     print("Aluno em recuperação")
# else:
#     print("Aluno reprovado")

# Exemplo 3

# materiais = ["metal","plastico","vidro"]
# for material in materiais:
#     print(f"Processando material: {material}.")
#     print(f"material {material} processando com sucesso!")
# print("Fim do processamento de materiais.")

# 2. o laço while (Repetiçoes Indeterminadas)
# use quando você você não sabe quando vai parar. ele depende de uma condição (como um sensor de segurança ou um botão de emergência) 
# Exemplo: monitor de temperatura (loop Infinito controlado)
# Repete enquanto a temperatura estiver segura
# import time
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura} °C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 # Simulando o aquecimento da maquina
# print("ALERTA! temperatura atingiu o limite. Desligando motor...")


# listas de temperaturas lidas pelo sensor por minuto
# leituras=[70, 75, 82, 98, 110, 85, 80]
# for tem in leituras:
#     while temp > 100:
#         print(f"CRÍTICO; {temp}°C detectado! Acionando a parada de emergência.")
#         break # O loop para aqui e NÃO lê os proximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")
# print("Sistema desligado. Aguardando manutenção.")

# Produção de peças com controle de material usando continue
materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso: peça de {peca} detectada. Desviando para descarte...")
        continue #Pula o restante do código abaixo e vai para a próxima peça
#Este codigo só roda se a peça for 
print(f"Processando peça de {peca}. Furando e polindo...")
print("Fim do lote de produção.")