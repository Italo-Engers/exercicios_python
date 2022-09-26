from base import BaseFileReader

class CSVFileReader(BaseFileReader):
    def __init__(self, id: int, tipo_arquivo:str ) -> None:
        super().__init__(id, tipo_arquivo)
        # passar infos para a super classe com super()
        # https://realpython.com/python-super/
        pass

    def calculate_sum(self, file_path):
        return super().calculate_sum(file_path)
    
    # sobrescrever a funcao calculate_sum

