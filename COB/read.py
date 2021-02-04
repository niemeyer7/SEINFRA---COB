import pandas as pd 

banco =pd.read_csv("dadosgerais.csv", sep=';', error_bad_lines=False)
print(banco)