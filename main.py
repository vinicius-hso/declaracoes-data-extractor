import os
import csv
from PDFUtils import Reader

# ler entrada do usuário path destino dos arquivos
path = input('Insira o caminho do diretório de "Declarações": ')

# verificar diretório
dirs = os.listdir(path)

for dir in [dirs[0]]:
    
    if '.' == dir[0]: continue
    
    dir_path = f'{path}/{dir}'
    
    files = os.listdir(dir_path)
    
    # diretório vazio
    if not len(files): continue
    
    pdfs_content = []
    
    for file in files:
        if '.pdf' in file:
            
            # ler e extrair dados do arquivo
            file_path = f'{dir_path}/{file}'
            reader = Reader(file_path)
            content = reader.extract()
            pdfs_content.append(content)
            
    # TODO: criar csv...
    with open('./relatorio', 'w') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(content)