import wx


def main():
    telapesquisa(parent=None,title="")

class telapesquisa (wx.Frame):
    def __init__ (self,parent,title):
        super(telapesquisa, self).__init__(parent, title=title, size= (600,600))

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Fonte',(25,230), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (25,250), size=(50,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Categoria',(95,230), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (95,250), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Cla',(210,230), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (210,250), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Familia',(325,230), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (325,250), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Item',(440,230), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (440,250), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Desonerado',(25,290), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (25,310), size=(50,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Codigo',(95,290), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (95,310), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Descrição',(210,290), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (210,310), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Unidade',(325,290), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (325,310), size=(100,-1))
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Preço',(440,290), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (440,310), size=(100,-1))

        self.botaoInserir = wx.Button(panel,wx.ID_ANY,'Inserir',(440,530), size=(100,-1))
        self.botaoFechar = wx.Button(panel,wx.ID_ANY,'Fechar',(25,530), size=(100,-1))

        self.botaoFechar.Bind(wx.EVT_BUTTON, self.fechar)


        # self.buttonpesquisar = wx.Button(panel, wx.ID_ANY, 'Pesquisar', (25, 300),size=(100,-1))

       
        
        self.Show(True)


    def fechar(self, event):
        
        self.Close()

        self.Destroy()


if __name__ == '__main__':

    app = wx.App()
    main()  
    app.MainLoop()




