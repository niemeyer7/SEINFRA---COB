class catalagos:
    def __init__(self, listaDeitensCatalago):
        self.listaDeitensCatalago = listaDeitensCatalago
        

    def ajustarDados(self):
        self.idFonte = self.listaDeitensCatalago[0]
        self.categoria = self.listaDeitensCatalago[1]
        self.cla = self.listaDeitensCatalago[2]
        self.familia = self.listaDeitensCatalago[3]
        self.item = self.listaDeitensCatalago[4]
        self.desonerado = self.listaDeitensCatalago[5]
        self.codigo = self.listaDeitensCatalago[6]
        self.descricao = self.listaDeitensCatalago[7]
        self.unidade = self.listaDeitensCatalago[8]
        self.preco = self.listaDeitensCatalago[9]
        

        