'''
2021-05-17
Calculate Shannon Diversity (Hprime)
Change input file as needed. Alternatively, rewrite as a function.
KA
'''
import pandas as pd
import math
import numpy as np

df = pd.read_csv('Nhe_19amplified_HA_rep1_barcode_clusters.csv')

read_count=df['read_count']
total_reads=np.sum(df['read_count'])
df['H_input']=(read_count/total_reads)*(np.log(read_count/total_reads)) #log base natural log
H_input=df['H_input']
Hprime=np.sum(H_input)
Hprime=Hprime*(-1.0)
Hmax=np.log(len(df))
even=Hprime/Hmax #Pielou's evenness index
print('Shannon = '+str(Hprime))
print('Evenness = '+str(even))