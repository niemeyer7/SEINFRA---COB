import psycopg2

def conectar():
    connect = psycopg2.connect(host = '10.9.198.106',database = 'COB', user = 'postgres', password = 'wes@123')
    cursor = connect.cursor()
    return connect,cursor

def comandos_sql(sql,fetchall=False):
    connect,cursor = conectar()
    cursor.execute(sql)    
    if fetchall == True:
        dados = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()
    if fetchall == True:
        return dados

def query_tabela(tabela):
    connect,cursor = conectar()
    cursor.execute("""SELECT * FROM {tabela}""".format(tabela=tabela))
    dados = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()
    return dados

def query_inclusao(fk_empresa_id,categoria,cla,familia,item,desonerado,CODIGO,descricao,unidade,preco):
    connect,cursor = conectar()
    cursor.execute("""
    INSERT INTO catalogo(fk_empresa_id, categoria, cla,familia, item, desonerado, CODIGO, descricao, unidade, PRECO)
    VALUES(   
        {fk_empresa_id}, 
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
        fk_empresa_id=fk_empresa_id,
        categoria=categoria,
        cla=cla,
        familia=familia,
        item=item,
        desonerado=desonerado,
        decricao=descricao,
        unidade=unidade,
        preco=preco
        ))
    connect.commit()
    cursor.close()
    connect.close()
    

if __name__ == "__main__":
    dado = query_tabela(tabela='catalogo')
    for i in dado:
        print(i)
    
    # query_inclusao()
