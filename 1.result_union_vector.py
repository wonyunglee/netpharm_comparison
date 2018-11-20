# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:42:28 2017

@author: Administrator
"""


import pandas as pd
import re
import os
import numpy as np

os.chdir (r'C:\Users\Administrator\Desktop\netpharm_platform_comparison\compound_inconsistency\compound_tar_GSEA')

# target result union vector 생성

target_list = []    

for i in range(74):
    TCMSP = pd.read_excel(str(i)+'_com_TCMSP_tar(adme).xlsx')
    if list(TCMSP) != []:
        TCMSP_tar = list(TCMSP['target'])
        target_list.extend(TCMSP_tar)

    BATMAN = pd.read_excel(str(i)+'_com_BATMAN_tar(adme).xlsx')
    if list(BATMAN) != []:
        BATMAN_tar = list(BATMAN['target'])
        target_list.extend(BATMAN_tar)
    
    mesh = pd.read_excel(str(i)+'_com_mesh_tar(adme).xlsx')
    if list(mesh) != []:
        mesh_tar = list(mesh['target'])
        target_list.extend(mesh_tar)

target_union_vector = pd.DataFrame(list(set(target_list)))
# #na와 nan이 포함되어 있음
target_union_vector = target_union_vector.sort_values(0)

# 해당 excel 파일의 0 column을 index로 만들면 vectorization 준비 완료!
target_union_vector.to_excel('com_tar_union_vector.xlsx')


# GSEA result의 vectorization

GSEA_type = ['GO','KEGG','OMIM']
for j in range(3):
    target_union_vector = pd.DataFrame()
    GSEA_list = []    
    for i in range(74):
        TCMSP = pd.read_excel(str(i)+'_com_TCMSP_'+str(GSEA_type[j])+'(adme).xlsx')
        TCMSP_tar = list(TCMSP['Term'])
        GSEA_list.extend(TCMSP_tar)
    
        BATMAN = pd.read_excel(str(i)+'_com_BATMAN_'+str(GSEA_type[j])+'(adme).xlsx')
        BATMAN_tar = list(BATMAN['Term'])
        GSEA_list.extend(BATMAN_tar)
        
        mesh = pd.read_excel(str(i)+'_com_mesh_'+str(GSEA_type[j])+'(adme).xlsx')
        mesh_tar = list(mesh['Term'])
        GSEA_list.extend(mesh_tar)
    
    target_union_vector = pd.DataFrame(list(set(GSEA_list)))
    # #na와 nan이 포함되어 있음
    target_union_vector = target_union_vector.sort_values(0)
    
    # 해당 excel 파일의 0 column을 index로 만들면 vectorization 준비 완료!
    target_union_vector.to_excel('com_'+str(GSEA_type[j])+'_union_vector.xlsx')

