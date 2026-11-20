# Como abrir e demonstrar o Insurance Intelligence

## Dashboard web
A versão completa do dashboard está prevista para a pasta `dashboard/`. O HTML original funciona localmente e contém dados sintéticos incorporados. Quando o arquivo for adicionado ao repositório, poderá ser publicado pelo GitHub Pages após a configuração correspondente.

## Power BI Desktop
1. Abra o Power BI Desktop.
2. Selecione Obter dados > Texto/CSV.
3. Importe os arquivos CSV da pasta `data/csv_powerbi`.
4. Configure os relacionamentos descritos em `ARQUITETURA_E_MODELO.md`.
5. Crie as medidas copiando `power-bi/Medidas_DAX_PowerBI.txt`.
6. Salve o relatório como `Insurance_Intelligence.pbix`.

## Transparência
Todos os dados são sintéticos. A seção “Leitura inteligente” do protótipo usa regras determinísticas, não IA generativa. Não há integração com sistemas ou APIs externas.
