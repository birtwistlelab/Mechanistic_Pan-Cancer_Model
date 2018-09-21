import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *





np.set_printoptions(threshold=np.nan)


numcells = 30

# # NOTE - generate data
for k in range(30,50):
    # t = []
    # with open('RandomPopCells/t_' +str(k)  + '.csv', newline='') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in spamreader:
    #         x = ', '.join(row)
    #         x = x.split(',')
    #         to_append = []
    #         for item in x:
    #             to_append.append(float(item))
    #         t.append(to_append)
    # t = np.array(t)



    xoutS = []
    with open('RandomPopCells2/xoutS_' +str(k)  + '.csv', newline='') as csvfile:
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
    with open('RandomPopCells2/xoutG_' +str(k)  + '.csv', newline='') as csvfile:
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





    m=2;
    flagD=0
    STIM = np.zeros(shape = (775));
    STIM[156-1:162]=[0,0,0,0,0,0,1721];
    th=30;
    [dataS, dataG] = RunPrep()
    output = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
    np.savetxt('6B_new/t_'+str(m)+'_'+str(k)+'.csv', output[0], delimiter=',')
    np.savetxt('6B_new/xoutG_'+str(m)+'_'+str(k)+'.csv', output[1], delimiter=',')
    np.savetxt('6B_new/xoutS_'+str(m)+'_'+str(k)+'.csv', output[2], delimiter=',')
    #
    # % INS only
    # STIM=zeros(NumSpecies,1);
    # STIM(156:162)=[0,0,0,0,0,0,1721];
    # Run_SimCells(STIM,th,'CellCycle2S_I')
    #
