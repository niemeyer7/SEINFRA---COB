import wx
import wx.adv


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

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.Quit,exitItem)
        
        self.comboOpcoes = ['EMOP','SCO-RIO','SINAPRI']
        self.boxcComp = wx.CheckBox(panel, wx.ID_ANY, 'Composicao',(25,10),size=(100,-1))
        self.Elemento = wx.CheckBox(panel,wx.ID_ANY,'Elemento',(25,30), size=(100,-1))
        self.lblCategoria = wx.StaticText(panel,wx.ID_ANY,'Categoria',(25,48), size=(100,-1))
        self.comboCategoria = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,65), choices = self.comboOpcoes, style=wx.CB_READONLY)
        self.lblCla = wx.StaticText(panel,wx.ID_ANY,'Cla',(25,89), size=(100,-1))
        self.comboCla = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,106), choices = self.comboOpcoes, style=wx.CB_READONLY)
        self.lblFamilia = wx.StaticText(panel,wx.ID_ANY,'Familia',(25,130), size=(100,-1))
        self.comboFamilia = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,147), choices = self.comboOpcoes, style=wx.CB_READONLY)
        self.lblitem = wx.StaticText(panel,wx.ID_ANY,'Familia',(25,170), size=(100,-1))
        self.comboitem = wx.ComboBox(panel, wx.ID_ANY, value='ID',pos = (25,187), choices = self.comboOpcoes, style=wx.CB_READONLY)

        self.desonerado = wx.CheckBox(panel,wx.ID_ANY,'Desonerado',(25,212), size=(100,-1))
        self.buttonFiltar = wx.Button(panel, wx.ID_ANY, 'Filtar', (25, 232),size=(100,-1))

        self.button_excluir = wx.Button(panel, wx.ID_ANY, 'Excluir', (25, 620),size=(100,-1))
        self.buttoninserircodigo = wx.Button(panel, wx.ID_ANY, 'Inserir', (400, 250),size=(100,-1))
        self.button_inserirtabela = wx.Button(panel, wx.ID_ANY, 'Inserir', (1070, 250),size=(100,-1))
        self.button_pesquisar = wx.Button(panel, wx.ID_ANY, 'Pesquisar', (600, 250),size=(100,-1))
        self.lblCodigo = wx.StaticText(panel,wx.ID_ANY,'Codigo',(200,250), size=(100,-1))
        self.caixacodigo = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (250,250), size=(150,-1))
        self.button_salvar = wx.Button(panel, wx.ID_ANY, 'Salvar', (1070, 620),size=(100,-1))
        
        self.buttonresetar = wx.Button(panel, wx.ID_ANY, 'Resetar', (600, 620),size=(100,-1))


        self.orcamentopesquisa = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_AUTOARRANGE,size=(980,220), pos=(200,10))      
        self.orcamentopesquisa.InsertColumn(0,"Item",width=50)
        self.orcamentopesquisa.InsertColumn(1,"Empresa",width=100)
        self.orcamentopesquisa.InsertColumn(2,"Codigo",width=200)
        self.orcamentopesquisa.InsertColumn(3,"Descrição",width=420)
        self.orcamentopesquisa.InsertColumn(4,"Unidade",width=100)
        self.orcamentopesquisa.InsertColumn(5,"Preço",width=100)
        
        self.lblprojeto = wx.StaticText(panel,wx.ID_ANY,'Projeto',(20,330), size=(100,-1))
        self.caixaprojeto = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (70,330), size=(150,-1))
        self.lbllocal = wx.StaticText(panel,wx.ID_ANY,'Local',(20,360), size=(100,-1))
        self.caixalocal = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (70,360), size=(150,-1))

        self.dateBegin = wx.adv.DatePickerCtrl(panel, wx.ID_ANY,wx.DefaultDateTime, pos=(450, 360),size=(100,-1))

        self.orcamentotabela = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_AUTOARRANGE,size=(1150,220), pos=(25,400))      
        self.orcamentotabela.InsertColumn(0,"Item",width=50)
        self.orcamentotabela.InsertColumn(1,"Empresa",width=100)
        self.orcamentotabela.InsertColumn(2,"Codigo",width=150)
        self.orcamentotabela.InsertColumn(3,"Descrição",width=420)
        self.orcamentotabela.InsertColumn(4,"Unidade",width=100)
        self.orcamentotabela.InsertColumn(5,"Preço",width=100)
        self.orcamentotabela.InsertColumn(6,"Quantidade",width=100)
        self.orcamentotabela.InsertColumn(7,"Total",width=120)
        self.SetTitle('eep')
        self.Show(True)



        
    def Quit(self, e):
        self.Close()
    
def main():

    app = wx.App()
    windowClass(None, "teste")

    app.MainLoop()

main()

