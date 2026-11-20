# Arquitetura e modelo analítico

## Fluxo conceitual
Dados sintéticos → validação e preparação → modelo analítico → visualização → interpretação dos indicadores.

## Camadas
1. **Dados:** tabelas CSV e planilha Excel com registros simulados.
2. **Preparação:** padronização, tipagem, relacionamento e validação de consistência.
3. **Modelo:** dimensões de calendário, mês, equipe, produto e unidade; fatos de propostas, apólices, renovações e metas.
4. **Visualização:** dashboard demonstrativo em HTML e estrutura de medidas DAX para estudo no Power BI.
5. **Interpretação:** comentários determinísticos baseados em regras; não equivalem a aconselhamento automatizado nem a IA generativa.

## Modelo dimensional
- DimCalendario / DimMes
- DimEquipe
- DimProduto
- DimUnidade
- FatoPropostas
- FatoApolices
- FatoRenovacoes
- Metas

## Premissas
Todos os dados são fictícios. A modelagem é didática e pode exigir ajustes de relacionamento, granularidade e tratamento antes de qualquer uso em ambiente produtivo.
