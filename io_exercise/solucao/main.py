from csv_reader import CSVFileReader
from json_reader import JsonFileReader

if __name__ == "__main__":

    csv_file_reader = CSVFileReader(id=1,tipo_arquivo="csv")
    path_csv = "arquivos\how_prices.csv"
    
    csv_file_reader.calculate_sum(path_csv)
    csv_file_reader.print_string()

    json_file_reader = JsonFileReader(id=2,tipo_arquivo="json")
    path_json = "arquivos\how_prices.json"
    json_file_reader.calculate_sum(path_json)
    json_file_reader.print_string()

    # Fazer o mesmo para o json