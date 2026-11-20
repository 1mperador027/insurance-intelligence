# Insurance Intelligence
### Inteligência Comercial e Gestão Estratégica de Seguros

> **Projeto independente, educacional e experimental.** Desenvolvido para aprendizagem e demonstração de conceitos de Business Intelligence, análise de dados e aplicações de IA no mercado de seguros.

O Insurance Intelligence simula uma operação de seguros com dados inteiramente fictícios para explorar indicadores comerciais, desempenho de equipes, conversão de propostas, gestão de apólices e renovações.

## Demonstração
- **[Abrir dashboard demonstrativo](https://1mperador027.github.io/insurance-intelligence/)**.
- **[Baixar base CSV para Power BI](data/insurance_intelligence_csv.zip)**.
- **[Consultar documentação de arquitetura](docs/ARQUITETURA_E_MODELO.md)**.
- **[Consultar medidas DAX](power-bi/Medidas_DAX_PowerBI.txt)**.

## Base analítica disponível
O pacote CSV contém:
- 1.500 propostas;
- 779 apólices emitidas;
- 420 eventos de renovação;
- dimensões de calendário, mês, produto, equipe e unidade;
- metas mensais por produto;
- dicionário de dados.

A base foi conferida quanto à unicidade dos identificadores, integridade das referências entre propostas, apólices e renovações e consistência da quantidade de propostas emitidas. Os dados são sintéticos e não representam uma operação real.

## O que o protótipo demonstra
- Indicadores de produção, conversão, prêmio médio e renovações;
- visualizações comerciais e de carteira;
- estrutura dimensional para evolução no Power BI;
- medidas DAX iniciais;
- comentários gerenciais baseados em regras determinísticas.

## Tecnologias e conceitos
Excel, CSV, Power BI (estrutura preparada), DAX, modelagem dimensional, HTML, JavaScript, Business Intelligence e Inteligência Artificial aplicada aos negócios.

## Premissas e transparência
- Todos os registros, nomes, unidades, equipes, valores e resultados são **fictícios e sintéticos**.
- O projeto não utiliza dados reais de clientes, colaboradores, instituições ou operações.
- Não possui vínculo institucional, patrocínio, endosso ou integração com o Itaú ou qualquer outra instituição financeira.
- Não se conecta a sistemas corporativos, APIs privadas ou bases externas.
- A leitura inteligente é baseada em regras fixas; não há modelo de IA generativa integrado.
- O arquivo Power BI (.pbix), autenticação, backend e integrações operacionais não fazem parte desta versão.

## Próximas evoluções
Disponibilizar a planilha Excel e o PDF de portfólio diretamente no repositório, aprofundar a documentação e montar o arquivo PBIX com validação de relacionamentos e medidas.

---
**Insurance Intelligence — projeto independente de aprendizagem.**
