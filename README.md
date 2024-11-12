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
SistemaDeGestão.py: Script principal que contém o código-fonte do projeto.<br>
dados.json: Arquivo onde os dados de consumo são salvos. Este arquivo é criado automaticamente ao inserir dados pela primeira vez.<br>

## Exemplo de Uso
Se o usuário inserir um consumo de 36 kWh diários para um determinado aparelho, o sistema calculará o consumo acumulado ao longo dos períodos, utilizando os dados armazenados no arquivo JSON para fornecer uma visão histórica e realista do consumo total.<br>

## Conclusão<br>
Concluindo, este projeto oferece uma solução prática e acessível para o monitoramento do consumo de energia residencial, utilizando Python e arquivos JSON para armazenamento persistente de dados. Com funcionalidades para calcular o consumo diário, semanal e mensal, ele permite que o usuário tenha uma visão detalhada e histórica do uso de energia. A partir desses registros, é possível identificar padrões de consumo e promover uma gestão energética mais eficiente. Com futuras melhorias, como a adição de uma interface gráfica e visualizações em gráficos, o projeto pode se tornar uma ferramenta ainda mais eficaz para quem deseja controlar e reduzir seus gastos com energia elétrica.

## Melhorias Futuras
Interface Gráfica: Adicionar uma interface gráfica para tornar o programa mais amigável.<br>
Visualização de Dados: Criar gráficos para uma visualização mais intuitiva do consumo energético.<br>
Alertas: Notificar o usuário quando o consumo ultrapassar uma meta pré-definida.<br>
