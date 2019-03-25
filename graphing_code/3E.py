import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *


np.set_printoptions(threshold=sys.maxsize)



# # # NOTE - generating data
# # #
# # NOTE - 1
# th=24;
# flagD=1;
# STIM= np.zeros(shape = (775));
#
# # STIM[32-1] = 1
# STIM[32-1] = 25
#
#
#
# # [dataS, dataG] = RunPrep()
#
# # m=[0,0.001];
# m=[0,0.15];
#
#
# # dataS_up=dataS;
#
#
#
# for i in range(0,2):
#
#     # redundant line, but had to do this to keep weird stuff from happening
#     [dataS, dataG] = RunPrep()
#     dataS_up=dataS;
#
#
#     dataS_up.kS[446-1:448] = dataS.kS[446-1:448]*m[i];
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
#
#     np.savetxt('3E_output/t1' +'_' + str(i) + '.csv', t, delimiter=',')
#     np.savetxt('3E_output/xoutG1' +'_' + str(i) + '.csv', xoutG, delimiter=',')
#     np.savetxt('3E_output/xoutS1' +'_' + str(i) + '.csv', xoutS, delimiter=',')
#
#
#     print()
#     print(i)
#     print(m[i])
#     print(dataS.kS[446-1:448]*m[i])
#     print(dataS_up.kS[446-1:448])



# # NOTE - 2
# th=24;
# flagD=1;
# STIM= np.zeros(shape = (775));
#
# # STIM[31-1] = 1
#
# STIM[31-1] = 25
#
#
#
# # m=[0,1];
# m = [0,5]
#
#
#
#
# for i in range(0,2):
#     [dataS, dataG] = RunPrep()
#
#     dataS_up=dataS;
#
#     dataS_up.kS[446-1:448]=dataS.kS[446-1:448]*m[i];
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
#
#     np.savetxt('3E_output/t2' +'_' + str(i) + '.csv', t, delimiter=',')
#     np.savetxt('3E_output/xoutG2' +'_' + str(i) + '.csv', xoutG, delimiter=',')
#     np.savetxt('3E_output/xoutS2' +'_' + str(i) + '.csv', xoutS, delimiter=',')
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
#
# # NOTE - 3
# th=24;
# flagD=1;
# STIM= np.zeros(shape = (775));
#
#
# STIM[32-1] = 25
# STIM[31-1] = 25
#
# m=[0,5];
#
#
# for i in range(0,2):
#
#     [dataS, dataG] = RunPrep()
#
#     dataS_up=dataS;
#
#
#     dataS_up.kS[446-1:448]=dataS.kS[446-1:448]*m[i];
#     [t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
#
#     np.savetxt('3E_output/t3' +'_' + str(i) + '.csv', t, delimiter=',')
#     np.savetxt('3E_output/xoutG3' +'_' + str(i) + '.csv', xoutG, delimiter=',')
#     np.savetxt('3E_output/xoutS3' +'_' + str(i) + '.csv', xoutS, delimiter=',')
#
#
#
# sys.exit()


# NOTE - plot data

y_ax_labels = ["EGF","Insulin","EGF + Insulin"]

labels=["Without repair","With repair"]

colors_array = ['b','r','g','y']







t = []
with open('3E_output/t3_1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')

        to_append = []
        for item in x:
            to_append.append(float(item))

        t.append(to_append)

t = np.array(t)





f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)


for k in range(1,4):

    legend_array = []


    for i in range(0,2):


        xoutS = []
        with open('3E_output/xoutS' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)






        y = xoutS[:,2]



        # sys.exit("debug")




        if k==1:

            plt.xticks([0,6,12,18,24])
            # plt.yticks([0,100,200,300,400])

            ax1.set_yticks([0,100,200,300,400])
            # plt.ylim(ymax=400)
            EGF, = ax1.plot(t/3600, y, color = colors_array[i], label=labels[i])

            # m_EGF, = ax1.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)
            # legend_array.append(m_EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title("Single-stranded breaks")

            # plt.legend(handles=legend_array)
            # plt.title(y_ax_labels[k-1])



        if k==2:
            plt.xticks([0,6,12,18,24])
            # plt.ylim(ymax=1000)
            plt.yticks([0,200,400,600,800,1000])
            # ax2.set_yticks([0,200,400,600,800,1000])



            EGF, = ax2.plot(t/3600, y, color = colors_array[i], label=labels[i])



            # m_EGF, = ax1.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)
            # legend_array.append(m_EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title("Double-stranded breaks")

            # plt.legend(handles=legend_array)
            # plt.title(y_ax_labels[k-1])

            ax2.set_ylabel('[p53 Active] (nM)')





        if k==3:
            plt.xticks([0,6,12,18,24])

            EGF, = ax3.plot(t/3600, y, color = colors_array[i], label=labels[i])

            # ax3.set_yticks([0,200,400,600,800,1000])


            # m_EGF, = ax1.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)
            # legend_array.append(m_EGF)

            ax3.legend(handles=legend_array)
            ax3.set_title("Both")

            # plt.legend(handles=legend_array)
            # plt.title(y_ax_labels[k-1])

        plt.xlabel('Time (hours)')









f.savefig("fig3_output/" + "python_3e.pdf")
