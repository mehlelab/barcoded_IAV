'''
2021-06-01
Make venn diagrams for mice
KA
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import venn
from venn import venn
Pst_colors=["#ffed85", "#efa536","#ffd900",'#ffe75c','#f5d000',"#ffe347"]
#load dataframes
mouse7 = pd.read_csv('HA_Pst_R_rep1_barcode_clusters.csv')
mouse8 = pd.read_csv('HA_Pst_RR_rep1_barcode_clusters.csv')
mouse9 = pd.read_csv('HA_Pst_NA_rep1_barcode_clusters.csv')
mouse10 = pd.read_csv('HA_Pst_L_rep1_barcode_clusters.csv')
mouse11 = pd.read_csv('HA_Pst_LL_rep1_barcode_clusters.csv')
mouse12 = pd.read_csv('HA_Pst_LR_rep1_barcode_clusters.csv')
#NheI_stock = pd.read_csv('HA_Pst_stock_rep1_barcode_clusters.csv')

#convert dataframe to list format
mouse7_bc = mouse7['barcode_clusters'].values.tolist()
mouse8_bc = mouse8['barcode_clusters'].values.tolist()
mouse9_bc = mouse9['barcode_clusters'].values.tolist()
mouse10_bc = mouse10['barcode_clusters'].values.tolist()
mouse11_bc = mouse11['barcode_clusters'].values.tolist()
mouse12_bc = mouse12['barcode_clusters'].values.tolist()
#stock_bc = NheI_stock['barcode_clusters'].values.tolist()

######################################################################################################

#Plot 3dpi mice
data_dict = {'Mouse 7':set(mouse7_bc),
             'Mouse 8': set(mouse8_bc),
             'Mouse 9': set(mouse9_bc)
             }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=8,cmap=Pst_colors)
plt.savefig('mice_pst_3dpi_venn.svg')

#Plot 6dpi mice
data_dict = {'Mouse 10':set(mouse10_bc),
             'Mouse 11': set(mouse11_bc),
             'Mouse 12': set(mouse12_bc)
             }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=8,cmap=Pst_colors)
plt.savefig('mice_pst_6dpi_venn.svg')
'''
#Plot all mice
data_dict = {'Mouse 7':set(mouse7_bc),
             'Mouse 8': set(mouse8_bc),
             'Mouse 9': set(mouse9_bc),
             'Mouse 10':set(mouse10_bc),
             'Mouse 11': set(mouse11_bc),
             'Mouse 12': set(mouse12_bc)
             }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6,cmap=Pst_colors)
plt.savefig('mice_pst_all_venn.png',dpi=600)
'''
print('DONE')