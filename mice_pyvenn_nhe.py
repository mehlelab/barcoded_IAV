'''
2021-06-01
Make venn diagrams for mice
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import venn
from venn import venn

Pst_colors=["#ffed85", "#efa536","#ffd900",'#ffe75c','#f5d000',"#ffe347"]
Nhe_colors=['#1844bc','#c9d5f8', '#102e7e','#5d82ea','#133490','#edf1fd']

mouse1 = pd.read_csv('HA_Nhe_R_rep1_barcode_clusters.csv')
mouse2 = pd.read_csv('HA_Nhe_RR_rep1_barcode_clusters.csv')
mouse3 = pd.read_csv('HA_Nhe_NA_rep1_barcode_clusters.csv')
mouse4 = pd.read_csv('HA_Nhe_L_rep1_barcode_clusters.csv')
mouse5 = pd.read_csv('HA_Nhe_LL_rep1_barcode_clusters.csv')
mouse6 = pd.read_csv('HA_Nhe_LR_rep1_barcode_clusters.csv')
#NheI_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

#convert dataframe to list format
mouse1_bc = mouse1['barcode_clusters'].values.tolist()
mouse2_bc = mouse2['barcode_clusters'].values.tolist()
mouse3_bc = mouse3['barcode_clusters'].values.tolist()
mouse4_bc = mouse4['barcode_clusters'].values.tolist()
mouse5_bc = mouse5['barcode_clusters'].values.tolist()
mouse6_bc = mouse6['barcode_clusters'].values.tolist()
#stock_bc = NheI_stock['barcode_clusters'].values.tolist()

######################################################################################################

#Plot 3dpi mice
data_dict = {'Mouse 1':set(mouse1_bc),
             'Mouse 2': set(mouse2_bc),
             'Mouse 3': set(mouse3_bc)
             }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=8,cmap=Nhe_colors)
plt.savefig('mice_nhe_3dpi_venn.svg')

#Plot 6dpi mice
data_dict = {'Mouse 4':set(mouse4_bc),
             'Mouse 5': set(mouse5_bc),
             'Mouse 6': set(mouse6_bc)
             }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=8,cmap=Nhe_colors,legend_loc='best')
plt.savefig('mice_nhe_6dpi_venn.svg')
'''
#Plot all mice
data_dict = {'Mouse 1':set(mouse1_bc),
             'Mouse 2': set(mouse2_bc),
             'Mouse 3': set(mouse3_bc),
             'Mouse 4':set(mouse4_bc),
             'Mouse 5': set(mouse5_bc),
             'Mouse 6': set(mouse6_bc)
             }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6,cmap=Nhe_colors)
plt.savefig('mice_nhe_all_venn.png',dpi=600)
'''
print('DONE')