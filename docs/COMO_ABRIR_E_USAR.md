# Como abrir e demonstrar o Insurance Intelligence

## Dashboard web
O dashboard HTML completo será colocado em `dashboard/`. O protótipo usa dados sintéticos incorporados e pode ser aberto em navegador moderno.

## Power BI Desktop
1. Abra o Power BI Desktop.
2. Selecione Obter dados > Texto/CSV.
3. Importe os arquivos de `data/csv_powerbi/`.
4. Configure os relacionamentos descritos em `ARQUITETURA_E_MODELO.md`.
5. Crie as medidas copiando `power-bi/Medidas_DAX_PowerBI.txt`.
6. Salve como `Insurance_Intelligence.pbix`.

## Transparência
Todos os dados são sintéticos. A leitura gerencial do protótipo usa regras determinísticas, não IA generativa. Não há integração com sistemas ou APIs externas.
