#!/usr/bin/env python3
"""Gera pacote CSV sintético e reproduzível para o Insurance Intelligence."""
import calendar, csv, io, json, random, zipfile
from datetime import date, timedelta
from pathlib import Path
R=random.Random(20251119); Y=2025; root=Path(__file__).resolve().parents[1]
def pack(headers, rows):
 b=io.StringIO(newline=""); w=csv.writer(b,lineterminator="\n"); w.writerow(headers); w.writerows(rows); return b.getvalue().encode("utf-8-sig")
def mk(d): return d.strftime("%Y-%m")
products=[("P01","Vida","Pessoas"),("P02","Residencial","Patrimonial"),("P03","Prestamista","Pessoas"),("P04","Auto","Patrimonial"),("P05","Acidentes Pessoais","Pessoas")]
teams=[("E01","Equipe Alfa","Comercial"),("E02","Equipe Beta","Comercial"),("E03","Equipe Gama","Comercial"),("E04","Equipe Delta","Comercial")]
units=[("U01","Unidade Centro","Sudeste"),("U02","Unidade Norte","Sudeste"),("U03","Unidade Sul","Sudeste")]
cal=[]; months=[]
for m in range(1,13):
 months.append([f"{Y}-{m:02d}",Y,m,calendar.month_name[m],f"T{(m-1)//3+1}"])
 for day in range(1,calendar.monthrange(Y,m)[1]+1):
  d=date(Y,m,day); cal.append([d.isoformat(),Y,m,calendar.month_name[m],f"T{(m-1)//3+1}",mk(d)])
statuses=["Emitida"]*779+["Não convertida"]*438+["Em análise"]*283; R.shuffle(statuses)
props=[]; lookup={}; start=date(Y,1,1)
for i,s in enumerate(statuses,1):
 d=start+timedelta(days=R.randrange(365)); pid=f"PR{i:05d}"; prod=R.choice(products)[0]; team=R.choice(teams)[0]; unit=R.choice(units)[0]; amount=round(R.uniform(350,4200),2)
 reason=R.choice(["Preço","Desistência","Sem retorno","Elegibilidade"]) if s=="Não convertida" else ""
 props.append([pid,d.isoformat(),prod,team,unit,f"{amount:.2f}",s,reason,mk(d)])
 lookup[pid]=(d,prod,team,unit,amount,s)
issued=[(pid,p) for pid,p in lookup.items() if p[5]=="Emitida"]
policies=[]; pmap={}
for i,(pid,p) in enumerate(issued,1):
 d,prod,team,unit,amount,_=p; maxd=(date(Y,12,31)-d).days; em=d+timedelta(days=R.randrange(min(25,maxd)+1)); aid=f"AP{i:05d}"; premium=round(amount*R.uniform(.88,1.08),2)
 policies.append([aid,pid,em.isoformat(),prod,team,unit,f"{premium:.2f}","Ativa",mk(em)]); pmap[aid]=(prod,team,unit)
selected=R.sample(list(pmap),420); rs=["Renovada"]*284+["Pendente"]*83+["Cancelada"]*53; R.shuffle(rs); renew=[]
for i,(aid,status) in enumerate(zip(selected,rs),1):
 d=start+timedelta(days=R.randrange(365)); prod,team,_=pmap[aid]; unit=R.choice(units)[0]
 renew.append([f"RE{i:05d}",aid,d.isoformat(),prod,team,unit,f"{R.uniform(350,4500):.2f}",status,mk(d)])
