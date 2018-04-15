# figure 3 replication

import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *


np.set_printoptions(threshold=np.nan)

# TODO
# 3B - ERK
# 3E - p53
# 3G (left; cPARP dynamics),
# 3J (cell cycle dynamics)





# [dataS, dataG] = RunPrep()
# flagD = 0
# th = 24
# xoutS = []
# xoutG = []
# STIM= np.zeros(shape = (775));
# #
# out = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)

[dataS, dataG] = RunPrep()




condsD = []

for k in range(1,4):
    STIMS= np.zeros(shape = (775,4));
    indegf=156-1;
    indins=162-1;

    if k == 1:
        STIMS[indegf,0]=0.01;
        STIMS[indegf,1]=0.1;
        STIMS[indegf,2]=1;
        STIMS[indegf,3]=10;

    if k==2:
        STIMS[indins,0]=0.17;
        STIMS[indins,1]=1.7;
        STIMS[indins,2]=17;
        STIMS[indins,3]=1721;

    if k==3:
        STIMS[[indegf,indins],0]=[0.01,0.17];
        STIMS[[indegf,indins],1]=[0.01,1721];
        STIMS[[indegf,indins],2]=[10,0.17];
        STIMS[[indegf,indins],3]=[10,1721];


    th=6;
    flagD=1;
    condsD=[];




    for i in range(0,4):
        STIM=STIMS[:,i];
        [t,xoutG,xoutS]=RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
        np.savetxt('fig3_output/t' + '_' + str(k) + '_' + str(i) + '.csv', t, delimiter=',')
        np.savetxt('fig3_output/xoutG' + '_' + str(k) + '_' + str(i) + '.csv', xoutG, delimiter=',')
        np.savetxt('fig3_output/xoutS' + '_' + str(k) + '_' + str(i) + '.csv', xoutS, delimiter=',')


# %% Figure 3B-D
# % pERK, pAKT, p4EBP1 Dynamics
#
# condsD=[];
# for k=1:3
# STIMS=zeros(775,4);
# indegf=156;
# indins=162;
# if k==1
# STIMS(indegf,1)=0.01;
# STIMS(indegf,2)=0.1;
# STIMS(indegf,3)=1;
# STIMS(indegf,4)=10;
# end
# if k==2
# STIMS(indins,1)=0.17;
# STIMS(indins,2)=1.7;
# STIMS(indins,3)=17;
# STIMS(indins,4)=1721;
# end
# if k==3
# STIMS([indegf,indins],1)=[0.01,0.17];
# STIMS([indegf,indins],2)=[0.01,1721];
# STIMS([indegf,indins],3)=[10,0.17];
# STIMS([indegf,indins],4)=[10,1721];
# end


# th=6;
# flagD=1;
# condsD=[];
# for i=1:size(STIMS,2)
#     STIM=STIMS(:,i);
    # [tout_all,xoutG_all,xoutS_all]=RunModel(flagD,th,STIM,[],[],[],[]);
#     D.tout_all=tout_all;
#     D.xoutG_all=xoutG_all;
#     D.xoutS_all=xoutS_all;
#     condsD{i}=D;
#     disp(i)
#
# end
# txt=strcat(matpath,'GFdoseresponse1D_EI_',num2str(k),'.mat');
# save(txt,'-v7.3','condsD');
# end





















#
# %% Figure 3B-D
# % pERK, pAKT, p4EBP1 Dynamics
#
# condsD=[];
# for k=1:3
# STIMS=zeros(775,4);
# indegf=156;
# indins=162;
# if k==1
# STIMS(indegf,1)=0.01;
# STIMS(indegf,2)=0.1;
# STIMS(indegf,3)=1;
# STIMS(indegf,4)=10;
# end
# if k==2
# STIMS(indins,1)=0.17;
# STIMS(indins,2)=1.7;
# STIMS(indins,3)=17;
# STIMS(indins,4)=1721;
# end
# if k==3
# STIMS([indegf,indins],1)=[0.01,0.17];
# STIMS([indegf,indins],2)=[0.01,1721];
# STIMS([indegf,indins],3)=[10,0.17];
# STIMS([indegf,indins],4)=[10,1721];
# end
#
# th=6;
# flagD=1;
# condsD=[];
# for i=1:size(STIMS,2)
#     STIM=STIMS(:,i);
#     [tout_all,xoutG_all,xoutS_all]=RunModel(flagD,th,STIM,[],[],[],[]);
#     D.tout_all=tout_all;
#     D.xoutG_all=xoutG_all;
#     D.xoutS_all=xoutS_all;
#     condsD{i}=D;
#     disp(i)
#
# end
# txt=strcat(matpath,'GFdoseresponse1D_EI_',num2str(k),'.mat');
# save(txt,'-v7.3','condsD');
# end
