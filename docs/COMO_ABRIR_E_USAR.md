# Como abrir e demonstrar o Insurance Intelligence

## Dashboard web
Abra a [demonstração publicada](https://1mperador027.github.io/insurance-intelligence/). Ela apresenta KPIs e gráficos sintéticos estáticos. Não há filtros operacionais nesta versão web.

## Power BI Desktop
1. Baixe o [pacote CSV](https://1mperador027.github.io/insurance-intelligence/data/insurance_intelligence_csv.zip).
2. Extraia o ZIP no computador.
3. No Power BI Desktop, selecione **Obter dados → Texto/CSV** e importe os arquivos da pasta `csv_powerbi`.
4. Configure os relacionamentos conforme [Arquitetura e modelo](ARQUITETURA_E_MODELO.md).
5. Crie as medidas copiando `power-bi/Medidas_DAX_PowerBI.txt`.
6. Salve o relatório como `Insurance_Intelligence.pbix` no seu computador.

## Transparência
A base é inteiramente sintética. Os indicadores e gráficos do dashboard web são demonstrativos; a análise detalhada deve ser construída no Power BI. A leitura inteligente usa regras determinísticas, não IA generativa. Não há integração com sistemas ou APIs externas. O arquivo PBIX não está incluído nesta versão.