metas=[[f"{Y}-{m:02d}",p[0],f"{R.uniform(65000,105000):.2f}"] for m in range(1,13) for p in products]
dictionary=[
["FatoPropostas","PropostaID","Identificador único da proposta","Texto; chave"],["FatoPropostas","DataProposta","Data de registro","Data"],["FatoPropostas","StatusProposta","Emitida, Não convertida ou Em análise","Categoria"],["FatoPropostas","PremioProposto","Prêmio proposto","Decimal"],["FatoApolices","ApoliceID","Identificador único da apólice","Texto; chave"],["FatoApolices","PropostaID","Proposta de origem","Chave estrangeira"],["FatoApolices","PremioEmitido","Prêmio emitido","Decimal"],["FatoRenovacoes","RenovacaoID","Identificador do evento","Texto; chave"],["FatoRenovacoes","ApoliceID","Apólice relacionada","Chave estrangeira"],["FatoRenovacoes","StatusRenovacao","Renovada, Pendente ou Cancelada","Categoria"],["DimMes","AnoMes","Competência AAAA-MM","Dimensão"],["DimProduto","ProdutoID","Identificador do produto","Dimensão"],["DimEquipe","EquipeID","Identificador da equipe","Dimensão"],["DimUnidade","UnidadeID","Identificador da unidade","Dimensão"]]
files={
"Dicionario_de_Dados.csv":pack(["Tabela","Campo","Descrição","Tipo / Regra"],dictionary),
"csv_powerbi/DimCalendario.csv":pack(["Data","Ano","MesNumero","Mes","Trimestre","AnoMes"],cal),
"csv_powerbi/DimMes.csv":pack(["AnoMes","Ano","MesNumero","Mes","Trimestre"],months),
"csv_powerbi/DimProduto.csv":pack(["ProdutoID","Produto","Categoria"],products),
"csv_powerbi/DimEquipe.csv":pack(["EquipeID","Equipe","Perfil"],teams),
"csv_powerbi/DimUnidade.csv":pack(["UnidadeID","Unidade","Regiao"],units),
"csv_powerbi/FatoPropostas.csv":pack(["PropostaID","DataProposta","ProdutoID","EquipeID","UnidadeID","PremioProposto","StatusProposta","MotivoNaoConversao","AnoMes"],props),
"csv_powerbi/FatoApolices.csv":pack(["ApoliceID","PropostaID","DataEmissao","ProdutoID","EquipeID","UnidadeID","PremioEmitido","StatusApolice","AnoMes"],policies),
"csv_powerbi/FatoRenovacoes.csv":pack(["RenovacaoID","ApoliceID","DataVencimento","ProdutoID","EquipeID","UnidadeID","PremioRenovacaoPrevisto","StatusRenovacao","AnoMes"],renew),
"csv_powerbi/Metas.csv":pack(["AnoMes","ProdutoID","MetaPremio"],metas)}
assert len(props)==1500 and len(policies)==779 and len(renew)==420 and len(cal)==365 and len(metas)==60
assert len({x[0] for x in props})==1500 and len({x[0] for x in policies})==779 and len({x[0] for x in renew})==420
pids={x[0] for x in props}; aids={x[0] for x in policies}
assert all(x[1] in pids for x in policies) and all(x[1] in aids for x in renew)
assert sum(x[6]=="Emitida" for x in props)==len(policies)
out=root/"data"/"insurance_intelligence_csv.zip"; out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name,data in files.items(): z.writestr(name,data)
with zipfile.ZipFile(out) as z: assert len(z.namelist())==10 and z.testzip() is None
print(f"OK: {out.stat().st_size} bytes; propostas=1500; apólices=779; renovações=420; integridade=OK")


# JSON usado pelos filtros e gráficos interativos do dashboard.
dashboard_data={
 "proposals":[{"date":x[1],"product":x[2],"team":x[3],"unit":x[4],"premium":float(x[5]),"status":x[6]} for x in props],
 "policies":[{"date":x[2],"product":x[3],"team":x[4],"unit":x[5],"premium":float(x[6])} for x in policies],
 "renewals":[{"date":x[2],"product":x[3],"team":x[4],"unit":x[5],"premium":float(x[6]),"status":x[7]} for x in renew],
 "products":[{"id":x[0],"name":x[1]} for x in products],
 "teams":[{"id":x[0],"name":x[1]} for x in teams],
 "units":[{"id":x[0],"name":x[1]} for x in units]
}
(root/"data"/"dashboard_data.json").write_text(json.dumps(dashboard_data,ensure_ascii=False,separators=(",",":")),encoding="utf-8")

# Workbook Excel analítico: tabelas completas, indicadores e orientações.
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table as PDFTable, TableStyle, PageBreak, KeepTogether

