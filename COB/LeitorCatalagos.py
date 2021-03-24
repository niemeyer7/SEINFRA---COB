import pandas as pd 
import modelcatalagos



# for item in emop:

#     x = modelcatalagos.catalagos(listaDeitensCatalago=emop[1], tipo=2)


#     print(x.idFonte)

#CSV Catalagos sem preco

emopsP = pd.read_csv("C:/Users/oscar.ribeiro/Desktop/SEINFRA---COB/COB/dadosEMOPsPreco.csv", sep=':', error_bad_lines=False)
emopsP = tuple(emopsP.to_records(index=False))


#CSV Preco itens

# precoemop = pd.read_csv("C:/Users/oscar.ribeiro/Desktop/SEINFRA---COB/COB/dadosEMOPsPreco.csv", sep=':', error_bad_lines=False)

x = modelcatalagos.catalagos(listaDeitensCatalago=emopsP[1], tipo=2)