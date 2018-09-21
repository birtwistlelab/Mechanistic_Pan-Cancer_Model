import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *





np.set_printoptions(threshold=np.nan)


numcells = 10
flagD = 0

# for k in range(0,10):
#
#
#
#     t = []
#     with open('RandomPopCells/t_' +str(k)  + '.csv', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         for row in spamreader:
#             x = ', '.join(row)
#             x = x.split(',')
#
#             to_append = []
#             for item in x:
#                 to_append.append(float(item))
#
#             t.append(to_append)
#
#     t = np.array(t)
#
#
#
#     xoutS = []
#     with open('RandomPopCells/xoutS_' +str(k)  + '.csv', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         for row in spamreader:
#             x = ', '.join(row)
#             x = x.split(',')
#
#             to_append = []
#             for item in x:
#                 to_append.append(float(item))
#
#             xoutS.append(to_append)
#
#     xoutS = np.array(xoutS)
#
#
#     xoutG = []
#     with open('RandomPopCells/xoutG_' +str(k)  + '.csv', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         for row in spamreader:
#             x = ', '.join(row)
#             x = x.split(',')
#
#             to_append = []
#             for item in x:
#                 to_append.append(float(item))
#
#             xoutG.append(to_append)
#
#     xoutG = np.array(xoutG)
#
#     # xoutG_up = []
#     xoutS_up = np.matrix(xoutS[2880,:])
#     xoutG_up = np.matrix(xoutG[2880,:])
#     xoutG_up = np.matrix.transpose(xoutG_up)
#
#     NumSpecies=775;
#
#
#     m=1; #NO STIM
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[0,0,0,0,0,0,0]; #ligs
#     STIM[769-1]=0; #MEKi
#     STIM[771-1]=0; #AKTi
#     th=80;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('5A_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('5A_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('5A_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#
#     # % Effect of inhibitors and GFs, TRAIL dose response in SS state.
#     # m=1; %NO STIM
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[0,0,0,0,0,0,0]; %ligs
#     # STIM(769)=0; %MEKi
#     # STIM(771)=0; %AKTi
#     # th=80;
#     # filename=strcat('Apoptosis2S_',num2str(m));
#     # Run_SimCells(STIM,th,filename)
#     #
#
#     m=2;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[3.3,0,0,0,0,0,1721]; #ligs
#     STIM[769-1]=0; #MEKi
#     STIM[771-1]=0; #AKTi
#     th=80;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('5A_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('5A_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('5A_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#
#
#     # m=2;
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[3.3,0,0,0,0,0,1721]; %ligs
#     # STIM(769)=0; %MEKi
#     # STIM(771)=0; %AKTi
#     # th=80;
#     # filename=strcat('Apoptosis2S_',num2str(m));
#     # Run_SimCells(STIM,th,filename)
#     #
#
#
#     m=3;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[3.3,0,0,0,0,0,1721]; #ligs
#     STIM[769-1]=10000; #MEKi
#     STIM[771-1]=0; #AKTi
#     th=80;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('5A_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('5A_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('5A_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#
#     # m=3;
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[3.3,0,0,0,0,0,1721]; %ligs
#     # STIM(769)=10000; %MEKi
#     # STIM(771)=0; %AKTi
#     # th=80;
#     # filename=strcat('Apoptosis2S_',num2str(m));
#     # Run_SimCells(STIM,th,filename)
#     #
#
#
    # m=4;
    # STIM = np.zeros(shape = (775));
    # STIM[156-1:162]=[3.3,0,0,0,0,0,1721]; #ligs
    # STIM[769-1]=0; #MEKi
    # STIM[771-1]=10000; #AKTi
    # th=80;
    # [dataS, dataG] = RunPrep()
    # [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
    # np.savetxt('5A4_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
    # np.savetxt('5A4_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
    # np.savetxt('5A4_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#     # m=4;
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[3.3,0,0,0,0,0,1721]; %ligs
#     # STIM(769)=0; %MEKi
#     # STIM(771)=10000; %AKTi
#     # th=80;
#     # filename=strcat('Apoptosis2S_',num2str(m));
#     # Run_SimCells(STIM,th,filename)
#     #
#
#     m=5;
#     STIM = np.zeros(shape = (775));
#     STIM[156-1:162]=[3.3,0,0,0,0,0,1721]; #ligs
#     STIM[769-1]=10000; #MEKi
#     STIM[771-1]=10000; #AKTi
#     th=80;
#     [dataS, dataG] = RunPrep()
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, [], [])
#     np.savetxt('5A_output/t_'+str(m)+'_'+str(k)+'.csv', t, delimiter=',')
#     np.savetxt('5A_output/xoutG_'+str(m)+'_'+str(k)+'.csv', xoutG, delimiter=',')
#     np.savetxt('5A_output/xoutS_'+str(m)+'_'+str(k)+'.csv', xoutS, delimiter=',')
#     # m=5;
#     # STIM=zeros(NumSpecies,1);
#     # STIM(156:162)=[3.3,0,0,0,0,0,1721]; %ligs
#     # STIM(769)=10000; %MEKi
#     # STIM(771)=10000; %AKTi
#     # th=80;
#     # filename=strcat('Apoptosis2S_',num2str(m));
#     # Run_SimCells(STIM,th,filename)
#
#
#
# sys.exit("data generation done")


