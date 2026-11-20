# Insurance Intelligence
### Inteligência Comercial e Gestão Estratégica de Seguros

> **Projeto independente, educacional e experimental.** Desenvolvido para aprendizagem e demonstração de conceitos de Business Intelligence, análise de dados e aplicações de IA no mercado de seguros.

O projeto simula uma operação de seguros com dados inteiramente fictícios para explorar indicadores comerciais, desempenho de equipes, conversão de propostas, gestão de apólices e renovações.

## Demonstração e materiais
- **[Abrir dashboard interativo](https://1mperador027.github.io/insurance-intelligence/)** — filtros por competência, produto, equipe e unidade.
- **[Baixar base CSV para Power BI](https://1mperador027.github.io/insurance-intelligence/data/insurance_intelligence_csv.zip)** — pacote gerado e validado automaticamente durante a publicação.
- **[Baixar planilha analítica Excel](https://1mperador027.github.io/insurance-intelligence/data/Insurance_Intelligence_Base_Analitica.xlsx)** — visão executiva e tabelas estruturadas.
- **[Baixar relatório de portfólio PDF](https://1mperador027.github.io/insurance-intelligence/docs/Projeto_Insurance_Intelligence_Portfolio.pdf)**.
- [Arquitetura e modelo](docs/ARQUITETURA_E_MODELO.md).
- [Medidas DAX](power-bi/Medidas_DAX_PowerBI.txt).
- [Texto sugerido para LinkedIn](docs/TEXTO_LINKEDIN.md).

## Base analítica
O fluxo de publicação gera um pacote reproduzível com 1.500 propostas, 779 apólices, 420 eventos de renovação, dimensões de calendário, mês, produto, equipe e unidade, metas mensais e dicionário de dados. O script de geração está em `scripts/generate_synthetic_data.py`.

## Tecnologias
CSV, Excel, Power BI (estrutura preparada), DAX, modelagem dimensional, HTML, JavaScript e Business Intelligence.

## Premissas e transparência
- Todos os registros, nomes, unidades, equipes, valores e resultados são **fictícios e sintéticos**.
- Sem dados reais de clientes, colaboradores, instituições ou operações.
- Sem vínculo institucional, patrocínio, endosso ou integração com o Itaú ou qualquer outra instituição financeira.
- Sem conexão com sistemas corporativos, APIs privadas ou bases externas.
- O dashboard possui filtros funcionais alimentados pela base sintética. A leitura inteligente usa regras fixas; não há IA generativa integrada.
- Esta versão ainda não inclui arquivo Power BI (.pbix), backend, autenticação ou integração operacional.

**Insurance Intelligence — projeto independente de aprendizagem.**
