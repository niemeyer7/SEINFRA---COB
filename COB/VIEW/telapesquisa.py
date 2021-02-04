import wx

class telapesquisa (wx.Frame):
    def __init__ (self,parent,title):
        super(telapesquisa, self).__init__(parent, title=title, size= (1200,700))

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        
        self.lblpesquisar = wx.StaticText(panel,wx.ID_ANY,'Pesquisa',(25,230), size=(100,-1))
        self.caixapesquisar = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, (25,250), size=(150,-1))
        self.buttonpesquisar = wx.Button(panel, wx.ID_ANY, 'Pesquisar', (25, 300),size=(100,-1))


        self.orcamentopesquisa = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LC_AUTOARRANGE,size=(980,650), pos=(200,10))      
        self.orcamentopesquisa.InsertColumn(0,"Empresa",width=100)
        self.orcamentopesquisa.InsertColumn(1,"Codigo",width=200)
        self.orcamentopesquisa.InsertColumn(2,"Descrição",width=420)
        self.orcamentopesquisa.InsertColumn(3,"Unidade",width=100)
        self.orcamentopesquisa.InsertColumn(4,"Preço",width=100)
       
        
        self.Show(True)

    
def main():

    app = wx.App()
    telapesquisa(None, "teste")

    app.MainLoop()




