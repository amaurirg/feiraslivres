import csv
from conn_db import Conexao

arquivo_csv = "DEINFO_AB_FEIRASLIVRES_2014.csv"

file = open(arquivo_csv)
fileReader = csv.reader(file)
dados_csv = list(fileReader)

feiras = Conexao()

for row in dados_csv[1::]:
    feiras.insere((
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                    row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16]))

feiras.fecha_conexao()
print("Dados importados com sucesso!")
