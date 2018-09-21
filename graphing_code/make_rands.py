import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *



np.set_printoptions(threshold=np.nan)


flagD=0;
th=24;
STIM = np.zeros(shape = (775));


numcells = 10


for i in range(30,50):

    # redundant but get weird results if i don't include this in every loop
    [dataS, dataG] = RunPrep()

    [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, [], [])

    np.savetxt('RandomPopCells2/t_'+str(i)+'.csv', t, delimiter=',')
    np.savetxt('RandomPopCells2/xoutG_'+str(i)+'.csv', xoutG, delimiter=',')
    np.savetxt('RandomPopCells2/xoutS_'+str(i)+'.csv', xoutS, delimiter=',')
