import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *





np.set_printoptions(threshold=np.nan)


# numcells = 10
# flagD = 0
#
#
#
# # # NOTE - generate data
# for k in range(numcells):
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
    #
    #
    #
    # xoutS = []
    # with open('RandomPopCells/xoutS_' +str(k)  + '.csv', newline='') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in spamreader:
    #         x = ', '.join(row)
    #         x = x.split(',')
    #
    #         to_append = []
    #         for item in x:
    #             to_append.append(float(item))
    #
    #         xoutS.append(to_append)
    #
    # xoutS = np.array(xoutS)
    #
    #
    # xoutG = []
    # with open('RandomPopCells/xoutG_' +str(k)  + '.csv', newline='') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in spamreader:
    #         x = ', '.join(row)
    #         x = x.split(',')
    #
    #         to_append = []
    #         for item in x:
    #             to_append.append(float(item))
    #
    #         xoutG.append(to_append)
    #
    # xoutG = np.array(xoutG)
    #
    # # xoutG_up = []
    # xoutS_up = np.matrix(xoutS[2880,:])
    # xoutG_up = np.matrix(xoutG[2880,:])
    # xoutG_up = np.matrix.transpose(xoutG_up)
#
#     NumSpecies=775;
#
#
#
#
#     m=1;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[10,0,0,0,0,0,0];
#     th=30;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('6B_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('6B_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('6B_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#
#
#     #
#     # % EGF only
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[10,0,0,0,0,0,0];
#     # Run_SimCells(STIM,th,'CellCycle2S_E')
#
#
#     m=2;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[0,0,0,0,0,0,1721];
#     th=30;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('6B_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('6B_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('6B_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#     #
#     # % INS only
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[0,0,0,0,0,0,1721];
#     # Run_SimCells(STIM,th,'CellCycle2S_I')
#     #
#
#
#
#     m=3;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[10,0,0,0,0,0,1721];
#     th=30;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('6B_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('6B_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('6B_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#     # % EGF+INS
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[10,0,0,0,0,0,1721];
#     # Run_SimCells(STIM,th,'CellCycle2S_E+I')
#
#
#     m=4;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[10,0,0,0,0,0,1721];
#     STIM[769-1] = 10000
#     th=30;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('6B_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('6B_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('6B_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#     # % EGF+INS+MEKi
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[10,0,0,0,0,0,1721];
#     # STIM(769)=10000;
#     # Run_SimCells(STIM,th,'CellCycle2S_E+I+MEKi')
#
#
#
#     m=5;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[10,0,0,0,0,0,1721];
#     STIM[771-1] = 10000
#     th=30;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('6B_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('6B_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('6B_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#     #
#     # % EGF+INS+AKTi
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[10,0,0,0,0,0,1721];
#     # STIM(771)=10000;
#     # Run_SimCells(STIM,th,'CellCycle2S_E+I+AKTi')
#
#
#
#
# sys.exit("generating data")


# NOTE - plot data

numcells = 30


# f, (ax1, ax2, ax3,ax4,ax5) = plt.subplots(5, sharex=False, sharey=False)


# for bar graph
to_graph = []

for m in range(1,6):
# for m in range(1,6):


    # for bar graph
    count = 0

    for k in range(numcells):
    # for k in range(1,numcells+1):

        t = []
        with open('6B_new/t_'+str(m)+'_'+str(k)+'.csv', newline='') as csvfile:
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
        with open('6B_new/xoutS_'+str(m)+'_'+str(k)+'.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)


        # condense
        i = 0
        t_new = []
        xoutS_new = []
        while i<len(t):
            t_new.append(t[i])
            xoutS_new.append(xoutS[i,:])

            i = i+30


        t = np.array(t_new)
        xoutS = np.array(xoutS_new)

        ind2plot=[59-1]; #cycA


        # plot index 59-1
        # y = xoutS[:,ind2plot]
        #
        # if m==1:
        #     line, = ax1.plot(t/3600, y)
        #     ax1.set_yticks([0,50])
        #     ax1.set_xticks([0,6,12,18,24,30])
        #
        #
        # if m==2:
        #     line, = ax2.plot(t/3600, y)
        #     ax2.set_yticks([0,50])
        #     ax2.set_xticks([0,6,12,18,24,30])
        #
        # if m==3:
        #     line, = ax3.plot(t/3600, y)
        #     ax3.set_yticks([0,50])
        #     ax3.set_xticks([0,6,12,18,24,30])
        # if m==4:
        #     line, = ax4.plot(t/3600, y)
        #     ax4.set_yticks([0,50])
        #     ax4.set_xticks([0,6,12,18,24,30])
        # if m==5:
        #     line, = ax5.plot(t/3600, y)
        #     ax5.set_yticks([0,50])
        #     ax5.set_xticks([0,6,12,18,24,30])







        # check S phase

        timeind = 96
        ind2define=[50-1,59-1,69-1]

        # print(k)


        try:
            if sum(xoutS[timeind,ind2define]) > 20:
                count = count+1
            # if sum(cells{i}.xoutS_all(timeind,ind2define))>20 %definition of S-phase, when CYCA/cdk2>XnM
        except:
            pass


    to_graph.append(count/numcells*100)


# ax1.set_title("EGF")
# ax2.set_title("INS")
# ax3.set_title("EGF+INS")
# ax4.set_title("EGF+INS+MEKi")
# ax5.set_title("EGF+INS+AKTi")







f = plt.figure()

objects = ("EGF","INS","EGF+INS","EGF+INS+MEKi","EGF+INS+AKTi")
y_pos = np.arange(len(objects))
performance = to_graph

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks([0,25,50])

plt.tick_params(labelsize=10)

plt.ylabel('Percent Proliferating Cells')
# plt.xlabel('Time (hours)')

# plt.title('Cells with Growth Factors')

# plt.show()


# f.savefig("4A_output/gfs_graph.pdf")


f.savefig("6B_new/6b_bar.pdf")
