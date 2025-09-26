import pandas as pd

df = pd.read_excel('dados_fake.xlsx')

def validacao(df):
    erro = []

    for idx, linha in df.iterrows():
        if pd.isna(linha["Nome"]) or str(linha["Nome"]).strip() == "":
            erro.append(f"linha {idx} nome vazio")


    for idx, linha in df.iterrows():
        if pd.isna(linha["Idade"]) or linha["Idade"] >= 120 or linha["Idade"] <= 0:
            erro.append(f"linha {idx} idade nao condinzente")


    for idx, linha in df.iterrows():
        if pd.isna(linha["CPF"]) or str(linha["CPF"]).strip() == "":
            erro.append(f" linha {idx} CPF nao preenchido corretamente")
            

    for idx, linha in df.iterrows():
        if linha["Situação"] not in ['Desempregado','Empregado']:
            erro.append(f"linha {idx} situacao preenchiada errada")


    return erro

df_final = validacao(df)
for resp in df_final:
    print(resp)

print(df)
    