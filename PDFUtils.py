import PyPDF2

class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = None
        
    def read(self):
        # creating a pdf file object
        pdfFileObj = open(self.file_path, 'rb')
        
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        
        # creating a page object
        # pagina 1 
        pageObj = pdfReader.pages[0]
        
        # extracting text from page
        self.file_content = pageObj.extract_text()
        self.extract()
        
        # closing the pdf file object
        pdfFileObj.close()
        
    def extract(self):
        s = self.file_content.find('IDENTIFICAÇÃO DO CONTRIBUINTE')
        content = self.file_content[s:]
        
        positions_dict = {
            'nome': content.find('Nome:'),
            'nascimento': content.find('Data de Nascimento'),
            'titulo': content.find('Título Eleitoral:'),
            'endereco': content.find('Município:'),
            'uf': content.find('UF:'),
            'ocupacao': content.find('Natureza da Ocupação:'),
            'cpf': content.find('CPF:'),
        }
        
        values = {
            'nome': None,
            'nascimento': None,
            'titulo': None,
            'endereco': None,
            'uf': None,
            'ocupacao': None,
            'cpf': None,
        }
        
        for i in positions_dict:
            start = positions_dict[i]
            aux = content[start:]
            aux = aux.split('\n')[0]
            
            values[i] = aux
            
            # sanitize
            if i == 'nome':
                pass
            elif i == 'titulo':
                pass
            elif i == 'uf':
                pass
            elif i == 'ocupacao':
                pass
            elif i == 'nascimento':
                if 'Título' in aux:
                    position = aux.find('Título')
                    values[i] = aux[:position]
            elif i == 'endereco':
                if 'UF' in aux:
                    position = aux.find('UF')
                    values[i] = aux[:position]
            elif i == 'cpf':
                if 'Nome' in aux:
                    position = aux.find('Nome')
                    values[i] = aux[:position]
            
        
        print(values)
                
        
# TODO:
# salvar o conteúdo em um csv    
       
        
        
    
        