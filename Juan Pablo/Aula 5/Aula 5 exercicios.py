#Exercicio 1
#Tente criar um codigo que conte de 1 a 10, mas use o continue para não imprimir
# o numero 5 (simulando uma folha de sensor específica no item)
# for sensor in range(1,11):
#     if sensor == 5:
#         print(f"Sensor n°{sensor}com falha")
#     print(f"Sensor {sensor} sem falha")
#     continue
# print(" Fim! ;-;")

#Exercicio 2
#simule um semáforo com parada para cada cor. determine um tempo que 
# deseja para que quando mudar para tal cor ele represente uma pausa para cada cor. 
# Use o continue para pular a cor amarela 
# (simulando um semáforo com defeito que não acende a luz amarela)
import time

# Define os tempos de pausa para cada cor (em segundos)
tempo_verde = 5
tempo_amarelo = 2  # Este tempo não será utilizado, pois pularemos o amarelo
tempo_vermelho = 4

# Lista das cores do semáforo
# cores = ["VERDE", "AMARELO", "VERMELHO"]

# print("--- Iniciando Simulação do Semáforo (Defeituoso) ---")
# print("O amarelo foi pulado para simular o defeito.\n")

# # Loop infinito para simular o funcionamento contínuo
# while True:
#     for cor in cores:
#         # Usando 'continue' para pular a cor amarela
#         if cor == "AMARELO":
#             print(f"[{cor}] - Lâmpada queimada! Pulando para o próximo...")
#             continue
        
#         # Simula a cor Verde
#         if cor == "VERDE":
#             print(f"[{cor}] - Siga com responsabilidade. ({tempo_verde}s)")
#             time.sleep(tempo_verde)
            
#         # Simula a cor Vermelha
#         elif cor == "VERMELHO":
#             print(f"[{cor}] - PARE! ({tempo_vermelho}s)")
#             time.sleep(tempo_vermelho)
            
#     print("\n--- Ciclo Reiniciado ---\n")

#Exercicio 3 - Soma de cargas de Energia (for)
#Uma fabrica tem 5 máquinas. peça ao usuario (via input dentro do loop) 
# o consumo em kwh de cada uma das 5 máquinas. Ao final do loop,
# o programa deve exibir o consumo total da fábrica

# Inicializa a variável que guardará o total
# total_consumo = 0

# # Loop for para percorrer 5 máquinas (1 até 5)
# for i in range(1, 6):
#     # Pede o input do usuário dentro do loop
#     consumo = float(input(f"Digite o consumo em kWh da máquina {i}: "))
    
#     # Soma o consumo da máquina atual ao total
#     total_consumo += consumo

# # Exibe o resultado total após o término do loop
# print("-" * 30)
# print(f"O consumo total da fábrica é: {total_consumo} kWh")
# print("-" * 30)

#Exercicio 4 - identificador de peças defeituosas (for + if)
# percorra uma lista de medidas de peças:
# medidias = [50.1, 49.8, 52.0, 50.0, 48.5].
# o padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler  a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada"
# print("----Avaliação de peças----")
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]

# for medida in medidas:
#     if medida >= 50.0:
#         print(f"Medida {medida}: Aprovada")
#     else:
#         print(f"Medida {medida}: Rejeitada")
# print("----Fim da avaliação de peças----")

#Exercicio 5 - uma balança industrial está pesando um lote de 6 sacos de insumos.
#O peso ideal do saco é 50kg, mas o sistema aceita variações.
#crie um programa que peça ao usuario o peso de cada saco (via input dentro do loop)e,
#para cada um, informe se ele está "dentro do limite" (Entre 48kg e 52kg) ou 
#"Fora do limite". No final, exiba quantos sacos estão dentro do limite.
# Configuração inicial
total_sacos = 6
limite_inferior = 48.0
limite_superior = 52.0
sacos_dentro = 0

print(f"--- Sistema de Pesagem Industrial ({total_sacos} sacos) ---")
print(f"Peso ideal: 50kg (Limite: {limite_inferior}kg a {limite_superior}kg)\n")

# Loop para solicitar o peso de cada saco
for i in range(1, total_sacos + 1):
    peso = float(input(f"Digite o peso do saco {i} (kg): "))
    
    # Verifica se o peso está dentro do limite
    if limite_inferior <= peso <= limite_superior:
        print(f"-> Saco {i}: Dentro do limite ({peso}kg)")
        sacos_dentro += 1
    else:
        print(f"-> Saco {i}: FORA do limite ({peso}kg)")

# Resultado final
print("-" * 30)
print(f"Resumo: {sacos_dentro} de {total_sacos} sacos estão dentro do limite.")