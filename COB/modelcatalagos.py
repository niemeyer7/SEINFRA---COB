# import usuarioDAO

class catalagos:
    def __init__(self, listaDeitensCatalago, tipo=1):
        self.listaDeitensCatalago = listaDeitensCatalago
        
        if tipo == 1:
            self.ajustarCatalago()
        
        if tipo == 2:
            self.ajustarCatalagoNovo()

    def ajustarCatalago(self):
        self.id = self.listaDeitensCatalago[0]
        self.idFonte = self.listaDeitensCatalago[1]
        self.categoria = self.listaDeitensCatalago[2]
        self.cla = self.listaDeitensCatalago[3]
        self.familia = self.listaDeitensCatalago[4]
        self.item = self.listaDeitensCatalago[5]
        self.desonerado = self.listaDeitensCatalago[6]
        self.codigo = self.listaDeitensCatalago[7]
        self.descricao = self.listaDeitensCatalago[8]
        self.unidade = self.listaDeitensCatalago[9]


    
    def ajustarCatalagoNovo(self):
        self.idFonte = self.listaDeitensCatalago[0]
        self.categoria = self.listaDeitensCatalago[1]
        self.cla = self.listaDeitensCatalago[2]
        self.familia = self.listaDeitensCatalago[3]
        self.item = self.listaDeitensCatalago[4]
        self.desonerado = self.listaDeitensCatalago[5]
        self.codigo = self.listaDeitensCatalago[6]
        self.descricao = self.listaDeitensCatalago[7]
        self.unidade = self.listaDeitensCatalago[8]
        

    # def gravarNoBanco(self):
    #     usuarioDAO.query_inclusao(idFonteEmpresa=self.idFonte,
    #     categoria=self.categoria,
    #     cla=self.cla,
    #     familia=self.familia,
    #     item=self.item,
    #     desonerado=self.desonerado,
    #     codigo=self.codigo,
    #     descricao=self.descricao,
    #     unidade=self.unidade,preco=self.preco)