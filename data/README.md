# Base de dados — Insurance Intelligence

**[Baixar pacote CSV para Power BI](https://1mperador027.github.io/insurance-intelligence/data/insurance_intelligence_csv.zip)**

O ZIP é gerado automaticamente no deploy pelo script `scripts/generate_synthetic_data.py`. A geração valida as contagens, unicidade dos identificadores e integridade das referências antes da publicação.

- FatoPropostas: 1.500 registros.
- FatoApolices: 779 registros.
- FatoRenovacoes: 420 eventos.
- Dimensões de calendário, mês, produto, equipe e unidade.
- Metas mensais por produto e dicionário de dados.

Extraia o ZIP e importe os CSVs no Power BI Desktop. Consulte [arquitetura do modelo](../docs/ARQUITETURA_E_MODELO.md) e [medidas DAX](../power-bi/Medidas_DAX_PowerBI.txt).

Todos os registros são fictícios e não representam clientes, operações, resultados ou dados de qualquer instituição financeira ou seguradora.
