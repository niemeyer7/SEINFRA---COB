import wx


def main():
    teste()

class teste(object):
    """docstring for teste"""
    def __init__(self):
        super(teste, self).__init__()

        self.frame = wx.Frame(None, -1, 'Gerador Orçamento Basico', style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        self.frame.SetDimensions(0,0,1500,800)
        self.panel = wx.Panel(self.frame)

        self.statusbar =  self.frame.CreateStatusBar(1)

        self.menu_arquivo = wx.Menu()
        self.abaNovoOrcamento = self.menu_arquivo.Append(wx.ID_ANY, "Novo Orcamento", "Novo Orcamento")
        self.abaCarregarOrcamento = self.menu_arquivo.Append(wx.ID_ANY, "Carregar Orcamento", "Carregar Orcamento")

        self.menuAjuda = wx.Menu()
        self.abaAjuda = self.menuAjuda.Append(wx.ID_ANY, "Ajuda", "Ajuda")

        self.menu_bar = wx.MenuBar()
        self.menu_bar.Append(self.menu_arquivo,"Arquivo")
        self.menu_bar.Append(self.menuAjuda,"Ajuda")
        self.frame.SetMenuBar(self.menu_bar)

        self.comboOpcoes = ['EMOP','SCO-RIO','SINAPRI']

        self.comboFiltro = wx.ComboBox(self.panel, wx.ID_ANY, value='ID',pos = (25,60), choices = self.comboOpcoes, style=wx.CB_READONLY)

        self.buttonFiltar = wx.Button(self.panel, wx.ID_ANY, 'Filtar', (25, 300),size=(100,-1))



        self.button_excluir = wx.Button(self.panel, wx.ID_ANY, 'Excluir', (25, 690),size=(100,-1))
        self.buttoninserircodigo = wx.Button(self.panel, wx.ID_ANY, 'Inserir', (400, 250),size=(100,-1))
        self.button_inserirtabela = wx.Button(self.panel, wx.ID_ANY, 'Inserir', (1350, 250),size=(100,-1))
        self.button_pesquisar = wx.Button(self.panel, wx.ID_ANY, 'Pesquisar', (750, 250),size=(100,-1))
        self.caixacodigo = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, (250,250), size=(150,-1))
        self.button_salvar = wx.Button(self.panel, wx.ID_ANY, 'Salvar', (1350, 690),size=(100,-1))

        self.buttonresetar = wx.Button(self.panel, wx.ID_ANY, 'Resetar', (750, 690),size=(100,-1))


        #wx.StaticText(self.panel, wx.ID_ANY, "Filtra", (25, 25))
        #self.txtFiltro = wx.TextCtrl(self.panel, wx.ID_ANY,"", (60, 25),size=(500, -1),style=wx.TE_PROCESS_ENTER)
        
        self.frame.Show()
        self.frame.Centre()


if __name__ == '__main__':
    app = wx.App()
    main()  
    app.MainLoop()