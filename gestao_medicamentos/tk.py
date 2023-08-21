from tkinter import *       

root = Tk()

class Application():

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
        

    def tela(self):
        self.root.title('Cadastro de Clientes')
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
        ###CRIAÇÃO BOTÃO LIMPAR
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.20, rely=0.1, relwidth=0.1, relheight=0.15)
        ###CRIAÇÃO BOTÃO BUSCAR
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.30, rely=0.1, relwidth=0.1, relheight=0.15)
        ###CRIAÇÃO BOTÃO NOVO
        self.bt_buscar = Button(self.frame_1, text='Novo', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.60, rely=0.1, relwidth=0.1, relheight=0.15)
        ###CRIAÇÃO BOTÃO ALTERAR
        self.bt_limpar = Button(self.frame_1, text='Alterar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.70, rely=0.1, relwidth=0.1, relheight=0.15)
        ###CRIAÇÃO BOTÃO APAGAR
        self.bt_buscar = Button(self.frame_1, text='Apagar', bd=2, bg = '#acb1f8', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx= 0.80, rely=0.1, relwidth=0.1, relheight=0.15)

        ##CRIACAO DE LABEL E ENTRADA DO CODIGO
        self.lb_codigo = Label(self.frame_1, text = 'Código', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_codigo.place(relx= 0.045, rely= 0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.045, rely=0.15, relwidth=0.08)

        ##CRIACAO DE LABEL E ENTRADA DO NOME
        self.lb_nome = Label(self.frame_1, text = 'Nome', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_nome.place(relx= 0.045, rely= 0.30)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.045, rely=0.40, relwidth=0.7)

        ##CRIACAO DE LABEL E ENTRADA DO TELEFONE
        self.lb_telefone = Label(self.frame_1, text = 'Telefone', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_telefone.place(relx= 0.05, rely= 0.60)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.045, rely=0.7, relwidth=0.4)

        ##CRIACAO DE LABEL E ENTRADA DA CIDADE
        self.lb_telefone = Label(self.frame_1, text = 'Cidade', bg='#eaebfd', font=('verdana', 10 , 'bold'))
        self.lb_telefone.place(relx= 0.55, rely= 0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.545, rely=0.7, relwidth=0.4)




Application()
    


