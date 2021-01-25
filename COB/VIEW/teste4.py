import wx
   
class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(300, 250))
        self.painel1()
        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout() 
        
class panel1(wx.panel):
    def __init__ (self,-1, style=wx.SUNKEN_BORDER):
        button_excluir = wx.Button(self, wx.ID_ANY, 'Excluir', (25, 690),size=(100,-1))
        buttoninserircodigo = wx.Button(self, wx.ID_ANY, 'Inserir', (400, 250),size=(100,-1))
        button_inserirtabela = wx.Button(self, wx.ID_ANY, 'Inserir', (1350, 250),size=(100,-1))
        button_pesquisar = wx.Button(self, wx.ID_ANY, 'Pesquisar', (750, 250),size=(100,-1))
        caixacodigo = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, (250,250), size=(150,-1))
        button_salvar = wx.Button(self, wx.ID_ANY, 'Salvar', (1350, 690),size=(100,-1))

   
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 2, wx.EXPAND)
        box.Add(button_excluir, 1, wx.EXPAND)
        box.Add(buttoninserircodigo, 3, wx.EXPAND)
        box.Add(button_inserirtabela, 4, wx.EXPAND)
        box.Add(button_pesquisar, 5, wx.EXPAND)
        box.Add(caixacodigo, 6, wx.EXPAND)
        box.Add(button_salvar, 7, wx.EXPAND)
  
           
app = wx.PySimpleApp()
frame = MyFrame(None, -1, "Sizer Test")
frame.Show()
app.MainLoop()