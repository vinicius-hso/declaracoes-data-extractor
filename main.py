import os
import sys
import csv
from PDFUtils import Reader

# ler entrada do usuário path destino dos arquivos
path = input('Insira o caminho do diretório de "Declarações": ')

# verificar diretório
dirs = os.listdir(path)

# TODO: criar csv...
with open('./relatorio.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    
    headers = {
        "NOME": None,
        "DATA NASCIMENTO": None,
        "TÍTULO ELEITORAL": None,
        "MUNICÍPIO": None,
        "UF": None,
        "OCUPAÇÃO": None,
        "CPF": None
    }
    
    writer.writerow(headers)

    for dir in dirs:
        
        if '.' == dir[0]: continue
        
        dir_path = f'{path}/{dir}'
        
        files = os.listdir(dir_path)
        
        # diretório vazio
        if not len(files): continue
        
        pdfs_content = []
        
        for file in files:
            if '.pdf' in file:
                
                windows_platform = 'win32' in sys.platform
                # ler e extrair dados do arquivo
                file_path = f'{dir_path}\{file}' if windows_platform else f'{dir_path}/{file}'
                reader = Reader(file_path)
                content = reader.extract()
                pdfs_content.append(content)
                
        for c in pdfs_content:
            # write a row to the csv file
            writer.writerow(c.values())
                
                
# /Users/viniciusoliveira/Downloads/declaracoes