### Felipe Men dos Santos 557571

# Monitor de Consumo de Energia Residencial<br>
Este projeto em Python é uma ferramenta para registrar e monitorar o consumo de energia elétrica de aparelhos domésticos, utilizando arquivos JSON para armazenar os dados de forma persistente. Ele permite que o usuário insira dados diários de consumo e visualize o consumo de energia diária, semanal e mensal.

## Funcionalidades<br>
<p>Inserção de Dados de Consumo: Permite adicionar informações sobre o consumo de um aparelho, incluindo nome do aparelho, horas de uso e consumo em watts.</p>

***Cálculo do Consumo Diário***: Exibe o consumo total de energia do dia atual.<br>
***Cálculo do Consumo Semanal***: Calcula o consumo total dos últimos 7 dias.<br>
***Cálculo do Consumo Mensal***: Calcula o consumo total dos últimos 30 dias.<br>
***Persistência de Dados***: Os dados são armazenados em um *arquivo JSON (dados.json)*, garantindo que o histórico de consumo seja preservado entre execuções do programa.
## Estrutura do Projeto<br>
SistemaDeGestão.py: Script principal que contém o código-fonte do projeto.
dados.json: Arquivo onde os dados de consumo são salvos. Este arquivo é criado automaticamente ao inserir dados pela primeira vez.

## Exemplo de Uso
Se o usuário inserir um consumo de 36 kWh diários para um determinado aparelho, o sistema calculará o consumo acumulado ao longo dos períodos, utilizando os dados armazenados no arquivo JSON para fornecer uma visão histórica e realista do consumo total.

Melhorias Futuras
Interface Gráfica: Adicionar uma interface gráfica para tornar o programa mais amigável.
Visualização de Dados: Criar gráficos para uma visualização mais intuitiva do consumo energético.
Alertas: Notificar o usuário quando o consumo ultrapassar uma meta pré-definida.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.
