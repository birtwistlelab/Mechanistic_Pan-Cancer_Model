# 4A No GFs


import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *

from scipy.signal import *

import peakutils



np.set_printoptions(threshold=np.nan)


numcells = 60

flagD=0;




# NOTE - No GFs
for k in range(0,numcells):

    t = []
    with open('RandomPopCells/t_' +str(k)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            t.append(to_append)

    t = np.array(t)



    xoutS = []
    with open('RandomPopCells/xoutS_' +str(k)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutS.append(to_append)

    xoutS = np.array(xoutS)


    xoutG = []
    with open('RandomPopCells/xoutG_' +str(k)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutG.append(to_append)

    xoutG = np.array(xoutG)

    # xoutG_up = []
    xoutS_up = np.matrix(xoutS[2880,:])
    xoutG_up = np.matrix(xoutG[2880,:])
    xoutG_up = np.matrix.transpose(xoutG_up)

    NumSpecies=775;

    # % WITH GFs

    th=72;
    STIM = np.zeros(shape = (775));
    STIM[775-1]=100000;
    STIM[156-1:162]=[0,0,0,0,0,0,0];

    # Run_SimCells2(STIM1,STIM2,th1,th2,'DNADamageSerum')

    [dataS, dataG] = RunPrep()

    [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])


    np.savetxt('4A_output/no_gfs/t_'+str(k)+'_1.csv', t, delimiter=',')
    np.savetxt('4A_output/no_gfs/xoutG_'+str(k)+'_1.csv', xoutG, delimiter=',')
    np.savetxt('4A_output/no_gfs/xoutS_'+str(k)+'_1.csv', xoutS, delimiter=',')
