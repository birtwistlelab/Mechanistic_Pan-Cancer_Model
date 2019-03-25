# 4A GFs


import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *

from scipy.signal import *

import peakutils



np.set_printoptions(threshold=sys.maxsize)


numcells = 30

flagD=0;




# NOTE - GFs
for k in range(25,30):

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
    STIM1 = np.zeros(shape = (775));
    STIM1[156-1:162]=[3.3,0,0,0,0,0,1721]; #ligs
    th1=72;


    th2=72;
    STIM2 = np.zeros(shape = (775));
    STIM2[775-1]=100000;
    STIM2[156-1:162]=[3.3,0,0,0,0,0,1721]; #ligs
    # Run_SimCells2(STIM1,STIM2,th1,th2,'DNADamageSerum')

    [dataS, dataG] = RunPrep()


    [t, xoutG_out, xoutS_out] = RunModel(flagD, th1, STIM1, xoutS_up, xoutG_up, dataS, dataG, [], [])

    # np.savetxt('4A_output/gfs/t_'+str(k)+'_1.csv', t, delimiter=',')
    # np.savetxt('4A_output/gfs/xoutG_'+str(k)+'_1.csv', xoutG, delimiter=',')
    # np.savetxt('4A_output/gfs/xoutS_'+str(k)+'_1.csv', xoutS, delimiter=',')



    xoutS_up2 = np.matrix(xoutS_out[xoutS_out.shape[0]-1,:])
    xoutG_up2 = np.matrix(xoutG_out[xoutG_out.shape[0]-1,:])
    xoutG_up2 = np.matrix.transpose(xoutG_up2)




    [dataS, dataG] = RunPrep()
    [t, xoutG, xoutS] = RunModel(flagD, th2, STIM2, xoutS_up2, xoutG_up2, dataS, dataG, [], [])

    np.savetxt('4A_output/gfs/t_'+str(k)+'_2.csv', t, delimiter=',')
    # np.savetxt('4A_output/gfs/xoutG_'+str(k)+'_2.csv', xoutG, delimiter=',')
    np.savetxt('4A_output/gfs/xoutS_'+str(k)+'_2.csv', xoutS, delimiter=',')
