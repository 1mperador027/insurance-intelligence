# Como abrir e demonstrar o Insurance Intelligence

## Dashboard web
Abra a [demonstração publicada](https://1mperador027.github.io/insurance-intelligence/). Os filtros de competência, produto, equipe e unidade atualizam os KPIs e os gráficos a partir da base sintética.

## Arquivos para download
- [Planilha analítica Excel](../data/Insurance_Intelligence_Base_Analitica.xlsx).
- [Relatório de portfólio PDF](Projeto_Insurance_Intelligence_Portfolio.pdf).
- [Base CSV para Power BI](../data/insurance_intelligence_csv.zip).

## Power BI Desktop
1. Baixe o [pacote CSV](https://1mperador027.github.io/insurance-intelligence/data/insurance_intelligence_csv.zip).
2. Extraia o ZIP no computador.
3. No Power BI Desktop, selecione **Obter dados → Texto/CSV** e importe os arquivos da pasta `csv_powerbi`.
4. Configure os relacionamentos conforme [Arquitetura e modelo](ARQUITETURA_E_MODELO.md).
5. Crie as medidas copiando `power-bi/Medidas_DAX_PowerBI.txt`.
6. Salve o relatório como `Insurance_Intelligence.pbix` no seu computador.

## Transparência
A base é inteiramente sintética. O dashboard web é interativo, mas não substitui a análise detalhada no Power BI. A leitura inteligente usa regras determinísticas, não IA generativa. Não há integração com sistemas ou APIs externas. O arquivo PBIX não está incluído nesta versão.
