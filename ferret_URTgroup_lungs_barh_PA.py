"""
2021-05-03
Make stacked bar graphs for ferret lungs (34, 35, 36)
DONT FORGET TO RENAME READ_ID COLUMN IN INPUTS BEFORE STARTING
Note: this is massively faster if you exclude the stock barcodes
KA
"""

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

PA_colors = ["#ade9ff", "#47ceff","#003c52", "#00aeef", "#0096ce", '#c2ecff','#00547a','#70d2ff','#001c29','#008bcc'] #PA 10-color palette

######################################################################################################
######################################################################################################
######################################################################################################

#Ferret 34, 5 lobes plus stock, PA only

UL_34 = pd.read_csv('34UL_PA1_processed_5_to_3_barcode_clusters.csv')
LL_34 = pd.read_csv('34LL_PA1_processed_5_to_3_barcode_clusters.csv')
UR_34 = pd.read_csv('34UR_PA1_processed_5_to_3_barcode_clusters.csv')
MR_34 = pd.read_csv('34MR_PA1_processed_5_to_3_barcode_clusters.csv')
LR_34 = pd.read_csv('34LR_PA1_processed_5_to_3_barcode_clusters.csv')
#Nhe_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

ferret_34_dict = {'UL':UL_34,
           'LL':LL_34,
           'UR':UR_34,
           'MR':MR_34,
           'LR':LR_34,
           #'Stock':Nhe_stock
           }

for key,df in ferret_34_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['Lobe ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(ferret_34_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('ferret_34_lobe_concat.csv')
df_pivot=df_concat.pivot_table(index='Lobe ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=PA_colors, title='F34 PA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('F34_PA_all_lobes_rep1_barh.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()

######################################################################################################
######################################################################################################
######################################################################################################

#Ferret 35, 5 1 lobe only


MR_35 = pd.read_csv('35MR_PA1_processed_5_to_3_barcode_clusters.csv')
#Nhe_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

ferret_35_dict = {'MR':MR_35}

for key,df in ferret_35_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['Lobe ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(ferret_35_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('ferret_35_lobe_concat.csv')
df_pivot=df_concat.pivot_table(index='Lobe ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=PA_colors, title='F35 PA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('F35_PA_all_lobes_rep1_barh.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()

######################################################################################################
######################################################################################################
######################################################################################################

#Ferret 36, 5 lobes


UL_36 = pd.read_csv('36_UL_PA_processed_5_to_3_barcode_clusters.csv')
LL_36 = pd.read_csv('36_LL_PA_processed_5_to_3_barcode_clusters.csv')
UR_36 = pd.read_csv('36_UR_PA_processed_5_to_3_barcode_clusters.csv')
MR_36 = pd.read_csv('36MR_PA1_processed_5_to_3_barcode_clusters.csv')
LR_36 = pd.read_csv('36_LR_PA_processed_5_to_3_barcode_clusters.csv')
#Nhe_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

ferret_36_dict = {'UL':UL_36,
           'LL':LL_36,
           'UR':UR_36,
           'MR':MR_36,
           'LR':LR_36,
           #'Stock':Nhe_stock
           }

for key,df in ferret_36_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['Lobe ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(ferret_36_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('ferret_36_lobe_concat.csv')
df_pivot=df_concat.pivot_table(index='Lobe ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=PA_colors, title='F36 PA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('F36_PA_all_lobes_rep1_barh.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()