from csv_reader import CSVFileReader

if __name__ == "__main__":

    csv_file_reader = CSVFileReader(id=1,tipo_arquivo="csv")
    path_csv = ""
    csv_file_reader.calculate_sum(path_csv)
    csv_file_reader.print_string()

    # Fazer o mesmo para o json