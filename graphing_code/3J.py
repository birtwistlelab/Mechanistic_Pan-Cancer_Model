import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *

from matplotlib.font_manager import FontProperties


np.set_printoptions(threshold=sys.maxsize)


# read in files
# kTCleak = []
# with open('initialized/i_kTCleakF.txt', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         x = ', '.join(row)
#         x = x.split(',')
#
#         to_append = []
#         for item in x:
#             to_append.append(float(item))
#
#         kTCleak.append(to_append)
#
# kTCleak = np.array(kTCleak)
#
# kTCmaxs = []
# with open('initialized/i_kTCmaxsF.txt', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         x = ', '.join(row)
#         x = x.split(',')
#
#         to_append = []
#         for item in x:
#             to_append.append(float(item))
#
#         kTCmaxs.append(to_append)
#
# kTCmaxs = np.array(kTCmaxs)








# # %% Figure 3J
# # % Dynamics of Cell Cycle Proteins
# #
#
#
# # NOTE - generating data



# STIM = np.zeros(shape = (775));
# th=96;
# flagD=1;
#
#
m=[1,10,60];
#
# for i in range(len(m)):
#
#     # redundant but get weird results if i don't include this in every loop
#     [dataS, dataG] = RunPrep()
#     dataS_up=dataS;
#     dataG_up=dataG;
#
#     dataG_up.kTCleak=kTCleak;
#     dataG_up.kTCmaxs=kTCmaxs;
#
#     dataG_up.kTCleak[10-1:12]=0;
#     dataG_up.kTCmaxs[10-1:12]=0;
#     dataG_up.kTCd[10-1:12]=0;
#
#     xoutG=dataG.x0gm_mpc_D;
#     xoutG_up=xoutG;
#
#     xoutG_up[292-1:294]=xoutG[292-1:294]*m[i];
#
#
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], xoutG_up, dataS_up, dataG_up, dataG_up.kTCleak, dataG_up.kTCmaxs)
#
#     np.savetxt('3J_output/t_'+str(i)+'.csv', t, delimiter=',')
#     np.savetxt('3J_output/xoutG_'+str(i)+'.csv', xoutG, delimiter=',')
#     np.savetxt('3J_output/xoutS_'+str(i)+'.csv', xoutS, delimiter=',')
#
#
#
# sys.exit("data generation done")


# plotting data


sp=[46-1,50-1,59-1,69-1]; #Cyclin D, E, A, and B, active.

# f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=False, sharey=False)


# for k in range(len(sp)):



f = plt.figure()
colors_array = ['b','r','g']
labels = ["Basal Cyclin D mRNA x 1","x 30","x 60"]
legend_array=[]
k=2

for i in range(len(m)):


    t = []
    with open('3J_output/t_' + str(i)  + '.csv', newline='') as csvfile:
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
    with open('3J_output/xoutS_' + str(i)  + '.csv', newline='') as csvfile:
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

    y = xoutS[:,sp[k]]



    if k==0:
        # line1, = ax.plot(x, y, color=colors_array[i-1])
        line1, = plt.plot(x, y, color=colors_array[i],label=labels[i])
        plt.yticks([0,40,80,120])

        plt.xticks([0,24,48,72,96])
        legend_array.append(line1)



    if k==1:
        # line1, = ax.plot(x, y, color=colors_array[i-1])
        line1, = plt.plot(x, y, color=colors_array[i],label=labels[i])
        plt.yticks([0,20,40])
        plt.xticks([0,24,48,72,96])
        legend_array.append(line1)

    if k==2:
        # line1, = ax.plot(x, y, color=colors_array[i-1])
        line1, = plt.plot(x, y, color=colors_array[i],label=labels[i])
        plt.yticks([0,20,40])
        plt.xticks([0,24,48,72,96])
        legend_array.append(line1)

    if k==3:
        # line1, = ax.plot(x, y, color=colors_array[i-1])
        line1, = plt.plot(x, y, color=colors_array[i],label=labels[i])
        plt.yticks([0,20,40])
        plt.xticks([0,24,48,72,96])
        legend_array.append(line1)


        # ax.set_ylabel('[cPARP]')
        # ax.set_xlabel('Time (hours)')



plt.legend(handles=legend_array)
plt.legend(loc=1)

plt.ylabel('[CYCA*]')
plt.xlabel('Time (hours)')

f.savefig("3J_output/3Jfig_"+str(k)+".pdf")



# %% Figure 3J
# % Dynamics of Cell Cycle Proteins
#
#
# % IMPORT DATA
# St=load(strcat(matpath,'CellCycle1D.mat'));
# conds=St.conds;
#
# sp=[46,50,59,69]; %Cyclin D, E, A, and B, active.
# a=figure;
# for k=1:length(sp)
# subplot(2,2,k)
# for i=1:length(conds)-1
#     x=conds{i}.tout_all/3600;
#     y=conds{i}.xoutS_all(:,sp(k));
#     plot(x,y,'Color',colororder(i,:))
#     axis tight
#     xlim([0 max(x)])
#     set(gca,'XTick',[0:24:96])
#     hold on
# end
#     if k==1; set(gca,'YTick',0:40:120); end
#     if k==2; set(gca,'YTick',0:20:60); end
# end
