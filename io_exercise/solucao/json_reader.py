from base import BaseFileReader
import json

class JsonFileReader(BaseFileReader):
    def __init__(self, id: int, tipo_arquivo:str ) -> None:

        super().__init__(id, tipo_arquivo)

        # passar infos para a super classe com super()
        # https://realpython.com/python-super/
    def calculate_sum(self, file_path): 
        with open(file_path, 'r') as f:
            data = (json.load(f))
            data_filtrada = data['SalePrice']
            data_valores = data_filtrada.values()   
          
            self.soma=0
            for kind in data_valores:                  
                self.soma += float(kind)
             


            

    
    
    # sobrescrever a funcao calculate_sum