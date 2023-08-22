from tkinter import *       
from tkinter import ttk
import Funcs

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
    
        ###CRIAÇÃO BOTÃO BUSCAR
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.045, rely=0.85, relwidth=0.1, relheight=0.12)
        ###CRIAÇÃO BOTÃO NOVO PACIENTE 
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'), command= self.add_paciente)
        self.bt_novo.place(relx= 0.145, rely=0.85, relwidth=0.1, relheight=0.12)
        ###CRIAÇÃO BOTÃO ADICIONAR MEDICAÇÃO
        self.bt_adicionar = Button(self.frame_1, text='Adicionar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_adicionar.place(relx= 0.70, rely=0.85, relwidth=0.1, relheight=0.12)
        ###CRIAÇÃO BOTÃO APAGAR
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx= 0.80, rely=0.85, relwidth=0.1, relheight=0.12)

        ##CRIACAO DE LABEL DO ID
        self.lb_id = Label(self.frame_1, text = 'ID', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_id.place(relx= 0.045, rely= 0.02)
        
        self.id_entry = Entry(self.frame_1)
        self.id_entry.place(relx=0.045, rely=0.10, relwidth=0.08)

        ##CRIACAO DE LABEL DO STATUS
        self.lb_status = Label(self.frame_1, text = 'Status', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_status.place(relx= 0.65, rely= 0.02)

        self.status_entry = Entry(self.frame_1)
        self.status_entry.place(relx=0.65, rely=0.10, relwidth=0.25)

        ##CRIACAO DE LABEL DO STATUS
        self.lb_disp = Label(self.frame_1, text = 'PRIMEIRA DISPENSAÇÃO', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_disp.place(relx= 0.65, rely= 0.4)

        self.disp_entry = Entry(self.frame_1)
        self.disp_entry.place(relx=0.65, rely=0.5, relwidth=0.25)

        ##CRIACAO DE LABEL E ENTRADA DO NOME
        self.lb_nome = Label(self.frame_1, text = 'Nome', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_nome.place(relx= 0.045, rely= 0.20)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.045, rely=0.30, relwidth=0.55)

        ##CRIACAO DE LABEL E ENTRADA DO CONVÊNIO
        self.lb_convenio = Label(self.frame_1, text = 'Convênio', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_convenio.place(relx= 0.045, rely= 0.40)

        self.convenio_entry = Entry(self.frame_1)
        self.convenio_entry.place(relx=0.045, rely=0.5, relwidth=0.4)

        ##CRIACAO DE LABEL E ENTRADA DO MEDICAMENTO
        self.medicamento = Label(self.frame_1, text = 'Medicamento', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.medicamento.place(relx= 0.045, rely= 0.6)

        self.medicamento_entry = Entry(self.frame_1)
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