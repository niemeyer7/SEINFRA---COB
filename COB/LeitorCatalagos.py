import pandas as pd 
# import modelcatalagos


emop =pd.read_csv("C:/Users/oscar.ribeiro/Desktop/SEINFRA---COB/COB/dadosgerais.csv", sep=':', error_bad_lines=False)
emop = emop.to_records(index=False)
emop = tuple(emop)
print(emop[1])

# sinapi =pd.read_csv("C:/Users/oscar.ribeiro/Desktop/SEINFRA---COB/COB/sinapi.csv", sep=':', error_bad_lines=False)
# sinapi = sinapi.to_records(index=False)
# sinapi = tuple(sinapi)
# print(sinapi[1])


# for item in emop:

#     x = modelcatalagos.catalagos(listaDeitensCatalago=emop[1], tipo=2)


#     print(x.idFonte)

#CSV Catalagos sem preco

# emopsP = pd.read_csv("C:/Users/oscar.ribeiro/Desktop/SEINFRA---COB/COB/dadosEMOPsPreco.csv", sep=':', error_bad_lines=False)

#CSV Preco itens


for i in emop:
    print(i)