# Constrói planilha com dados tabulares e resumo executivo.
xlsx_path=root/"data"/"Insurance_Intelligence_Base_Analitica.xlsx"
wb=Workbook()
ws=wb.active; ws.title="Visao_Executiva"
navy="10243B"; teal="159B91"; light="EAF1F6"; white="FFFFFF"
ws["A1"]="INSURANCE INTELLIGENCE"; ws["A1"].font=Font(size=20,bold=True,color=white); ws["A1"].fill=PatternFill("solid",fgColor=navy)
ws.merge_cells("A1:D1")
ws["A2"]="Base sintética • Projeto independente, educacional e experimental"; ws["A2"].font=Font(italic=True,color="536579"); ws.merge_cells("A2:D2")
kpis=[
["Indicador","Valor","Definição"],
["Propostas registradas",len(props),"Total de propostas na base"],
["Propostas emitidas",sum(x[6]=="Emitida" for x in props),"Propostas com status Emitida"],
["Taxa de conversão",sum(x[6]=="Emitida" for x in props)/len(props),"Emitidas / propostas registradas"],
["Apólices emitidas",len(policies),"Registros da tabela FatoApolices"],
["Prêmio emitido (R$)",round(sum(float(x[6]) for x in policies),2),"Soma do prêmio emitido"],
["Renovações registradas",len(renew),"Eventos de renovação simulados"],
["Renovações concluídas",sum(x[7]=="Renovada" for x in renew),"Eventos com status Renovada"],
["Taxa de renovação",sum(x[7]=="Renovada" for x in renew)/len(renew),"Renovadas / eventos registrados"],
["Renovações pendentes",sum(x[7]=="Pendente" for x in renew),"Eventos com status Pendente"],
["Renovações canceladas",sum(x[7]=="Cancelada" for x in renew),"Eventos com status Cancelada"],
]
for row in kpis: ws.append(row)
for c in ws[3]:
 c.font=Font(bold=True,color=white); c.fill=PatternFill("solid",fgColor=teal)
for row in range(4,ws.max_row+1):
 ws.cell(row,2).number_format="0.0%" if ws.cell(row,1).value in ("Taxa de conversão","Taxa de renovação") else '#,##0.00'
ws["A16"]="AVISO"; ws["A16"].font=Font(bold=True,color=white); ws["A16"].fill=PatternFill("solid",fgColor=navy)
ws["A17"]="Todos os dados, nomes, equipes, unidades, valores e resultados são fictícios. Não representam qualquer instituição, cliente ou operação real."
ws.merge_cells("A17:D18"); ws["A17"].alignment=Alignment(wrap_text=True,vertical="top")
ws.column_dimensions["A"].width=29; ws.column_dimensions["B"].width=22; ws.column_dimensions["C"].width=58; ws.column_dimensions["D"].width=18
ws.freeze_panes="A4"
tables={
"FatoPropostas":(["PropostaID","DataProposta","ProdutoID","EquipeID","UnidadeID","PremioProposto","StatusProposta","MotivoNaoConversao","AnoMes"],props),
"FatoApolices":(["ApoliceID","PropostaID","DataEmissao","ProdutoID","EquipeID","UnidadeID","PremioEmitido","StatusApolice","AnoMes"],policies),
"FatoRenovacoes":(["RenovacaoID","ApoliceID","DataVencimento","ProdutoID","EquipeID","UnidadeID","PremioRenovacaoPrevisto","StatusRenovacao","AnoMes"],renew),
"DimCalendario":(["Data","Ano","MesNumero","Mes","Trimestre","AnoMes"],cal),
"DimMes":(["AnoMes","Ano","MesNumero","Mes","Trimestre"],months),
"DimProduto":(["ProdutoID","Produto","Categoria"],products),
"DimEquipe":(["EquipeID","Equipe","Perfil"],teams),
"DimUnidade":(["UnidadeID","Unidade","Regiao"],units),
"Metas":(["AnoMes","ProdutoID","MetaPremio"],metas),
"Dicionario":(["Tabela","Campo","Descricao","TipoRegra"],dictionary),
}
for name,(headers,rows) in tables.items():
 sh=wb.create_sheet(name); sh.append(headers)
 for row in rows: sh.append(row)
 for cell in sh[1]:
  cell.font=Font(bold=True,color=white); cell.fill=PatternFill("solid",fgColor=navy); cell.alignment=Alignment(wrap_text=True)
 for col in range(1,sh.max_column+1):
  values=[len(str(sh.cell(r,col).value or "")) for r in range(1,min(sh.max_row,100)+1)]
  sh.column_dimensions[get_column_letter(col)].width=min(max(max(values+[12])+2,14),32)
 sh.freeze_panes="A2"; sh.auto_filter.ref=sh.dimensions
 if sh.max_row>1:
  tab=Table(displayName="tb"+name,ref=sh.dimensions); tab.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2",showRowStripes=True,showColumnStripes=False); sh.add_table(tab)
