from tkinter import *       
from tkinter import ttk
from funcs import Funcs

root = Tk()

class Application(Funcs):

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.limpa_cliente()
        self.monta_tabelas()
        self.select_lista()
        root.mainloop()
        
    def tela(self):
        self.root.title('Liberação de Medicamentos')
        self.root.configure(background= '#acb1f8')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 1366, height= 760)
        self.root.minsize(width=800, height=600)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#eaebfd', highlightbackground= 'white', highlightthickness=5)
        self.frame_1.place(relx=0.02 , rely= 0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd = 4, bg= '#eaebfd', highlightbackground= 'white', highlightthickness=5)
        self.frame_2.place(relx=0.02 , rely= 0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):

        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background='#eaebfd')
        self.aba2.configure(background='#eaebfd')

        self.abas.add(self.aba1, text = 'Cadastro')
        self.abas.add(self.aba2, text = 'Liberação')

        self.abas.place(relx=0.00, rely=0.0, relwidth=0.99, relheight=0.99)

        ###ABA 1
    
        ###CRIAÇÃO BOTÃO BUSCAR
        self.bt_buscar = Button(self.aba1, text='Buscar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.045, rely=0.85, relwidth=0.1, relheight=0.12)
        ###CRIAÇÃO BOTÃO NOVO PACIENTE 
        self.bt_novo = Button(self.aba1, text='Novo Paciente', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'), command= self.add_paciente)
        self.bt_novo.place(relx= 0.145, rely=0.85, relwidth=0.15, relheight=0.12)
        ###CRIAÇÃO BOTÃO APAGAR
        self.bt_apagar = Button(self.aba1, text='Apagar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx= 0.80, rely=0.85, relwidth=0.1, relheight=0.12)
        ##CRIACAO DE LABEL DO ID
        self.lb_id = Label(self.aba1, text = 'ID', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_id.place(relx= 0.045, rely= 0.02)
        self.id_entry = Entry(self.aba1)
        self.id_entry.place(relx=0.045, rely=0.10, relwidth=0.08)
        ##CRIACAO DE LABEL E ENTRADA DO NOME
        self.lb_nome = Label(self.aba1, text = 'Nome', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_nome.place(relx= 0.045, rely= 0.20)
        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.045, rely=0.30, relwidth=0.55)
        ##CRIACAO DE LABEL E ENTRADA DO CONVÊNIO
        self.lb_convenio = Label(self.aba1, text = 'Convênio', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_convenio.place(relx= 0.045, rely= 0.40)
        self.convenio_entry = Entry(self.aba1)
        self.convenio_entry.place(relx=0.045, rely=0.5, relwidth=0.4)


        ###ABA 2

        ###CRIAÇÃO BOTÃO BUSCAR
        self.bt_buscar = Button(self.aba2, text='Buscar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.045, rely=0.85, relwidth=0.1, relheight=0.12)
        ###CRIAÇÃO BOTÃO NOVO PACIENTE 
        self.bt_novo = Button(self.aba2, text='Novo', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'), command= self.add_paciente)
        self.bt_novo.place(relx= 0.145, rely=0.85, relwidth=0.1, relheight=0.12)
        ###CRIAÇÃO BOTÃO APAGAR
        self.bt_apagar = Button(self.aba2, text='Apagar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx= 0.80, rely=0.85, relwidth=0.1, relheight=0.12)
        ##CRIACAO DE LABEL DO ID
        self.lb_id = Label(self.aba2, text = 'ID', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_id.place(relx= 0.045, rely= 0.02)
        self.id_entry = Entry(self.aba2)
        self.id_entry.place(relx=0.045, rely=0.10, relwidth=0.08)
        ##CRIACAO DE LABEL DO STATUS
        self.lb_status = Label(self.aba2, text = 'Status', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_status.place(relx= 0.65, rely= 0.02)
        self.status_entry = Entry(self.aba2)
        self.status_entry.place(relx=0.65, rely=0.10, relwidth=0.25)
        ##CRIACAO DE LABEL DA DISPENSACAO
        self.lb_disp = Label(self.aba2, text = 'PRIMEIRA DISPENSAÇÃO', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_disp.place(relx= 0.65, rely= 0.4)
        self.disp_entry = Entry(self.aba2)
        self.disp_entry.place(relx=0.65, rely=0.5, relwidth=0.25)
        ##CRIACAO DE LABEL E ENTRADA DO NOME
        self.lb_nome = Label(self.aba2, text = 'Nome', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_nome.place(relx= 0.045, rely= 0.20)
        self.nome_entry = Entry(self.aba2)
        self.nome_entry.place(relx=0.045, rely=0.30, relwidth=0.55)
        ##CRIACAO DE LABEL E ENTRADA DO CONVÊNIO
        self.lb_convenio = Label(self.aba2, text = 'Convênio', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_convenio.place(relx= 0.045, rely= 0.40)
        self.convenio_entry = Entry(self.aba2)
        self.convenio_entry.place(relx=0.045, rely=0.5, relwidth=0.4)
        ##CRIACAO DE LABEL E ENTRADA DO MEDICAMENTO
        self.medicamento = Label(self.aba2, text = 'Medicamento', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.medicamento.place(relx= 0.045, rely= 0.6)
        self.medicamento_entry = Entry(self.aba2)
        self.medicamento_entry.place(relx=0.045, rely=0.7, relwidth=0.4)

    #CONSTRUINDO TREEVIEW
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=('col1','col2','col3','col4','col5'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='CONVENIO')
        self.listaCli.heading('#4', text='PRIMEIRA DISPENSAÇÃO')
        self.listaCli.heading('#5', text='STATUS')

        self.listaCli.column('#0', width=1, stretch=NO)
        self.listaCli.column('#1', width=30)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=100)
        self.listaCli.column('#4', width=100)
        self.listaCli.column('#5', width=200)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrool_lista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.1, relheight=0.85)

        
Application()