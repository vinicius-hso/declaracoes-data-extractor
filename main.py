import os
import sys
import csv
from PDFUtils import Reader

input_dir_path = input('Insira o caminho do diretório de "Declarações": ')
output_dir_path = input('Insira o caminho de diretõrio para salvar o arvquido de relatório: ')

# teste local
# input_dir_path = "C:\\Users\\vinicius\\Downloads\\declaracoes\\declaracoes"
# input_dir_path = 'C:\\Users\\vinicius\\Downloads\\dec'
# output_dir_path = input_dir_path

# C:\Users\vinicius\Downloads\declaracoes\declaracoes

def get_pdf_paths(dir_path, pdfs = []):

    # percorrer dirs e salvar .pdf em lista
    pdfs_paths = []
    dirs = os.listdir(dir_path)

     # percorrer os diretórios
    for dir in dirs:
        # ignorando arquivos invisíveis
        if '.' == dir[0] or "." in dir : continue   
        
        # identificando Plataforma
        windows_platform = 'win32' in sys.platform
        
        # montando caminho do arquivo de acordo com a plataforma
        path = ""
        path = f'{dir_path}\\{dir}' if windows_platform else f'{dir_path}/{dir}'
        
        # # listar arquivos do diretorio
        files = os.listdir(path)
        
        for file in files:
            if ".pdf" in file:
                file_path = f'{path}\\{file}' if windows_platform else f'{path}/{file}'
                pdfs_paths.append(file_path)
        
    return pdfs_paths

def get_pdf_content(pdf_path):
    reader = Reader(pdf_path)
    content = reader.extract_data()
    # print(content)
    return content 
    
def create_csv_report(out, headers, content):

    windows_platform = 'win32' in sys.platform
    out_file =  f'{out}\\relatorio.csv' if windows_platform else f'{out}/relatorio.csv'
    

    with open(out_file, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)

        # create headers
        writer.writerow(headers)

        for c in content:
            # write a row to the csv file
            writer.writerow(c.values())

HEADERS = {
    "NOME": None,
    "DATA NASCIMENTO": None,
    "TÍTULO ELEITORAL": None,
    "MUNICÍPIO": None,
    "UF": None,
    "OCUPAÇÃO": None,
    "CPF": None
}

if __name__ == '__main__':

    pdfs = get_pdf_paths(input_dir_path)
    content = [get_pdf_content(pdf) for pdf in pdfs]

    create_csv_report(output_dir_path, HEADERS, content)
    print(f'Relatório criado com sucesso: `{output_dir_path}')
                
# /Users/viniciusoliveira/Downloads/declaracoes