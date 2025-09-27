import pandas as pd
import re

df = pd.read_excel('dados_fake.xlsx')

def validacao(df):
    erro = []
    cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    celular = r"^(\+55\s?)?(\(?\d{2}\)?\s?)?\d{4,5}-?\d{4}$"

    for idx, linha in df.iterrows():
        if pd.isna(linha["Nome"]) or str(linha["Nome"]).strip() == "":
            erro.append(f"linha {idx} nome vazio")


        if pd.isna(linha["Idade"]) or linha["Idade"] >= 120 or linha["Idade"] <= 0:
            erro.append(f"linha {idx} idade nao condinzente")

        valor = str(linha["CPF"])
        if not re.fullmatch(cpf , valor):
            erro.append(f" linha {idx} CPF nao preenchido corretamente")
            
            
        if linha["Situação"] not in ['Desempregado','Empregado']:
            erro.append(f"linha {idx} situacao preenchiada errada")

        telefone = str(linha["Telefone"])
        if not re.fullmatch(celular, telefone):
            erro.append(f"linha {idx} telefone preenchido no formato errado")


    return erro

df_final = validacao(df)
for resp in df_final:
    print(resp)
html = df.to_html("planilha.html" ,  index=False)

print(html)
    