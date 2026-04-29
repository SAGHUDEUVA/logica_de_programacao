# Foco: print, input, operações matemáticas e f-strings
# 1. Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
#  viagem!


# modelo = input("Digite o modelo do veículo: ")
# placa = input("Digite a placa do veículo: ")


# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# Questão 2
# Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
# cheio em python.
# Cálculo de Autonomia de Caminhão

# print("Cálculo de Autonomia")
# try:
#     capacidade_tanque = float(input("Digite a capacidade do tanque de combustível (em litros): "))
    
#     consumo_medio = float(input("Digite o consumo médio do caminhão (km/l): "))
    
#     autonomia = capacidade_tanque * consumo_medio
    
#     print("-" * 30)
#     print(f"Capacidade do tanque: {capacidade_tanque:.2f} litros")
#     print(f"Consumo médio: {consumo_medio:.2f} km/l")
#     print(f"A autonomia total do caminhão é: {autonomia:.2f} km")
#     print("-" * 30)

# except ValueError:
#     print("Por favor, digite valores numéricos válidos.")

# Exercicio 3
# 3. Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.
# Entrada do valor do frete em USD
# frete_usd = float(input("Digite o valor do frete em USD: "))
# taxa_conversao = 5.00

# frete_brl = frete_usd * taxa_conversao

# print(f"O valor do frete em BRL é: R$ {frete_brl:.2f}")

# Exercicio 4
# 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.

# rota1 = float(input("Digite o tempo da rota 1 (em horas): "))
# rota2 = float(input("Digite o tempo da rota 2 (em horas): "))
# rota3 = float(input("Digite o tempo da rota 3 (em horas): "))

# media = (rota1 + rota2 + rota3) / 3

# print(f"A média de tempo das entregas é: {media:.2f} horas")

# ================ ;-; ===================
# Exercicio 5
# Foco: if, elif, else e operadores lógicos

# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".
# Monitor de Carga de Caminhão

# try:
#     peso = float(input("Digite o peso atual do caminhão em toneladas (t): "))

    
#     if peso < 10:
        
#         print("Status: Carga Leve")
#     elif 10 <= peso <= 25:
        
#         print("Status: Carga padrão")
#     else:
        
#         print("ALERTA: Excesso de Peso!")

# except ValueError:
#     print("Por favor, digite um número válido para o peso.")

# Exercicio 6
# Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional"

# Solução Exercicio 6 - Classificador de Destino

# print ("======Qual o local desejado?======")
# codigo_carga = input("Digite o código da carga: ")


# if not codigo_carga:
#     print("Código inválido.")
# else:
#     primeira_letra = codigo_carga[0].upper()
   
#     if primeira_letra == 'N':
#         print("Região Norte")
#     elif primeira_letra == 'S':
#         print("Região Sul")
#     else:
#         print("Região Internacional")

# Exercicio 7
# Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# print("----Liberação de saida----")
# checklist = input("O check list está concluido?(sim/nao")
# motorista_identificado = input("motorista identificado? (sim/nao): ")

# if checklist == ("sim") and motorista_identificado == ("sim"):
#     print("veiculo AUTORISADO a iniciar rota.")
# else:
#     print("veiculo NÃO identificado. Verifique as pendências.")

# Exercicio 8
#  Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".
# Entrada de dados
# total_agendadas = int(input("Digite o total de entregas agendadas: "))
# total_atrasadas = int(input("Digite o total de entregas com atraso: "))

# indice_atraso = (total_atrasadas / total_agendadas) * 100


# if indice_atraso > 10:
#     print("Necessário Otimizar Rotas")
# else:
#     print("Logística Eficiente")

# Execicio 9
# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# medida = float(input("Digite a pressão do pneu em PSI: "))


# if 100 <= medida <= 110:                
#     print(f"A pressão {medida} PSI está dentro do padrão.")
# elif medida < 100:                      
#     print(f"A pressão {medida} PSI está abaixo do recomendado.")
# else:                                   
#     print(f"A pressão {medida} PSI está acima do recomendado.")

# ============;-;=============
# Exercicio 10
# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
# import time
# for i in range(5, 0, -1):
#     time.sleep(1)
#     print(f"Portão fecha em {i}")
# print("Portão Trancado!")

# Exercicio 11
# Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

faturamento_total = 0.0

print("--- Sistema de Somatório de Fretes ---")
print("Digite os valores dos fretes (digite 0 para encerrar):")

while True:
    
    valor_frete = float(input("Digite o valor do frete: R$ "))
    
    
    if valor_frete == 0:
        break
    
    
    faturamento_total += valor_frete


print("-" * 30)
print(f"Faturamento total acumulado: R$ {faturamento_total:}")

# Exercicio 12
# Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada em python.
# maior_km = 0

# for i in range(5):
#     km = float(input(f"Digite a quilometragem do veículo {i+1}: "))
    
#     if km > maior_km:
#         maior_km = km

# print(f"A maior quilometragem registrada foi: {maior_km} km")

