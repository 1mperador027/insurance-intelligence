# Arquitetura e modelo analítico

## Fluxo
Geração de dados sintéticos → validação → preparação e modelagem → visualização → interpretação dos indicadores.

## Camadas
1. **Dados:** pacote ZIP com tabelas CSV e dicionário, gerado de forma reproduzível por `scripts/generate_synthetic_data.py`.
2. **Preparação:** importação, tipagem, padronização e validação de integridade.
3. **Modelo:** dimensões de calendário, mês, equipe, produto e unidade; fatos de propostas, apólices, renovações e metas.
4. **Visualização:** dashboard web estático de demonstração e medidas DAX iniciais para estudo no Power BI.
5. **Interpretação:** comentários demonstrativos por regras determinísticas; não equivalem a IA generativa.

## Modelo dimensional sugerido
- `DimMes[AnoMes]` → `FatoPropostas[AnoMes]`
- `DimMes[AnoMes]` → `FatoApolices[AnoMes]`
- `DimMes[AnoMes]` → `FatoRenovacoes[AnoMes]`
- `DimMes[AnoMes]` → `Metas[AnoMes]`
- `DimProduto[ProdutoID]` → fatos e metas
- `DimEquipe[EquipeID]` → fatos correspondentes
- `DimUnidade[UnidadeID]` → fatos correspondentes

Configure relacionamentos 1:* com filtro em uma direção, da dimensão para a tabela fato. Verifique tipos de dados e cardinalidade após importar.

## Materiais e limites
- [Baixar pacote CSV](https://1mperador027.github.io/insurance-intelligence/data/insurance_intelligence_csv.zip).
- [Medidas DAX iniciais](../power-bi/Medidas_DAX_PowerBI.txt).
- Não há arquivo Excel (.xlsx) nem Power BI (.pbix) incluído no repositório nesta versão; o PBIX deve ser montado e salvo localmente no Power BI Desktop.

Todos os dados são fictícios. A modelagem é didática e exige validação antes de qualquer adaptação a um contexto real.
