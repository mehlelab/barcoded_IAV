"""
2021-05-21
Plot HA and PA bars for all ferret trachea
KA
"""

#Trachea, 34-36, PA and HA

import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

print('Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

#universally remove top and right spines
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

mpl.rcParams['font.size'] = 12 #change the font size
plt.rcParams['figure.figsize'] = [12, 6] #set default figure size

HA_colors = ['#102e7e','#5d82ea','#0e276c','#edf1fd','#1844bc','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #1844bc derived 10-color palette
PA_colors = ["#ade9ff", "#47ceff","#003c52", "#00aeef", "#0096ce", '#c2ecff','#00547a','#70d2ff','#001c29','#008bcc'] #PA 10-color palette

##########################################################################################################

HA_36 = pd.read_csv('36_trachea_HA_barcode_clusters.csv')
HA_35 = pd.read_csv('35_trachea_HA_barcode_clusters.csv')
HA_34 = pd.read_csv('34_trachea_HA_barcode_clusters.csv')

HA_trachea_dict = {'F36':HA_36,
           'F35':HA_35,
           'F34':HA_34,
           }

for key,df in HA_trachea_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['trachea_ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(HA_trachea_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('trachea_HA.csv')
df_pivot=df_concat.pivot_table(index='trachea_ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=HA_colors, title='Trachea HA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('trachea_HA_all.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()
##########################################################################################################

PA_36 = pd.read_csv('36_trachea_PA_processed_5_to_3_barcode_clusters.csv')
PA_35 = pd.read_csv('35_trachea_PA_processed_5_to_3_barcode_clusters.csv')
PA_34 = pd.read_csv('34_trachea_PA_processed_5_to_3_barcode_clusters.csv')

PA_trachea_dict = {'F36':PA_36,
           'F35':PA_35,
           'F34':PA_34,
           }

for key,df in PA_trachea_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['trachea_ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(PA_trachea_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('trachea_PA.csv')
df_pivot=df_concat.pivot_table(index='trachea_ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=PA_colors, title='Trachea PA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('trachea_PA_all.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()