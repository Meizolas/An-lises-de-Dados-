import pandas as pd
import zipfile as zf
import tabula as tab
import os 
import sys

sys.stdout.reconfigure(encoding='utf-8')

zip_filename = "Anexos.zip"
pdf_filename = "Anexo_1.pdf"

with zf.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extract(pdf_filename)
    
pdf_path = os.path.join(os.getcwd(), pdf_filename)

df = tab.read_pdf(pdf_path, pages='all', stream=True, lattice=True, multiple_tables=True)
for idx, tabela in enumerate(df, start=1):
    print(f"\nTabela {idx}:")
    print(tabela.to_string(index=True))
    
tabela_csv = pd.concat(df, ignore_index=True, sort=False)
tabela_csv = tabela_csv.rename (columns=lambda x: x.replace('OD', 'Odontológica').replace('AMB', 'Ambulatorial'))

csv_filename = "tabela.csv"
tabela_csv.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"\nTabela salva em {csv_filename}")    

zip_filename = "Teste_Helio_Nunes.zip"
with zf.ZipFile(zip_filename, 'w', zf.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename, os.path.basename(csv_filename))
    
    
    
       

os.remove(pdf_filename)
os.remove(csv_filename)