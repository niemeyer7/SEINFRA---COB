import wx

class windowClass (wx.Frame):
    def __init__ (self,parent,title):
        super(windowClass, self).__init__(parent, title=title, size= (1200,600))

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

        self.button_excluir = wx.Button(panel, wx.ID_ANY, 'Excluir', (25, 520),size=(100,-1))
        self.buttoninserircodigo = wx.Button(panel, wx.ID_ANY, 'Inserir', (400, 250),size=(100,-1))
        self.button_inserirtabela = wx.Button(panel, wx.ID_ANY, 'Inserir', (1070, 250),size=(100,-1))
        self.button_pesquisar = wx.Button(panel, wx.ID_ANY, 'Pesquisar', (600, 250),size=(100,-1))
        self.lblCodigo = wx.StaticText(panel,wx.ID_ANY,'Codigo',(200,250), size=(100,-1))
        self.caixacodigo = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (250,250), size=(150,-1))
        self.button_salvar = wx.Button(panel, wx.ID_ANY, 'Salvar', (1070, 520),size=(100,-1))
        
        self.buttonresetar = wx.Button(panel, wx.ID_ANY, 'Resetar', (600, 520),size=(100,-1))


        
        self.SetTitle('eep')
        self.Show(True)
    def Quit(self, e):
        self.Close()
    
def main():

    app = wx.App()
    windowClass(None, "teste")

    app.MainLoop()

main()

