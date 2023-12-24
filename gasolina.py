#import pacotes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#DataFrame
data = pd.read_csv('gasolina.csv', sep=',')

#Grafico
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=data, x="dia", y="venda", color="red")
  grafico.set(title='Preço da Gasolina', xlabel='Dia', ylabel='Preço(R$)');
sfig = grafico.get_figure()
sfig.savefig("gasolina.png", orientation="landscape")