# TODO - debugging, delete

# xoutS = []
# with open('5A_output/xoutS_'+str(1)+'_'+str(0)+'.csv', newline='') as csvfile:
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
# xoutS1 = np.array(xoutS)
#
#
#
# xoutS = []
# with open('5A_output/xoutS_'+str(5)+'_'+str(0)+'.csv', newline='') as csvfile:
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
# xoutS2 = np.array(xoutS)
#
#
# print(xoutS1[100:110,59-1])
# print()
# print(xoutS2[100:110,59-1])
#
# sys.exit("debugging")


numcells = 30
f, (ax1, ax2, ax3,ax4,ax5) = plt.subplots(5, sharex=False, sharey=False)


# f = plt.figure()


# for m in range(4,5):
for m in range(1,6):

    # f = plt.figure()

    ttd = np.zeros(shape = (numcells));


    # for k in range(numcells):
    for k in range(numcells):


        t = []
        with open('5A_output/t_'+str(m)+'_'+str(k)+'.csv', newline='') as csvfile:
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
        with open('5A_output/xoutS_'+str(m)+'_'+str(k)+'.csv', newline='') as csvfile:
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


        t = np.array(t_new)/3600
        xoutS = np.array(xoutS_new)


        ind2plot=[59-1]; #cycA

        y = xoutS[:,106-1]



        if m==1:
            line, = ax1.plot(t, y)
            ax1.set_yticks([0,200,400])
            ax1.set_xticks([0,20,40,60,80])

        if m==2:
            line, = ax2.plot(t, y)
            ax2.set_yticks([0,200,400])
            ax2.set_xticks([0,20,40,60,80])

        if m==3:
            line, = ax3.plot(t, y)
            ax3.set_yticks([0,200,400])
            ax3.set_xticks([0,20,40,60,80])
        if m==4:
            line, = ax4.plot(t, y)
            ax4.set_yticks([0,200,400])
            ax4.set_xticks([0,20,40,60,80])
        if m==5:
            line, = ax5.plot(t, y)
            ax5.set_yticks([0,200,400])
            ax5.set_xticks([0,20,40,60,80])




        # % Calc ttd
        # time=find(xoutS_all(:,106)>100);
        # if ~isempty(time)
        #     ttds(n,k)=tout_all(min(time));
        # else ttds(n,k)=Inf;
        # end
        # end


        # calc TTD
    #     time = np.where(xoutS[:,106-1]>100)[0]
    #
    #
    #
    #     if time.size>0:
    #         # ttd[k] = t[min(time)]/3600
    #         ttd[k] = t[min(time)]
    #
    #
    #         print(k)
    #         # print(t[min(time)]/3600)
    #         print(t[min(time)])
    #
    #         print()
    #
    #
    #
    #
    # to_graph = []
    #
    #
    # # 24h
    # count = 0
    # for item in ttd:
    #     if item>0 and item<24:
    #         count = count+1
    # to_graph.append(count/numcells*100)
    #
    # # 48h
    # count = 0
    # for item in ttd:
    #     if item>0 and item<48:
    #         count = count+1
    # to_graph.append(count/numcells*100)
    #
    # # 72h
    # count = 0
    # for item in ttd:
    #     if item>0 and item<72:
    #         count = count+1
    # to_graph.append(count/numcells*100)
    #
    #
    # # make bar graph
    #
    #
    #
    #
    # objects = ("24h","48h","72h")
    # y_pos = np.arange(len(objects))
    # performance = to_graph
    #
    # plt.bar(y_pos, performance, align='center', alpha=0.5)
    # plt.xticks(y_pos, objects)
    # plt.yticks([0,25,50,75,100])
    #
    # plt.ylabel('Percent Death')
    # plt.xlabel('Time')
    #
    # # plt.title('Cells without Growth Factors')
    #
    # # plt.show()
    #
    #
    # f.savefig("new_5A_output/new_bar_graph " + str(m)+".pdf")

# plt.show()
f.savefig("5A_output/new_plot_for_real_this_time.pdf")



sys.exit("plot done")



##### plot matlab


m = 5

ttd = np.array([15,20,22,23,35,41,46,47,51,56])


to_graph = []
# 24h
count = 0
for item in ttd:
    if item>0 and item<24:
        count = count+1
to_graph.append(count/numcells*100)

# 48h
count = 0
for item in ttd:
    if item>0 and item<48:
        count = count+1
to_graph.append(count/numcells*100)

# 72h
count = 0
for item in ttd:
    if item>0 and item<72:
        count = count+1
to_graph.append(count/numcells*100)


# make bar graph




objects = ("24h","48h","72h")
y_pos = np.arange(len(objects))
performance = to_graph

plt.bar(y_pos, performance, align='center', alpha=0.5, color='g')
plt.xticks(y_pos, objects)
plt.yticks([0,25,50,75,100])

plt.ylabel('Percent Death')
plt.xlabel('Time')

# plt.title('Cells without Growth Factors')

# plt.show()


f.savefig("5A_output/matlab_bar_graph " + str(m)+".pdf")
