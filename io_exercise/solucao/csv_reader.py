from base import BaseFileReader
import csv

class CSVFileReader(BaseFileReader):
    def __init__(self, id: int, tipo_arquivo:str ) -> None:

        super().__init__(id, tipo_arquivo)

        # passar infos para a super classe com super()
        # https://realpython.com/python-super/

    def calculate_sum(self, file_path):
        with open(file_path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file)

            self.soma=0
        
            for item in reader: 
                self.soma += float(item['SalePrice'])    
        
    # sobrescrever a funcao calculate_sum

