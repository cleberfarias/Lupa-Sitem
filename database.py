import sqlite3

class Data_base:

    def __init__(self, name = 'system.db') -> None:        
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
        
    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alunos(

            CPF TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            COMPLEMENTO TEXT,
            MUNICIPIO TEXT,
            CONTATO TXT,
            EMAIL TXT,
            MATRICULA TXT,
            CURSO TXT,
            UNIDESCOLAR,
            

            PRIMARY KEY(CPF)
            );
        """) 
    def register_company(self, fullDataSet):       
        campos_tabela = ('CPF', 'NOME', 'LOGRADOURO', 'COMPLEMENTO', 'MUNICIPIO', 'CONTATO', 'EMAIL', 'MATRICULA', 'CURSO', 'UNIDESCOLAR')
        qntd = "?,?,?,?,?,?,?,?,?,?"
        cursor = self.connection.cursor()
    
        try:
            cursor.execute(f"INSERT INTO Alunos {campos_tabela} VALUES ({qntd})", fullDataSet)
            self.connection.commit()
            return "OK"
        except:
            return "Erro"

    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Alunos ORDER BY NOME")
            objetos = cursor.fetchall()
            return objetos
        except:
            pass
    def delete_companies(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Alunos WHERE CPF = '{id}' ")

            self.connection.commit()

            return "Cadastro de Alunos excluido com sucesso!"

        except:
            return "Erro ao Excluir registro!"
    def update_company(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Alunos SET
            CPF = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            COMPLEMENTO = '{fullDataSet[3]}',
            EMAIL = '{fullDataSet[4]}',
            CONTATO = '{fullDataSet[5]}',
            MATRICULA = '{fullDataSet[6]}',
            MUNICIPIO = '{fullDataSet[8]}',
            CURSO = '{fullDataSet[7]}',
            UNIDESCOLAR = '{fullDataSet[8]}'
            WHERE CPF = '{fullDataSet[0]}'""")
    
        self.connection.commit()

