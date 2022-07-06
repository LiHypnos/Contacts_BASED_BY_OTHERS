import mysql.connector
from classe_contato import Contato

class DBj:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            password='q1w2e3',
            database='agenda'
        )
        self.my_c = self.conexao.cursor()

    def save_contacts(self, cod, nome, telefone, email):
        objec= Contato(cod, nome, telefone, email)
        comand_sql = f'insert into Contatos ' \
                     f'(nome,telefone,email) ' \
                     f' value ' \
                     f'("{objec.nome}", "{objec.telefone}", "{objec.email}")'
        self.my_c.execute(comand_sql)
        self.conexao.commit()

    def list_contacts(self):
        comand_sql = 'select * from Contatos'
        self.my_c.execute(comand_sql)
        list = self.my_c.fetchall()
        for i in list:
            print(i)

    def update_data(self,gen,valor,cod):
        comand_sql = f'update Contatos set {gen} = "{valor}" where id = {cod}'
        self.my_c.execute(comand_sql)
        self.conexao.commit()

    def delete_contact(self, cod):
        comand_sql = f'delete from Contatos where id = {cod}'
        self.my_c.execute(comand_sql)
        self.conexao.commit()
