import csv

class BaseFileReader():

    def __init__(self, id:int, tipo_arquivo:str) -> None:
        self.id = id
        self.tipo_arquivo = tipo_arquivo
        self.soma = None

    def calculate_sum(self, file_path):  

        with open(file_path, mode="r") as csv_file:
            reader = csv.dictreader(csv_file)

            for values in reader:
                self.soma = sum(values[1])
                return self.soma

            print('-fini-')

        raise NotImplementedError()

    def print_string(self):
        print(f"Print de arquivo com id {self.id}, tipo de arquivo {self.tipo_arquivo} e soma total {self.soma}")