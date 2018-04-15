# replicate figures


import numpy as np
from RunPrep import *
from RunModel import *



# fig 2b

# flagD=0;
# th=24;
# STIM=zeros(NumSpecies,1);
# [tout_all,xoutG_all,xoutS_all]=RunModel(flagD,th,STIM,[],[],[],[]);
# tout_all=tout_all;
# xoutG_all=xoutG_all;
# xoutS_all=xoutS_all;

#
[dataS, dataG] = RunPrep()
flagD = 0
th = 24
xoutS = []
xoutG = []
STIM= np.zeros(shape = (775));
#
out = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
t = out[0]
xoutG = out[1]
xoutS = out[2]
#
# print(len(t))
# print(len(xoutG))
# print(len(xoutS))
#
#
# # NOTE - save to csv
np.savetxt('figs_output/t4.csv', t, delimiter=',')
np.savetxt('figs_output/xoutG4.csv', xoutG, delimiter=',')
np.savetxt('figs_output/xoutS4.csv', xoutS, delimiter=',')


sys.exit()

numcells=100;
# filename='RandomPopCells_100cells.mat';
# RunRandomPopCells(numcells,filename)


# cells0=[];
# flagD=0;
# th=24;
# STIM=zeros(775,1);


to_save = np.zeros(shape=(numcells))

for i in range(numcells):
    out = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)

    t = out[0]
    xoutG = out[1]
    xoutS = out[2]

    temp = np.zeros(shape=(3))






# for i=1:numcells
#     [tout_all,xoutG_all,xoutS_all]=RunModel(flagD,th,STIM,[],[],[],[]);
#     C.tout_all=tout_all;
#     C.xoutG_all=xoutG_all(end,:);
#     C.xoutS_all=xoutS_all(end,:);
#     cells0{i}=C;
#     disp(i)
# end
#
# if exist('filename','var')
#     save(filename,'-v7.3','cells0');
# else
#     save('RandomPopCells.mat','-v7.3','cells0');
# end













print("done")
