#!/usr/bin/env python3
"""Gera pacote CSV sintético e reproduzível para o Insurance Intelligence."""
import calendar, csv, io, random, zipfile
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
