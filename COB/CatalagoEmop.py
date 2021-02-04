import pandas as pd 
import modelcatalagos

banco =pd.read_csv("dadosgerais.csv", sep=';', error_bad_lines=False)
records = banco.to_records(index=False)
result = tuple(records)