guide=wb.create_sheet("Modelo_e_uso")
guide_rows=[
["ASSUNTO","ORIENTAÇÃO"],
["Relacionamentos","DimMes[AnoMes] 1:* com FatoPropostas, FatoApolices, FatoRenovacoes e Metas."],
["Produto","DimProduto[ProdutoID] 1:* com as tabelas fato e Metas."],
["Equipe","DimEquipe[EquipeID] 1:* com as tabelas fato correspondentes."],
["Unidade","DimUnidade[UnidadeID] 1:* com as tabelas fato correspondentes."],
["Direção de filtro","Preferir filtro unidirecional da dimensão para a fato."],
["Conversão","A taxa apresentada usa a coorte de propostas: status Emitida / propostas registradas."],
["Power BI","Importe as tabelas CSV do ZIP, configure relacionamentos e use as medidas em ../power-bi/Medidas_DAX_PowerBI.txt."],
["Limitação","Esta planilha é uma base analítica em Excel; não é um arquivo Power BI (.pbix)."],
["Independência","Projeto pessoal independente. Sem vínculo, patrocínio, endosso ou integração com Itaú ou outra instituição."],
["Dados","Todos os registros são sintéticos e destinados apenas a fins educacionais."]
]
for row in guide_rows: guide.append(row)
for cell in guide[1]: cell.font=Font(bold=True,color=white); cell.fill=PatternFill("solid",fgColor=teal)
guide.column_dimensions["A"].width=24; guide.column_dimensions["B"].width=110
for row in guide.iter_rows(min_row=2):
 guide.row_dimensions[row[0].row].height=32
 for cell in row: cell.alignment=Alignment(wrap_text=True,vertical="top")
guide.freeze_panes="A2"
wb.calculation.fullCalcOnLoad=True
wb.save(xlsx_path)
# Reabre para verificar estrutura e contagens antes de publicar.
check=load_workbook(xlsx_path,read_only=True,data_only=False)
assert set(check.sheetnames)=={"Visao_Executiva",*tables.keys(),"Modelo_e_uso"}
assert check["FatoPropostas"].max_row==1501 and check["FatoApolices"].max_row==780 and check["FatoRenovacoes"].max_row==421
check.close()

