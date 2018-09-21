import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *


np.set_printoptions(threshold=np.nan)


# # Add trail to system
#
#
STIM = np.zeros(shape = (775));
STIM [84-1] = 0.005; #TRAIL, low dose
#
#
# # 1
#
# # # No other stim (baseline)
# # # [tout_all1,xoutG_all1,xoutS_all1]=RunModel(1,100,STIM,[],[],[],[]);
flagD = 1
th = 100
# [dataS, dataG] = RunPrep()
# dataS_up = dataS
# [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, [], [])
#
#
# np.savetxt('3I_output2/t1.csv', t, delimiter=',')
# np.savetxt('3I_output2/xoutG1.csv', xoutG, delimiter=',')
# np.savetxt('3I_output2/xoutS1.csv', xoutS, delimiter=',')
#
#
#
#
#
#
#
#
#
#
# # 2
#
# # No pptases for pERK and pAKT
# [dataS, dataG] = RunPrep()
# dataS_up=dataS;
#
#
# # dataS_up.kS[1046-1]=0;
# # dataS_up.kS[1047-1]=0;
# # dataS_up.kS[1049-1]=0;
# # dataS_up.kS[1050-1]=0;
# # dataS_up.kS[988-1]=0;
# # dataS_up.kS[992-1]=0;
#
# dataS_up.kS[910-1] = dataS.kS[910-1]*10
# dataS_up.kS[913-1] = dataS.kS[913-1]*10
# dataS_up.kS[991-1] = dataS.kS[991-1]*10
# dataS_up.kS[995-1] = dataS.kS[995-1]*10
#
#
# [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, [], [])
#
#
# np.savetxt('3I_output2/t2.csv', t, delimiter=',')
# np.savetxt('3I_output2/xoutG2.csv', xoutG, delimiter=',')
# np.savetxt('3I_output2/xoutS2.csv', xoutS, delimiter=',')
# #
# #
# #
# #
# #
# #
# #
# #
# # 3
#
# # Add puma and noxa
# [dataS, dataG] = RunPrep()
# dataS_up=dataS;
# xoutG=dataG.x0gm_mpc_D;
# # xoutG[335-1:336]=xoutG[335-1:336]*16; #Add mRNA for PUMA and NOXA
# xoutG[335-1:336]=xoutG[335-1:336]*20; #Add mRNA for PUMA and NOXA
#
# #dataS_up.mExp_nM(53:54)=dataS_up.mExp_nM(53:54)*1000; %Add mRNA for PUMA and NOXA
# [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], xoutG, dataS_up, dataG, [], [])
#
# np.savetxt('3I_output2/t3.csv', t, delimiter=',')
# np.savetxt('3I_output2/xoutG3.csv', xoutG, delimiter=',')
# np.savetxt('3I_output2/xoutS3.csv', xoutS, delimiter=',')
#
#
#
# sys.exit("done data generation")


# NOTE - plot data



fig,ax = plt.subplots()

colors_array=['r','b','g']

for i in range(1,4):




    xoutG = []
    with open('3I_output2/xoutG'+ str(i)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutG.append(to_append)

    xoutG = np.array(xoutG)









    t = []
    with open('3I_output2/t' + str(i)  + '.csv', newline='') as csvfile:
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
    with open('3I_output2/xoutS' + str(i)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutS.append(to_append)

    xoutS = np.array(xoutS)




    x = t/3600

    y = xoutS[:,106-1]

    print(y.shape)



    line1, = ax.plot(x, y, color=colors_array[i-1])

    plt.xticks([0,10,20,30,40,50,60])


    ax.set_ylabel('[cPARP]')
    ax.set_xlabel('Time (hours)')


plt.savefig('3I_output/plot3.pdf')
