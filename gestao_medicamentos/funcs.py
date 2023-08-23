from tkinter import *       
from tkinter import ttk
import sqlite3

class Funcs():

    def limpa_cliente(self):

        self.nome_entry.delete(0, END)
        self.convenio_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('clients.bd')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def monta_tabelas(self):
        self.conecta_bd(); print('Conectando ao banco de dados')
        ### CRIAR TABELAS
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
            nome_paciente VARCHAR(40) NOT NULL,
            convenio_paciente VARCHAR(40) NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS valida_liberacao (
            id_liberacao INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
            id_paciente INTEGER,
            primeira_dispensacao DATE NOT NULL,
            status VARCHAR(40) NOT NULL,
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente)
            );
        """)
            
        self.conn.commit(); print("Banco de Dados Up")
 
    def add_paciente(self):
        
        self.id = self.id_entry.get()
        self.nome = self.nome_entry.get()
        self.convenio = self.convenio_entry.get()

        if not self.nome or not self.convenio:
            raise ValueError("Os campos 'Nome' e 'Convenio' devem ser preenchidos")
        else:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO pacientes (nome_paciente, convenio_paciente)
                VALUES (?, ?)""", (self.nome, self.convenio)
            )
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_cliente()
            

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""
        SELECT id_paciente, nome_paciente, convenio_paciente FROM pacientes ORDER BY nome_paciente;
        """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
        