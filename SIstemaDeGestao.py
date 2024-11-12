import json
from datetime import datetime, timedelta

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open("dados.json", "r") as dados:
            return json.load(dados)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Função para atualizar os dados de consumo no arquivo JSON
def atualizar_dados(data, aparelho, horas_uso, consumo):
    dados = carregar_dados()

    # Verifica se a data já está registrada; se não, cria uma entrada para ela
    if data not in dados:
        dados[data] = {"consumo": []}

    # Adiciona o registro de consumo para o aparelho nesta data
    dados[data]["consumo"].append({
        "aparelho": aparelho,
        "horas_uso": horas_uso,
        "consumo": consumo
    })

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=2)

# Função para calcular o consumo total de uma data específica
def consumo_diario(data):
    dados = carregar_dados()
    consumo_total = 0

    # Se a data existir nos dados, soma o consumo de todos os aparelhos naquele dia
    if data in dados:
        for item in dados[data]["consumo"]:
            consumo_total += item["consumo"]

    return consumo_total

# Função para calcular o consumo dos últimos 7 dias
def consumo_semanal():
    hoje = datetime.now()
    data_atual = hoje.strftime("%d-%m-%Y")
    consumo_total = consumo_diario(data_atual)
    consumo_total *= 7
    return consumo_total

# Função para calcular o consumo dos últimos 30 dias
def consumo_mensal():
    hoje = datetime.now()
    data_atual = hoje.strftime("%d-%m-%Y")
    consumo_total = consumo_diario(data_atual)
    consumo_total *= 30
    return consumo_total

# Função principal com o menu para o usuário
def main():
    while True:
        try:
            menu = int(input("""
1 - Inserir Dados de Consumo
2 - Ver Consumo Diário
3 - Ver Consumo Semanal
4 - Ver Consumo Mensal
5 - Sair
Escolha uma opção: """))
        except ValueError as mensagem:
            print(f"Ocorreu um ERRO inesperado: {mensagem}")
        else:
            match menu:
                case 1:
                    try:
                        data = datetime.now().strftime("%d-%m-%Y")
                        aparelho = input("Digite o NOME do aparelho que deseja inserir: ")
                        horas_uso = int(input("Digite quantas HORAS o aparelho ficou ligado: "))
                        consumo = float(input("Digite o CONSUMO em Watt: "))
                        kwh = (consumo * horas_uso) / 1000  # Conversão para kWh
                    except ValueError as mensagem:
                        print(f"Ocorreu um ERRO inesperado: {mensagem}")
                    else:
                        atualizar_dados(data, aparelho, horas_uso, kwh)
                        print("Dados inseridos com sucesso!")
                case 2:
                    data = datetime.now().strftime("%d-%m-%Y")
                    print(f"Consumo diário de hoje ({data}): {consumo_diario(data)} kWh")
                case 3:
                    print(f"Consumo semanal: {consumo_semanal()} kWh")
                case 4:
                    print(f"Consumo mensal: {consumo_mensal()} kWh")
                case 5:
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")


main()
