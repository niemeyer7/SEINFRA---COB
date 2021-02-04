import pandas as pd 

banco =pd.read_csv("dadosgerais.csv", sep=';', error_bad_lines=False)
pd.set_option('display.max_rows', banco.shape[0]+1)