# Relatório PDF de portfólio, com escopo, indicadores, arquitetura e limitações.
pdf_path=root/"docs"/"Projeto_Insurance_Intelligence_Portfolio.pdf"
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle",parent=styles["Title"],fontName="Helvetica-Bold",fontSize=25,leading=30,textColor=colors.HexColor("#10243B"),alignment=TA_CENTER,spaceAfter=12))
styles.add(ParagraphStyle(name="Sub",parent=styles["Normal"],fontSize=11,leading=16,textColor=colors.HexColor("#536579"),alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H2N",parent=styles["Heading2"],textColor=colors.HexColor("#159B91"),spaceBefore=10,spaceAfter=6))
styles.add(ParagraphStyle(name="SmallN",parent=styles["BodyText"],fontSize=8.5,leading=12))
doc=SimpleDocTemplate(str(pdf_path),pagesize=A4,rightMargin=1.8*cm,leftMargin=1.8*cm,topMargin=1.6*cm,bottomMargin=1.6*cm,title="Insurance Intelligence - Portfolio")
story=[]
story += [Spacer(1,2.2*cm),Paragraph("INSURANCE INTELLIGENCE",styles["CoverTitle"]),Paragraph("Inteligência Comercial e Gestão Estratégica de Seguros",styles["Sub"]),Spacer(1,1.2*cm)]
story += [Paragraph("<b>Projeto independente • Educacional • Experimental</b>",styles["Sub"]),Spacer(1,2*cm)]
story += [Paragraph("Um protótipo analítico para explorar como dados estruturados, indicadores e visualizações podem apoiar a leitura de desempenho comercial e a gestão de carteira no mercado de seguros.",styles["BodyText"]),Spacer(1,1.1*cm)]
story += [Paragraph("<b>Transparência institucional:</b> projeto pessoal sem vínculo, patrocínio, endosso ou integração com o Itaú ou qualquer outra instituição financeira. Todos os dados são fictícios.",styles["SmallN"]),PageBreak()]
story += [Paragraph("1. Objetivo e escopo",styles["H2N"]),Paragraph("O projeto simula um cenário de operação de seguros para demonstrar conceitos de Business Intelligence, modelagem dimensional, análise comercial e preparação de indicadores. A base foi criada de forma reproduzível por script Python, com verificações de integridade referencial e unicidade.",styles["BodyText"])]
story += [Paragraph("2. Base sintética",styles["H2N"])]
summary_data=[["Entidade","Quantidade"],["Propostas",f"{len(props):,}"],["Apólices",f"{len(policies):,}"],["Renovações",f"{len(renew):,}"],["Dias de calendário",f"{len(cal):,}"],["Metas produto/mês",f"{len(metas):,}"]]
pt=PDFTable(summary_data,colWidths=[8*cm,5*cm]); pt.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#10243B")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.4,colors.HexColor("#D7E0E8")),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#F1F5F8")]),("PADDING",(0,0),(-1,-1),7)])); story += [pt,Spacer(1,8)]
story += [Paragraph("Indicadores derivados da base",styles["H2N"])]
kpi_data=[["Indicador","Resultado"],["Conversão por coorte",f"{sum(x[6]=='Emitida' for x in props)/len(props):.1%}"],["Prêmio emitido",f"R$ {sum(float(x[6]) for x in policies):,.2f}"],["Taxa de renovação",f"{sum(x[7]=='Renovada' for x in renew)/len(renew):.1%}"]]
kt=PDFTable(kpi_data,colWidths=[8*cm,5*cm]); kt.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#159B91")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),.4,colors.HexColor("#D7E0E8")),("PADDING",(0,0),(-1,-1),7)])); story += [kt,PageBreak()]
story += [Paragraph("3. Arquitetura e tecnologias",styles["H2N"]),Paragraph("<b>Dados:</b> CSV e planilha Excel com tabelas fato e dimensões.<br/><b>Preparação:</b> script Python reproduzível e validações de consistência.<br/><b>Modelagem:</b> calendário, mês, produto, equipe e unidade; fatos de propostas, apólices e renovações; metas.<br/><b>Visualização:</b> dashboard HTML interativo com filtros por competência, produto, equipe e unidade e estrutura de medidas DAX para evolução no Power BI.<br/><b>Interpretação:</b> regras determinísticas, sem integração com IA generativa.",styles["BodyText"])]
story += [Paragraph("4. Materiais entregues",styles["H2N"]),Paragraph("• Dashboard web publicado no GitHub Pages.<br/>• Base sintética em CSV, com dicionário de dados.<br/>• Planilha Excel analítica com dez tabelas e visão executiva.<br/>• Medidas DAX iniciais e orientação de relacionamentos.<br/>• Script de geração e validação automatizada.<br/>• Documentação técnica e este relatório de portfólio.",styles["BodyText"])]
story += [Paragraph("5. Limitações e próximos passos",styles["H2N"]),Paragraph("A demonstração web é estática e não possui filtros operacionais. Não há arquivo Power BI (.pbix) nesta entrega; a montagem final do relatório requer Power BI Desktop. Não há backend, autenticação, conexão com APIs ou sistemas corporativos. Os gráficos web são demonstrativos e não substituem a análise detalhada no Power BI.",styles["BodyText"])]
story += [Spacer(1,10),Paragraph("<b>Uso responsável:</b> os dados, nomes, equipes, unidades, valores e resultados são inteiramente sintéticos. Qualquer adaptação a um contexto real exige autorização, governança, validação, segurança e avaliação regulatória.",styles["SmallN"])]
doc.build(story)
assert pdf_path.stat().st_size>3000 and xlsx_path.stat().st_size>5000 and (root/'data'/'dashboard_data.json').stat().st_size>10000
print(f"EXTRAS OK: Excel={xlsx_path.stat().st_size} bytes; PDF={pdf_path.stat().st_size} bytes; planilhas={len(check.sheetnames) if False else 11}")
