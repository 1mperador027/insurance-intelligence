# Definições, premissas e limitações

## Natureza dos dados
A base é sintética e reproduzível. Nenhum registro representa cliente, colaborador, unidade, produto, contrato ou operação real.

## Conversão
A conversão demonstrativa considera propostas criadas no período selecionado e identifica quais possuem status Emitida. A medida DAX usa a coorte da proposta, não divide apólices emitidas no mês por propostas abertas no mesmo mês.

## Leitura inteligente
Os textos de insight são gerados por regras determinísticas. Não há modelo generativo, treinamento, inferência por IA externa ou integração com serviços de IA.

## Limitações
- Sem arquivo .pbix nesta entrega; a planilha Excel analítica e o relatório PDF são gerados automaticamente no deploy.
- Sem conexão com sistemas ou APIs externas.
- Sem autenticação ou backend.
- A publicação é hospedada no GitHub Pages e gerada por GitHub Actions.
- O dashboard tem filtros funcionais por competência, produto, equipe e unidade, com indicadores e gráficos calculados a partir da base sintética.
- Indicadores e regras servem apenas para demonstração.

## Independência institucional
Projeto pessoal, independente, educacional e experimental. Não possui vínculo institucional, patrocínio, endosso ou integração com o Itaú ou qualquer outra instituição financeira.
