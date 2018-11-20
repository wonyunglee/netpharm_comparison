# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:54:39 2017

@author: Administrator
"""

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import scipy.stats

sns.set(style='whitegrid',palette='pastel')

os.chdir(r'C:\Users\Administrator\Desktop\netpharm_platform_comparison\compound_inconsistency\3.corr_res')

df_ttest = pd.DataFrame(columns=['platforms','type','pvalue'])

for w in range(3):
    for z in range(4):
        platform_list = ['TCMSP_BATMAN','BATMAN_mesh','mesh_TCMSP']
        result_list = ['target','GO','KEGG','OMIM']
        file_list = 'com_'+platform_list[w]+'_'+result_list[z]
    
        df1 = pd.read_excel('corr_'+file_list+'.xlsx')
        df2 = pd.DataFrame(columns=['type','corr_score','platforms'])
        
        plt.matshow(df1)
        plt.savefig('mat)'+file_list+'.png')
        plt.close()
        
        # 각 column(i), row(j)성분을 추출하여 df2로 옮겨넣기
        # 전체가 74개인것에 유의!
        order = -1
        for i in range(74):
            for j in range(74):
                order += 1
                if i!=j:
                    df2.loc[order] = ['non-identical',df1[i][j],platform_list[w]]
                elif i==j:
                    df2.loc[order] = ['identical',df1[i][j],platform_list[w]]
        df2 = df2.sort_values('type',ascending=True)
        df2 = df2.reset_index(drop=True)
        
        df2.to_excel('extract)'+file_list+'.xlsx')
        
        homo_data_before = df2['corr_score'][:74] 
        homo_data = homo_data_before[np.isfinite(homo_data_before)]
        
        hetero_data_before = df2['corr_score'][74:5476]
        hetero_data = hetero_data_before[np.isfinite(hetero_data_before)]

        
        t, p = scipy.stats.ttest_ind(homo_data, hetero_data, equal_var=False)
        df_ttest.loc[-1] = (platform_list[w],result_list[z],p)
        df_ttest.index = df_ttest.index +1
        
        # df2의 digonal(homogenous), non-digonal(heterogenous) data 나누
        
        sns_plot = sns.boxplot(x='type',y='corr_score',data=df2)
        fig = sns_plot.figure
        fig.savefig('sns)'+file_list+'.png')
        plt.gcf().clear()

df_ttest.to_excel('com_ttest.xlsx')