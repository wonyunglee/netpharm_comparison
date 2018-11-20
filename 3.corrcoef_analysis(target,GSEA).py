# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:53:03 2017

@author: Administrator
"""
import pandas as pd
import re
import os
import numpy as np

os.chdir(r'C:\Users\Administrator\Desktop\netpharm_platform_comparison\compound_inconsistency\2.res_vector')

# target, GSEA result의 vector를 pearson's corrcoef 분석으로 
# 각 본초의 상관성을 분석해줌

anal_tar = ['target','GO','KEGG','OMIM']

for x in range(4):
# target, GSEA result에 대해 각 platform의 분석결과 가져와서 합침
    TCMSP_mat = pd.read_excel('comTCMSP_'+str(anal_tar[x])+'_vector.xlsx')
    BATMAN_mat = pd.read_excel('comBATMAN_'+str(anal_tar[x])+'_vector.xlsx')
    mesh_mat = pd.read_excel('commesh_'+str(anal_tar[x])+'_vector.xlsx')
    concat_mat = pd.concat([TCMSP_mat,BATMAN_mat,mesh_mat], axis=1)
    concat_mat = concat_mat.T

    # 분석 후 TCMSPvs.BATMAN (0:100/100:200) / BATMANvs.mesh(100:200/200:300) / 
    #    mesh vs. TCMSP(200:300/0:100) 분할 후 저
#      각 matrix가 74*74임에 주의!
    
    corr_mat = pd.DataFrame(np.corrcoef(concat_mat))
    corr_mat.to_excel('corr_com_'+str(anal_tar[x]+'.xlsx'))
    TCMSP_BATMAN = pd.DataFrame(np.array(corr_mat.iloc[0:74,74:148]))
    TCMSP_BATMAN.to_excel('corr_com_TCMSP_BATMAN_'+str(anal_tar[x])+'.xlsx')
    BATMAN_mesh = pd.DataFrame(np.array(corr_mat.iloc[74:148,148:222]))
    BATMAN_mesh.to_excel('corr_com_BATMAN_mesh_'+str(anal_tar[x])+'.xlsx')
    TCMSP_BATMAN = pd.DataFrame(np.array(corr_mat.iloc[148:222,0:74]))
    TCMSP_BATMAN.to_excel('corr_com_mesh_TCMSP_'+str(anal_tar[x])+'.xlsx')
