import pandas as pd
from sqlalchemy import create_engine

USER = "root"
PASSWORD = "sua_senha"
HOST = "localhost"
DATABASE = "saude"

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

csv_files = ["D:/VS-Code/IntuitiveCare/Teste2-EmAndamento/Arquivos/4T2023.csv", "D:/VS-Code/IntuitiveCare/Teste2-EmAndamento/Arquivos/4T2024.csv"]

file = "D:/VS-Code/IntuitiveCare/Teste2-EmAndamento/Arquivos/4T2023.csv"
df = pd.read_csv(file, encoding="utf-8", sep=";", parse_dates=["DATA"], on_bad_lines='warn')  # Aqui você aplica a solução

for file in csv_files:
    print(f"Importando: {file}")
    
    df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")
    print(df.head())  

    df = pd.read_csv(file, encoding="utf-8", sep=";", parse_dates=["DATA"], on_bad_lines='warn')  
    
    df.columns = ["DATA_REGISTRO", "REG_ANS", "CD_CONTA_CONTABIL", "DESCRICAO", "VL_SALDO_INICIAL", "VL_SALDO_FINAL"]
    
    df.to_sql("despesas_saude", con=engine, if_exists="append", index=False)

print("Importação concluída!")
