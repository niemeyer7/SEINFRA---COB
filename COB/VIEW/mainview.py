import sys
import wx
import wx.adv
import ViewTelaPesquisa
import os
import ViewInserirdados


def main():
    windowClass(parent=None,title="Orcamento basico")

class windowClass (wx.Frame):
    def __init__ (self,parent,title):
        super(windowClass, self).__init__(parent, title=title, size= (1200,710))

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)


        self.menubar = wx.MenuBar()

        
        self.filebutton = wx.Menu()


        




        self.abaNovoOrcamento = self.filebutton.Append(wx.ID_ANY, "Novo Orcamento", "Novo Orcamento")
        self.abaCarregarOrcamento = self.filebutton.Append(wx.ID_OPEN, "&Carregar Orcamento")
        self.exitItem = self.filebutton.Append(wx.ID_EXIT, "Sair")

        self.sizer = wx.GridBagSizer(5,5)
        self.menubar.Append(self.filebutton,"Arquivo")

        

        self.menuinserir= wx.Menu()

        self.menubar.Append(self.menuinserir,"Especial")
        self.inseriritem = self.menuinserir.Append(wx.ID_ANY, "Inserir Item", "Inserir Item")

        self.SetMenuBar(self.menubar)
        self.Bind(wx.EVT_MENU, self.Quit,self.exitItem)


        self.Bind(wx.EVT_MENU, self.JanelaInserirDados, self.inseriritem)


        self.comboOpcoesFontes = ['EMOP','SCO-RIO','SINAPRI']
        self.comboOpçõesCategorias = [
    "01 - SERVIÇOS DE ESCRITÓRIO, LABORATÓRIO E CAMPO",
    "02 - CANTEIRO DE OBRA",
    "03 - MOVIMENTO DE TERRA",
    "04 - TRANSPORTES",
    "05 - SERVIÇOS COMPLEMENTARES",
    "06 - GALERIAS, DRENOS E CONEXOS",
    "07 - ARGAMASSAS, INJEÇÕES E CONSOLIDAÇÕES",
    "08 - BASES E PAVIMENTOS",
    "09 - SERVIÇOS DE PARQUES E JARDINS",
    "10 - FUNDAÇÕES",
    "11 - ESTRUTURAS",
    "12 - ALVENARIAS E DIVISÓRIAS",
    "13 - REVESTIMENTO DE PAREDES, TETOS E PISOS",
    "14 - ESQUADRIAS DE PVC, FERRO, ALUMÍNIO OU MADEIRA, VIDRAÇAS E FERRAGENS",
    "15 - INSTALAÇÕES ELÉTRICAS, HIDRÁULICAS, SANITÁRIAS E MECÂNICAS",
    "16 - COBERTURAS, ISOLAMENTOS E IMPERMEABILIZAÇÕES",
    "17 - PINTURAS",
    "18 - APARELHOS HIDRÁULICOS, SANITÁRIOS, ELÉTRICOS, MECÂNICOS E ESPORTIVOS",
    "19 - ALUGUEL DE EQUIPAMENTOS",
    "20 - CUSTOS RODOVIÁRIOS",
    "21 - ILUMINAÇÃO PÚBLICA",
    "22 - REFLORESTAMENTO E EXPLORAÇÃO FLORESTAL"]
        
        #Botoes

        self.comboFonte = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (-1,65), choices = self.comboOpcoesFontes, style=wx.CB_READONLY, size = (260,-1))
        self.comboCategoria = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (-1,106), choices = self.comboOpçõesCategorias, style=wx.CB_READONLY, size = (260,-1))
        self.comboCla = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (-1,147), choices = self.comboOpcoesFontes, style=wx.CB_READONLY, size = (260,-1))
        self.comboFamilia = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (-1,187), choices = self.comboOpcoesFontes, style=wx.CB_READONLY, size = (260,-1))
        self.comboitem = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (-1,227), choices = self.comboOpcoesFontes, style=wx.CB_READONLY, size = (260,-1))
        self.buttonFiltar = wx.Button(panel, wx.ID_ANY, 'Filtar', (-1, 277),size=(100,-1))
        self.button_excluir = wx.Button(panel, wx.ID_ANY, 'Excluir', (-1, 620),size=(100,-1))
        self.buttoninserircodigo = wx.Button(panel, wx.ID_ANY, 'Inserir', (410, 280),size=(100,-1))
        self.button_inserirtabela = wx.Button(panel, wx.ID_ANY, 'Inserir', (1070, 280),size=(100,-1))
        self.button_pesquisar = wx.Button(panel, wx.ID_ANY, 'Pesquisar', (600, 280),size=(100,-1))
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
        self.lblCodigo = wx.StaticText(panel,wx.ID_ANY,'Codigo',(200,280), size=(50,-1))
        self.lblprojeto = wx.StaticText(panel,wx.ID_ANY,'Projeto',(20,330), size=(50,-1))
        self.lbllocal = wx.StaticText(panel,wx.ID_ANY,'Local',(20,360), size=(50,-1))
        self.lblbdi = wx.StaticText(panel, wx.ID_ANY,"BDI", (750,360), size=(50,-1))

        #sizer

        # sizerteste = wx.BoxSizer(wx.VERTICAL)
        # sizerteste.Add(self.comboFonte,0,wx.EXPAND)
        # sizerteste.Add(self.comboCategoria,0,wx.EXPAND)
        # sizerteste.Add(self.comboCla,0,wx.EXPAND)
        # sizerteste.Add(self.comboFamilia,,wx.EXPAND)
        # sizerteste.Add(self.comboitem,-1,wx.EXPAND)
        # sizerteste.Add(self.lblCodigo,-1)
        

        # self.SetSizer(sizerteste)
        #Caixa txt

        self.caixacodigo = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (250,280), size=(150,-1))
        self.caixaprojeto = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (70,330), size=(150,-1))
        self.caixalocal = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (70,360), size=(150,-1))
        self.bdi = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (800,360), size=(150,-1))


        #bind pesquisa
        self.button_pesquisar.Bind(wx.EVT_BUTTON, self.JanelaPesquisa)

        #bind inserir dados
        # self.inseriritem.Bind(wx.EVT_BUTTON, )

        #tabela filtro
        self.orcamentopesquisa = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_AUTOARRANGE,size=(920,250), pos=(262,10))      
        self.orcamentopesquisa.InsertColumn(0,"Empresa",width=100)
        self.orcamentopesquisa.InsertColumn(1,"Codigo",width=200)
        self.orcamentopesquisa.InsertColumn(2,"Descrição",width=420)
        self.orcamentopesquisa.InsertColumn(3,"Unidade",width=100)
        self.orcamentopesquisa.InsertColumn(4,"Preço",width=100)
        

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

    def JanelaPesquisa(self, event):
        pesquisadescr = ViewTelaPesquisa.telapesquisa(None, "")

    def JanelaInserirDados(self, event):
        Inserirdados = ViewInserirdados.TelaInserirDados(None, "")


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
