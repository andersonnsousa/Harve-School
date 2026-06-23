import pandas as pd
import matplotlib.pyplot as plt

dfhotel = pd.read_csv('http://harve.com.br/praticas/reservashotel.csv')
print(dfhotel.head())
print(dfhotel.info())

estadias_sem = dfhotel['estadias_em_noites_semana'].value_counts()
estadias_find = dfhotel['estadias_em_noites_finalsemana'].value_counts()

print(f'total :{estadias_sem.sum()}+{estadias_find.sum()}')