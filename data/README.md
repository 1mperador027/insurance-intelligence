# Base de dados — Insurance Intelligence

**[Baixar pacote CSV para Power BI](insurance_intelligence_csv.zip)**

Base demonstrativa com dados inteiramente fictícios/sintéticos.

## Conteúdo
- `FatoPropostas`: 1.500 propostas.
- `FatoApolices`: 779 apólices.
- `FatoRenovacoes`: 420 eventos.
- Dimensões de calendário, mês, produto, equipe e unidade.
- Metas mensais por produto.
- Dicionário de dados.

## Integridade verificada
- Identificadores de propostas, apólices e renovações sem duplicidade.
- Todas as apólices referenciam uma proposta existente.
- Todas as renovações referenciam uma apólice existente.
- As 779 propostas com status `Emitida` correspondem às 779 apólices da base.

## Importação
Extraia o ZIP e importe os arquivos CSV no Power BI Desktop. Configure os relacionamentos conforme [a arquitetura do modelo](../docs/ARQUITETURA_E_MODELO.md) e utilize as [medidas DAX](../power-bi/Medidas_DAX_PowerBI.txt).

**Aviso:** os registros não representam clientes, operações, resultados ou dados de qualquer instituição financeira ou seguradora.
