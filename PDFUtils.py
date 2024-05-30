import PyPDF2

class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = None
        self.page_content = None

    def extract_data(self):
        pdfFileObj = open(self.file_path, 'rb')
        
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        
        # creating a page object
        # pagina 1
        flag = True
        c = 0
        while flag:
            pageObj = pdfReader.pages[c]
            
            # extracting text from page
            self.page_content = pageObj.extract_text()

            s = self.page_content.find('IDENTIFICAÇÃO DO CONTRIBUINTE')
            content = self.page_content[s:]
            
            c += 1
            if s < 0: continue
            flag = False
            
            positions_dict = {
                'nome': content.find('Nome:'),
                'nascimento': content.find('Data de Nascimento'),
                'titulo': content.find('Título Eleitoral:'),
                'municipio': content.find('Município:'),
                'uf': content.find('UF:'),
                'ocupacao': content.find('Natureza da Ocupação:'),
                'cpf': content.find('CPF:'),
            }
            
            values = {
                'nome': None,
                'nascimento': None,
                'titulo': None,
                'municipio': None,
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
                if i == 'nascimento':
                    if 'Título' in aux:
                        position = aux.find('Título')
                        values[i] = aux[:position]
                        
                        values[i] = values[i].split(': ')[1]
                elif i == 'municipio':
                    if 'UF' in aux:
                        position = aux.find('UF')
                        values[i] = aux[:position]
                        
                        values[i] = values[i].split(': ')[1]
                elif i == 'cpf':
                    if 'Nome' in aux:
                        position = aux.find('Nome')
                        values[i] = aux[:position]
                        
                        values[i] = values[i].split(': ')[1]
                
                else:
                    values[i] = values[i].split(': ')[1]
        
        # closing the pdf file object
        pdfFileObj.close()
        return values
            
    def read(self):
        print(self.file_path)
        # creating a pdf file object
        pdfFileObj = open(self.file_path, 'rb')
        
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        
        # creating a page object
        # pagina 1 
        print(len(pdfReader.pages))
        pageObj = pdfReader.pages[0]
        
        # extracting text from page
        self.file_content = pageObj.extract_text()
        
        # closing the pdf file object
        pdfFileObj.close()
        
    def extract(self):
        self.read()
        
        s = self.file_content.find('IDENTIFICAÇÃO DO CONTRIBUINTE')
        content = self.file_content[s:]
        
        positions_dict = {
            'nome': content.find('Nome:'),
            'nascimento': content.find('Data de Nascimento'),
            'titulo': content.find('Título Eleitoral:'),
            'municipio': content.find('Município:'),
            'uf': content.find('UF:'),
            'ocupacao': content.find('Natureza da Ocupação:'),
            'cpf': content.find('CPF:'),
        }
        
        values = {
            'nome': None,
            'nascimento': None,
            'titulo': None,
            'municipio': None,
            'uf': None,
            'ocupacao': None,
            'cpf': None,
        }
        
        for i in positions_dict:
            print(i)
            start = positions_dict[i]
            aux = content[start:]
            aux = aux.split('\n')[0]
            
            values[i] = aux
            
            # sanitize
            if i == 'nascimento':
                if 'Título' in aux:
                    position = aux.find('Título')
                    values[i] = aux[:position]
                    
                    values[i] = values[i].split(': ')[1]
            elif i == 'municipio':
                if 'UF' in aux:
                    position = aux.find('UF')
                    values[i] = aux[:position]
                    
                    values[i] = values[i].split(': ')[1]
            elif i == 'cpf':
                if 'Nome' in aux:
                    position = aux.find('Nome')
                    values[i] = aux[:position]
                    
                    values[i] = values[i].split(': ')[1]
            
            else:
                print(values)
                values[i] = values[i].split(': ')[1]
            
        return values
     
       
        
        
    
        