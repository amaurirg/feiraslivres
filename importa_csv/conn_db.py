import psycopg2
import sys
from decouple import config


class Conexao:
    def __init__(self):
        # Dados para acesso ao banco - precisam estar no arquivo .env
        self.con = f"""host='{config('LOCALHOST')}'
                      dbname='{config('DB')}'
                      user='{config('USER_DB')}'
                      password='{config('PASSWORD_DB')}'
                   """

        # Tenta fazer a conexão ao banco
        try:
            self.conexao = psycopg2.connect(self.con)
            self.cur = self.conexao.cursor()

        # Caso ocorra um erro, exibe a string abaixo e também a mensagem de Exception
        except Exception as e:
            print('Erro de conexão!\n\n{}'.format(e))
            sys.exit()

    # Insere os dados do arquivo CSV no banco de dados
    def insere(self, dados):
        self.cur.execute("""INSERT INTO feiraslivres (
                        long, lat, setcens, areap, coddist, distrito, codsubpref, subprefe, regiao5,
                        regiao8, nome_feira, registro, logradouro, numero, bairro, referencia) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (dados))

    # Salva as inserções no banco de dados e fecha a conexão
    def fecha_conexao(self):
        self.conexao.commit()
        self.conexao.close()