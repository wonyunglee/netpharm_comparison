# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:11:15 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:48:27 2017

@author: Yung
"""
# 현재 chem_list의 data 문제로 100% conversion이 안되는듯 (아니면 중복된 inchikey가 있나?)

import pandas as pd
import re
import os
import numpy as np



os.chdir (r'C:\Users\Administrator\Desktop\netpharm_platform_comparison\compound_inconsistency\compound_tar_GSEA')
# 해당 폴더에 아래 BATMAN_CT_names(BATMAN에서 다운받은 target prediction 파일)이 있어야 하고
# 아래 두 파일 역시 해당 폴더에 저장됨

#targete vectorization
# mesh는 target이 없는 본초가 있음 / BATMAN은 index gene symbol

target_vector = pd.read_excel("com_tar_union_vector.xlsx")
platforms = ['TCMSP','BATMAN','mesh']
for j in range(3):
    matrix = np.zeros((len(target_vector),74))
    chem_info = pd.DataFrame(matrix, index=list(target_vector[0]))
    
    # 파일을 하나씩 불러오기
    for i in range(74):
        target = pd.read_excel(str(i)+'_com_'+str(platforms[j])+'_tar(adme).xlsx')
        # TCMSP(csv) : *_compound  / BATMAN(xlsx) : *_CT_tabe / mesh(xlsx) : *_mesh_ingredient
        
        if list(target) != []:
            tar_list = list(target['target'])
    
            for z in range(len(tar_list)):
                chem_info.loc[tar_list[z]][i] = 1
    
    chem_info.to_excel('com_'+str(platforms[j])+'_target_vector.xlsx')      
    
# GSEA vectorization

GSEAs = ['GO','KEGG','OMIM']
for x in range(3):
    
    GSEA_vector = pd.read_excel('com_'+str(GSEAs[x])+"_union_vector.xlsx")
    platforms = ['TCMSP','BATMAN','mesh']
    
    for j in range(3):
        matrix = np.zeros((len(GSEA_vector),74))
        chem_info = pd.DataFrame(matrix, index=list(GSEA_vector[0]))
        
        # 파일을 하나씩 불러오기
        for i in range(74):
            target = pd.read_excel(str(i)+'_com_'+str(platforms[j])+'_'+str(GSEAs[x])+'(adme).xlsx')
            
            if list(target) != []:
                tar_list = list(target['Term'])
        
                for z in range(len(tar_list)):
                    chem_info.loc[tar_list[z]][i] = 1
        
        chem_info.to_excel('com'+str(platforms[j])+'_'+str(GSEAs[x])+'_vector.xlsx')      
        