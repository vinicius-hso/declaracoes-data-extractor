import os
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
    
    for file in files:
        if '.pdf' in file:
            
            # ler e extrair dados do arquivo
            file_path = f'{dir_path}/{file}'
            reader = Reader(file_path)
            reader.read()
            
            break