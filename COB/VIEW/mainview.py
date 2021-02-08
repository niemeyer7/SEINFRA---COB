import wx
import wx.adv
import telapesquisa
import os



def main():
    windowClass(parent=None,title="Orcamento basico")

class windowClass (wx.Frame):
    def __init__ (self,parent,title):
        super(windowClass, self).__init__(parent, title=title, size= (1200,700))

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)


        menubar = wx.MenuBar()

        
        filebutton = wx.Menu()


        




        abaNovoOrcamento = filebutton.Append(wx.ID_ANY, "Novo Orcamento", "Novo Orcamento")
        abaCarregarOrcamento = filebutton.Append(wx.ID_ANY, "Carregar Orcamento", "Carregar Orcamento")
        exitItem = filebutton.Append(wx.ID_EXIT, "Sair")

        sizer = wx.GridBagSizer(5,5)
        menubar.Append(filebutton,"Arquivo")



        menuinserir= wx.Menu()

        menubar.Append(menuinserir,"Especial")
        inseriritem = menuinserir.Append(wx.ID_ANY, "Inserir Item", "Inserir Item")

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.Quit,exitItem)

        self.comboOpcoes = ['EMOP','SCO-RIO','SINAPRI']

        
        #Botoes

        self.comboFonte = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,65), choices = self.comboOpcoes, style=wx.CB_READONLY, size = (150,-1))
        self.comboCategoria = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,106), choices = self.comboOpcoes, style=wx.CB_READONLY, size = (150,-1))
        self.comboCla = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,147), choices = self.comboOpcoes, style=wx.CB_READONLY, size = (150,-1))
        self.comboFamilia = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,187), choices = self.comboOpcoes, style=wx.CB_READONLY, size = (150,-1))
        self.comboitem = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,227), choices = self.comboOpcoes, style=wx.CB_READONLY, size = (150,-1))
        self.buttonFiltar = wx.Button(panel, wx.ID_ANY, 'Filtar', (25, 277),size=(100,-1))
        self.button_excluir = wx.Button(panel, wx.ID_ANY, 'Excluir', (25, 620),size=(100,-1))
        self.buttoninserircodigo = wx.Button(panel, wx.ID_ANY, 'Inserir', (400, 250),size=(100,-1))
        self.button_inserirtabela = wx.Button(panel, wx.ID_ANY, 'Inserir', (1070, 250),size=(100,-1))
        self.button_pesquisar = wx.Button(panel, wx.ID_ANY, 'Pesquisar', (600, 250),size=(100,-1))
        self.button_salvar = wx.Button(panel, wx.ID_ANY, 'Salvar', (1070, 620),size=(100,-1))
        self.buttonresetar = wx.Button(panel, wx.ID_ANY, 'Resetar', (600, 620),size=(100,-1))

        #Checkbox
        self.boxcComp = wx.CheckBox(panel, wx.ID_ANY, 'Composicao',(25,10),size=(100,-1))
        self.Elemento = wx.CheckBox(panel,wx.ID_ANY,'Elemento',(25,30), size=(100,-1))
        self.desonerado = wx.CheckBox(panel,wx.ID_ANY,'Desonerado',(25,255), size=(100,-1))

        
        #Labels
        self.lblEmpresa = wx.StaticText(panel,wx.ID_ANY,'Fonte',(25,48), size=(100,-1))
        self.lblCategoria = wx.StaticText(panel,wx.ID_ANY,'Categoria',(25,89), size=(100,-1))
        self.lblCla = wx.StaticText(panel,wx.ID_ANY,'Cla',(25,130), size=(100,-1))
        self.lblFamilia = wx.StaticText(panel,wx.ID_ANY,'Familia',(25,170), size=(100,-1))
        self.lblitem = wx.StaticText(panel,wx.ID_ANY,'item',(25,210), size=(100,-1))
        self.lblCodigo = wx.StaticText(panel,wx.ID_ANY,'Codigo',(200,250), size=(50,-1))
        self.lblprojeto = wx.StaticText(panel,wx.ID_ANY,'Projeto',(20,330), size=(50,-1))
        self.lbllocal = wx.StaticText(panel,wx.ID_ANY,'Local',(20,360), size=(50,-1))
        self.lblbdi = wx.StaticText(panel, wx.ID_ANY,"BDI", (750,360), size=(50,-1))

        

        #Caixa txt

        self.caixacodigo = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (250,250), size=(150,-1))
        self.caixaprojeto = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (70,330), size=(150,-1))
        self.caixalocal = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (70,360), size=(150,-1))
        self.bdi = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (800,360), size=(150,-1))


        #bind pesquisa
        self.button_pesquisar.Bind(wx.EVT_BUTTON, self.janelapesquisa)

        #tabela filtro
        self.orcamentopesquisa = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_AUTOARRANGE,size=(980,220), pos=(200,10))      
        self.orcamentopesquisa.InsertColumn(0,"Item",width=50)
        self.orcamentopesquisa.InsertColumn(1,"Empresa",width=100)
        self.orcamentopesquisa.InsertColumn(2,"Codigo",width=200)
        self.orcamentopesquisa.InsertColumn(3,"Descrição",width=420)
        self.orcamentopesquisa.InsertColumn(4,"Unidade",width=100)
        self.orcamentopesquisa.InsertColumn(5,"Preço",width=100)
        

        #date
        self.dateBegin = wx.adv.DatePickerCtrl(panel, wx.ID_ANY,wx.DefaultDateTime, pos=(450, 360),size=(100,-1))

        #bind para pegar os dados do banco de dados  (maior parte dos botoes precisam estar vinculados com o banco)
        #bind para inserir os dados 

        # def carregaDadosCatalagosFiltrados(self,event):

        # coluna = self.comboFiltro.GetValue()
        # texto = self.txtFiltro.GetValue()
        
        # if coluna == "":
        #     coluna = ""

        # self.listaDeitensCatalago.DeleteAllItems()
        # self.index = 0
        # dados = geCDP.queryTabelaComWhereLike(tabela="",coluna=coluna,dado=texto)
        
        # for dado in dados:
        #     CatalagoQuery = modelcatalagos.catalagos(listaDeitensCatalago=dado)
        #     id = str(contratoQuery.id)
        #     Fonte = contratoQuery.idFonte
        #     Categoria = contratoQuery.categoria
        #     Cla = contratoQuery.cla
        #     Familia = contratoQuery.familia
        #     Item = contratoQuery.item 
        #     Desonerado = contratoQuery.desonerado
        #     Codigo = contratoQuery.codigo
        #     Descricao = contratoQuery.descricao
        #     Unidade = contratoQuery.unidade
        #     Preco = contratoQuery.preco
            

        #     self.listaDeitensCatalago.InsertStringItem(self.index, id)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 1, Fonte)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 2, Categoria)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 3, Cla)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 4, Familia)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 5, Item)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 6, Desonerado)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 7, Codigo)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 8, Descricao)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 9, Unidade)
        #     self.listaDeitensCatalago.SetStringItem(self.index, 9, Preco)
        #     self.index += 1

        # self.frame.Bind(wx.EVT_MENU, self.ViewInserirdados, self.inseriritem)

        #BIND SALVAR

        self.button_salvar.Bind(wx.EVT_BUTTON, self.onSave)


        #tabela orcamento
        self.orcamentotabela = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_AUTOARRANGE,size=(1150,220), pos=(25,400))      
        self.orcamentotabela.InsertColumn(0,"Item",width=50)
        self.orcamentotabela.InsertColumn(1,"Empresa",width=100)
        self.orcamentotabela.InsertColumn(2,"Codigo",width=150)
        self.orcamentotabela.InsertColumn(3,"Descrição",width=420)
        self.orcamentotabela.InsertColumn(4,"Unidade",width=100)
        self.orcamentotabela.InsertColumn(5,"Preço",width=100)
        self.orcamentotabela.InsertColumn(6,"Quantidade",width=100)
        self.orcamentotabela.InsertColumn(7,"Total",width=120)
        
        self.Show(True)

    def janelapesquisa(self, event):
        pesquisadescr = telapesquisa.telapesquisa(None, "")



    def Quit(self, e):
        self.Close()
    



    def onSave(self, event):
        try:
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        except:
            try:
                dlg = wx.FileDialog(self, "Save to file:", ".", "", "Text (*.txt)|*.txt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dlg.ShowModal() == wx.ID_OK):
                    self.filename = dlg.GetFilename()
                    self.dirname = dlg.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dlg.Destroy()
            except:
                pass

    def onSaveAs(self, event):
        try:
            dlg = wx.FileDialog(self, "Save to file:", ".", "", "Text (*.txt)|*.txt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if (dlg.ShowModal() == wx.ID_OK):
                    self.filename = dlg.GetFilename()
                    self.dirname = dlg.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
            dlg.Destroy()
        except:
            pass

if __name__ == '__main__':

    app = wx.App()
    main()  
    app.MainLoop()
