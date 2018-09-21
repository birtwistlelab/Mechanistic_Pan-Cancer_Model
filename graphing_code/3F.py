import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *

from scipy.signal import *

import peakutils



np.set_printoptions(threshold=np.nan)



# Figure 3F
# Stochastic DNA Damage Unit Testing



# NOTE - data generation ready, plotting not ready

damages=[1, 4, 10, 25];
#
# th = 30
# flagD = 0
#
#
# for i in range(len(damages)):
#
#     [dataS, dataG] = RunPrep()
#     dataS_up = dataS
#
#     dataS_up.kS[699-1] = 0
#     dataS_up.kS[701-1] = 0
#
#
#     STIM = np.zeros(shape = (775));
#     STIM[31-1] = damages[i]
#
#
#     for k in range(5):
#
#         [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, [], [])
#
#
#         inds = []
#         z = 0
#         while z < len(t):
#             inds.append(z)
#             z = z+10
#
#         np.savetxt('3F_output/t_'+str(i)+'_'+str(k)+'.csv', t[inds], delimiter=',')
#         np.savetxt('3F_output/xoutS_'+str(i)+'_'+str(k)+'.csv', xoutS[inds,:], delimiter=',')
#
#
# sys.exit("data generation done")
#
#
#
#
#
#
# # plotting
#
# peak_matrix = np.zeros(shape = (len(damages),5));
#
#
# for i in range(len(damages)):
#
#     for k in range(5):
#
#         t = []
#         with open('3F_output/t_' + str(i)+'_'+str(k)  + '.csv', newline='') as csvfile:
#             spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in spamreader:
#                 x = ', '.join(row)
#                 x = x.split(',')
#
#                 to_append = []
#                 for item in x:
#                     to_append.append(float(item))
#
#                 t.append(to_append)
#
#         t = np.array(t)
#
#
#
#         xoutS = []
#         with open('3F_output/xoutS_' + str(i) +'_'+str(k)  + '.csv', newline='') as csvfile:
#             spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in spamreader:
#                 x = ', '.join(row)
#                 x = x.split(',')
#
#                 to_append = []
#                 for item in x:
#                     to_append.append(float(item))
#
#                 xoutS.append(to_append)
#
#         xoutS = np.array(xoutS)
#
#
#         xoutIN = xoutS[:,3-1]
#
#         tout = t/3600
#
#         # peak_inds = find_peaks_cwt(xoutIN, tout)
#
#         peak_inds = peakutils.indexes(xoutIN, thres=0.02/max(xoutIN), min_dist=5)
#
#         print(peak_inds)
#         sys.exit()
#         # np.savetxt('3F_output/peak_'+str(i)+'_'+str(k)+'.csv', peak_inds, delimiter=',')
#         # TODO - need to save these in matrix
#
#
#         damages[i] = xoutS[1-1,31-1]




# %% Figure 3F
# % Stochastic DNA Damage Unit Testing (Bar Plots)
#
# % Get Data
# St=load(strcat(matpath,'DNADamage1S.mat'));
# cells=St.cells;
# for i=1:size(cells,1)
#     for k=1:size(cells,2)
#         xoutIN=cells{i,k}.xoutS_all(:,3);
#         tout=cells{i,k}.tout_all/3600;
#         [pks,locs,w]=findpeaks(xoutIN,tout,'MinPeakHeight',400,'MinPeakDistance',5);
#         peaks{i,k}=[pks,w];
#     end
#     damages(i)=cells{i,k}.xoutS_all(1,31);
# end
#
# % Plot box plots
# for i=1:size(peaks,1)
#     avar=[];
#     for k=1:size(peaks,2) %Cells
#         avar(k,:)=mean(peaks{i,k},1);
#         np(k)=length(peaks{i,k}(:,1));
#     end
#     hei(:,i)=avar(:,1);
#     wid(:,i)=avar(:,2);
#     nps(:,i)=np;
# end
# b2=figure; errorbar(damages,mean(nps),std(nps),'-sk','MarkerSize',5,'MarkerFaceColor','k'); set(gca,'XTick',damages); xlim([min(damages),max(damages)]);
# b3=figure; errorbar(damages,mean(hei),std(hei),'-sk','MarkerSize',5,'MarkerFaceColor','k'); set(gca,'XTick',damages); xlim([min(damages),max(damages)]); ylim([0 1500])
# b4=figure; errorbar(damages,mean(wid),std(wid),'-sk','MarkerSize',5,'MarkerFaceColor','k'); set(gca,'XTick',damages); xlim([min(damages),max(damages)]); ylim([0 5])









# NOTE - plot


f, (ax1, ax2, ax3,ax4) = plt.subplots(4, sharex=False, sharey=False)

for i in range(len(damages)):

    for k in range(5):

        t = []
        with open('3F_output/t_' + str(i)+'_'+str(k)  + '.csv', newline='') as csvfile:
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
        with open('3F_output/xoutS_' + str(i) +'_'+str(k)  + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)


        y = xoutS[:,3-1]

        # tout = t/3600



        if i==0:
            line, = ax1.plot(t/3600, y)
            ax1.set_yticks([0,5,10,15,20])
            ax1.set_xticks([0,6,12,18,24,30])


        if i==1:
            line, = ax2.plot(t/3600, y)
            ax2.set_yticks([0,300, 600,900, 1200])
            ax2.set_xticks([0,6,12,18,24,30])

        if i==2:
            line, = ax3.plot(t/3600, y)
            ax3.set_yticks([0,300, 600,900, 1200])
            ax3.set_xticks([0,6,12,18,24,30])
        if i==3:
            line, = ax4.plot(t/3600, y)
            ax4.set_yticks([0,300, 600,900, 1200])
            ax4.set_xticks([0,6,12,18,24,30])




f.savefig("3F_output/plot.pdf")


plt.show()
