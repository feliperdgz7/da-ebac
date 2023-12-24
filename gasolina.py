#import pacotes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#DataFrame
data = pd.read_csv('gasolina.csv', sep=',')

#Grafico
grafico = sns.lineplot(data=data, x="dia", y="venda")
sfig = grafico.get_figure()
sfig.savefig("gasolina.png", orientation="landscape")
