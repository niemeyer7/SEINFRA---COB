import psycopg2

def conectar():
    connect = psycopg2.connect(host = '10.9.198.106',database = 'COB', user = 'postgres', password = 'wes@123')
    cursor = connect.cursor()
    return connect,cursor

def comandosSql(sql,fetchall=False):
    connect,cursor = conectar()
    cursor.execute(sql)    
    if fetchall == True:
        dados = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()
    if fetchall == True:
        return dados

def queryTabela(tabela):
    connect,cursor = conectar()
    cursor.execute("""SELECT * FROM {tabela}""".format(tabela=tabela))
    dados = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()
    return dados

def criarTabelaEmpresa():
    connect,cursor = conectar()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empresa(
        idFonte SERIAL PRIMARY KEY,
        Fonte VARCHAR(255) NOT NULL 
        )""") 
    connect.commit()
    cursor.close()
    connect.close()



def criarTabela():
    connect,cursor = conectar()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS catalogo(
        IDitem SERIAL PRIMARY KEY,
        idFonte INT, 
        categoria VARCHAR(255) NOT NULL, 
        cla VARCHAR(255) ,
        familia TEXT NOT NULL, 
        item TEXT NOT NULL, 
        desonerado BYTEA NOT NULL, 
        codigo VARCHAR(255) NOT NULL, 
        descricao TEXT NOT NULL, 
        unidade VARCHAR(255) NOT NULL , 
        preco decimal(12,2) NOT NULL,
        PRIMARY KEY (idFonte, IDitem),
        FOREIGN KEY (IDitem)
            REFERENCES catalogo (IDitem),
        FOREIGN KEY (idFonte)
            REFERENCES empresa (idFonte))
    
    """) 
    connect.commit()
    cursor.close()
    connect.close()




def query_inclusao(idFonte,categoria,cla,familia,item,desonerado,codigo,descricao,unidade,preco):
    connect,cursor = conectar()
    cursor.execute("""
    INSERT INTO catalogo(idFonte, categoria, cla,familia, item, desonerado, codigo, descricao, unidade, preco)
    VALUES(   
        {idFonte}, 
        {categoria},
        {cla},
        {familia},
        {item},
        {desonerado}, 
        {codigo},
        {descricao},
        {unidade},
        {preco})
    """.format(
        idFonte=idFonte,
        categoria=categoria,
        cla=cla,
        familia=familia,
        item=item,
        desonerado=desonerado,
        codigo=codigo,
        decricao=descricao,
        unidade=unidade,
        preco=preco
        ))
    connect.commit()
    cursor.close()
    connect.close()
    

if __name__ == "__main__":
    criarTabela()
    criarTabelaEmpresa()
    
    # query_inclusao()
