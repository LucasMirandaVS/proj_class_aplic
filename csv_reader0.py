import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_filtrado = df[df['nome']== 'Lewis']

print(df_filtrado)