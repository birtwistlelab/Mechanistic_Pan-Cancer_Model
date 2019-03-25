import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *



np.set_printoptions(threshold=sys.maxsize)



# NOTE -  data generation

# RunRandomPopCells

# flagD=0;
# th=24;
# STIM = np.zeros(shape = (775));

# STIM[156-1:162]=[3.3,100,100,100,100,100,1721]

numcells = 10


# for i in range(numcells):
#
#     # redundant but get weird results if i don't include this in every loop
#     [dataS, dataG] = RunPrep()
#
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
#     np.savetxt('RandomPopCells/t_'+str(i)+'.csv', t, delimiter=',')
#     np.savetxt('RandomPopCells/xoutG_'+str(i)+'.csv', xoutG, delimiter=',')
#     np.savetxt('RandomPopCells/xoutS_'+str(i)+'.csv', xoutS, delimiter=',')
#
#
#
#
#
# sys.exit("data generation done")

# NOTE - data gen with stims



traildoses=[0.0385, 0.1925, 0.385, 1.9250, 3.85, 19.25, 38.5];
STIM = np.zeros(shape = (775));


# STIM[156-1:162]=[3.3,100,100,100,100,100,1721]
#
#
# th=5;
# flagD=0;
#
# for i in range(len(traildoses)):
#     for k in range(numcells):
#
#         t = []
#         with open('RandomPopCells/t_' +str(k)  + '.csv', newline='') as csvfile:
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
#         with open('RandomPopCells/xoutS_' +str(k)  + '.csv', newline='') as csvfile:
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
#
#         xoutG = []
#         with open('RandomPopCells/xoutG_' +str(k)  + '.csv', newline='') as csvfile:
#             spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in spamreader:
#                 x = ', '.join(row)
#                 x = x.split(',')
#
#                 to_append = []
#                 for item in x:
#                     to_append.append(float(item))
#
#                 xoutG.append(to_append)
#
#         xoutG = np.array(xoutG)
#
#
#
#
#         # xoutG_up = []
#         xoutS_up = np.matrix(xoutS[2880,:])
#         xoutG_up = np.matrix(xoutG[2880,:])
#         xoutG_up = np.matrix.transpose(xoutG_up)
#
#         # sys.exit()
#
#
#
#         [dataS, dataG] = RunPrep()
#
#         STIM[84-1]=traildoses[i];
#
#
#         [t_out, xoutG_out, xoutS_out] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
#
#
#         np.savetxt('3H_output2/t_'+str(i)+'_'+str(k)+'.csv', t_out, delimiter=',')
#         np.savetxt('3H_output2/xoutG_'+str(i)+'_'+str(k)+'.csv', xoutG_out, delimiter=',')
#         np.savetxt('3H_output2/xoutS_'+str(i)+'_'+str(k)+'.csv', xoutS_out, delimiter=',')
#
#
#
# sys.exit()






# plot


dead_cells = np.zeros(shape = (len(traildoses),numcells));

doses = np.zeros(shape = (len(traildoses)));



for i in range(len(traildoses)):
    for k in range(numcells):


        t = []
        with open('3H_output/t_'+str(i)+'_'+str(k)+'.csv', newline='') as csvfile:
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
        with open('3H_output/xoutS_'+str(i)+'_'+str(k)+'.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)





        x = t/3600;

        y=xoutS[:,106-1];

        if np.sum(y>100):
            # TODO = check this line
            dead_cells[i,k] = 1
        else:
            dead_cells[i,k] = 0

    doses[i] = xoutS[1-1,84-1]


# dosesngperml=doses*2.597402597402597e+01;

traildoses = np.array(traildoses)
dosesngperml=traildoses*2.597402597402597e+01;



# percent_dead_cells = np.sum(dead_cells,axis=1)/numcells*100;
percent_dead_cells = np.sum(dead_cells,axis=1)/numcells*100;

# TODO - probably fix syntax on this

x = np.log10(dosesngperml);
# TODO - possibly fix syntax

y=100-percent_dead_cells;


# fig,ax = plt.subplots()

f = plt.figure()


line1, = plt.plot(x, y,'o',markersize=12)

plt.ylabel('Percent Surviving Cells')
plt.xlabel('log10 ([TRAIL] (ng/mL)) ')




# ax.set_xscale('log')


plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
plt.xlim(0,3)
plt.xticks([0,0.5,1,1.5,2,2.5,3])

plt.savefig('3H_output/plot.pdf')






# St=load(strcat(matpath,'Apoptosis1S_dr.mat'));
# conds=St.condsS;
# dead_cells=[];
# doses=[];
# for i=1:size(conds,1)
#     for k=1:size(conds,2)
#         x=conds{i,k}.tout_all/3600;
#         y=conds{i,k}.xoutS_all(:,106);
#         %plot(x,y,'Color',colors(i,:))
#         hold on
#         if sum(y>100)
#             dead_cells(i,k)=1;
#         else dead_cells(i,k)=0;
#         end
#     end
#     doses(i)=conds{i,k}.xoutS_all(1,84);
# end
# dosesngperml=doses*2.597402597402597e+01;
#
# percent_dead_cells=sum(dead_cells,2)/size(conds,2)*100;
# x=log10(dosesngperml');
# y=100-percent_dead_cells;
# [params,x_vector,y_vector]=sigm_fit(x,y);
# %Experimental data (Luis)
# [traildeath_exp,~,~]=xlsread('data_experimental.xlsx','TRAILdr','','basic');
# plot(log10(traildeath_exp(:,1)),traildeath_exp(:,2),'k*','MarkerSize',5)
# hold on
# plot(x_vector,y_vector,'r-')
# plot(x,y,'r.','MarkerSize',10)
# ylim([0 100])
# xlim([0 3])
# set(gca,'XTick',[0 1 2 3])
# set(gca,'XTickLabels',{'10^{0}','10^{1}','10^{2}','10^{3}'});
