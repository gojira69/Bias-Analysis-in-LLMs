import pandas as pd

df = pd.read_csv('SPICE-Data.csv')

df.to_csv('spiceData.tsv',sep='\t')
