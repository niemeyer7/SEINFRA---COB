import pandas as pd 
import modelcatalagos


emop =pd.read_csv("dadosgerais.csv", sep=';', error_bad_lines=False)
emop = emop.to_records(index=False)
emop = tuple(emop)


sinapi =pd.read_csv("sinapi.csv", sep=';', error_bad_lines=False)
sinapi = sinapi.to_records(index=False)
sinapi = tuple(sinapi)

for teste in emop:
    test2 = modelcatalagos.catalagos(listaDeitensCatalago=teste, tipo=2)

print(1)
print(test2)