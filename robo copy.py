import pandas as pd
import re
from datetime import datetime

df = pd.read_excel('usuarios_1000.xlsx')

def validar_data(data_val):

    if pd.isna(data_val):
        return False
    
    if isinstance(data_val, (datetime, pd.Timestamp)):
        return True
    
    formatos = ["%d/%m/%Y", "%Y-%m-%d"]
    for fmt in formatos:
        try:
            datetime.strptime(str(data_val), fmt)
            return True
        except ValueError:
            continue
    return False


def validacao(df):

    erro_por_linha = []
    
    cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    celular = r"^(\+55\s?)?(\(?\d{2}\)?\s?)?\d{4,5}-?\d{4}$"
    
    for idx, linha in df.iterrows():

        erro = []

        if pd.isna(linha["Nome Completo"]) or str(linha["Nome Completo"]).strip() == "":
            erro.append(f"linha {idx} nome vazio")

        if pd.isna(linha["Idade"]) or linha["Idade"] >= 120 or linha["Idade"] <= 0:
            erro.append(f"linha {idx} idade nao condinzente")

        valor = str(linha["CPF"])
        if not re.fullmatch(cpf , valor):
            erro.append(f" linha {idx} CPF nao preenchido corretamente")
            
        telefone = str(linha["Telefone"])
        if not re.fullmatch(celular, telefone):
            erro.append(f"linha {idx} telefone preenchido no formato errado")

        data_nasc = linha["Data de Nascimento"]
        if not validar_data(data_nasc):
            erro.append(f"linha {idx} data dde nascimento errada")

        if  pd.isna(linha["Renda Mensal (R$)"]) or linha["Renda Mensal (R$)"] < 0:
            erro.append(f"{idx} renda mensal invalida")

        data_insc = linha["Data de Inscrição"]
        if not validar_data(data_insc):
            erro.append(f"liha {idx} data de incricao invalida")

        if pd.isna(linha["Nome do Responsável"]) or str(linha["Nome do Responsável"]).strip() == "":
            erro.append(f"linha {idx} nome preenchido de maneira errada")

        erro_por_linha.append('; '.join(erro))
    
    df["Erros"] = erro_por_linha
    return df

df_final = validacao(df)
df_final.to_excel("usuarios_1000_com_erros.xlsx", index=False)

df_final.to_html("planilha_com_erros.html", index=False)