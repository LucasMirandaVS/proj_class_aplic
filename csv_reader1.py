# Refatorando o programa 0 e aplicando uma classe 
import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por_coluna(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]

# Caminho do arquivo CSV e filtros
arquivo_csv = './exemplo.csv'
filtro = ' disponibilidade'
limite = ' False'

# Criando instância da classe CsvProcessor
arquivo_CSV_final = CsvProcessor(arquivo_csv)
# Carregando o arquivo CSV
arquivo_CSV_final.carregar_csv()
# Aplicando filtro
print(arquivo_CSV_final.filtrar_por_coluna(filtro, limite))

arquivo_csv_2 = './exemplo2.csv'
limite2 = ' True'

arquivo_CSV_2 = CsvProcessor(arquivo_csv_2)
arquivo_CSV_2.carregar_csv()
print(arquivo_CSV_2.filtrar_por_coluna(filtro, limite2))



