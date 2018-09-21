# figure 3 replication

import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *


np.set_printoptions(threshold=np.nan)









[dataS, dataG] = RunPrep()




condsD = []

for k in range(1,4):
    STIMS= np.zeros(shape = (775,4));
    indegf=156-1;
    indins=162-1;

    if k == 1:
        STIMS[indegf,0]=0.01;
        STIMS[indegf,1]=0.1;
        STIMS[indegf,2]=1;
        STIMS[indegf,3]=10;

    if k==2:
        STIMS[indins,0]=0.17;
        STIMS[indins,1]=1.7;
        STIMS[indins,2]=17;
        STIMS[indins,3]=1721;

    if k==3:
        STIMS[[indegf,indins],0]=[0.01,0.17];
        STIMS[[indegf,indins],1]=[0.01,1721];
        STIMS[[indegf,indins],2]=[10,0.17];
        STIMS[[indegf,indins],3]=[10,1721];


    th=6;
    flagD=1;
    condsD=[];




    for i in range(0,4):
        STIM=STIMS[:,i];
        [t,xoutG,xoutS]=RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
        np.savetxt('fig3_output2/t' + '_' + str(k) + '_' + str(i) + '.csv', t, delimiter=',')
        np.savetxt('fig3_output2/xoutG' + '_' + str(k) + '_' + str(i) + '.csv', xoutG, delimiter=',')
        np.savetxt('fig3_output2/xoutS' + '_' + str(k) + '_' + str(i) + '.csv', xoutS, delimiter=',')






colors_array = ['b','r','g','y']


# NOTE - 3B ERK

inds = [151-1,155-1,226-1,227-1,228-1,676-1,718-1,729-1,730-1,733-1,738-1,740-1,742-1,750-1,757-1,758-1]

y_ax_labels = ["EGF","Insulin","EGF + Insulin"]

labels = [["E 0.01nM", "E 0.1nM","E 1nM","E 10nM"],["I 0.17nM","I 1.7nM","I 17nM","I 1721nM"],["Low/Low (E/I)","Low/High","High/Low","High/High"]]

# for k in range(1,4):

# TODO - change
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

for k in range(1,4):

    # f = plt.figure()

    # plt.subplot(2, 1, k)
    plt.ylim(0,100)
    # plt.title(y_ax_labels[k-1])

    legend_array = []


    for i in range(0,4):

        t = []

        with open('fig3_output2/t' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                t.append(to_append)

        t = np.array(t)/60


        xoutG = []


        with open('fig3_output2/xoutG' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutG.append(to_append)

        xoutG = np.array(xoutG)



        xoutS = []

        with open('fig3_output2/xoutS' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)




        matlab = []

        with open('fig3_data_matlab/mike_y_data' + str(i+1) + str(k) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                matlab.append(to_append[0])






        to_repeat = dataS.VxPARCDL[inds]/dataS.kS[3-1]

        to_repeat = np.matrix.transpose(to_repeat)

        to_repeat = np.repeat(to_repeat,len(t),axis=0)

        y = np.sum(np.multiply(xoutS[:,inds],to_repeat),axis=1)

        # EGF, = plt.plot(t, y, label=labels[k-1][i])
        if k==1:
            # EGF, = ax1.plot(t, y, '--', t, matlab, 'g^', label=labels[k-1][i])
            # EGF, = ax1.plot(t, y, '--')
            EGF, = ax1.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax1.plot(t, matlab,':', linewidth=5,  color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)
            # legend_array.append(m_EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title(y_ax_labels[k-1] + "  (horizontal dashes = python, vertical dashes = matlab)")

            # plt.legend(handles=legend_array)
            # plt.title(y_ax_labels[k-1])


        if k==2:
            EGF, = ax2.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax2.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])



            legend_array.append(EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title(y_ax_labels[k-1])
            ax2.set_ylabel('ppERK (nM)')

        if k==3:
            EGF, = ax3.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax3.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])

            legend_array.append(EGF)

            ax3.legend(handles=legend_array)
            ax3.set_title(y_ax_labels[k-1])

        # plt.ylabel('ppERK (nM)')
        plt.xlabel('Time (hours)')


        # legend_array.append(EGF)


    # plt.legend(handles=legend_array)

plt.show()
sys.exit("done 3b")
# f.savefig("fig3_output/" + "3B_ERK.pdf")










# NOTE- 3c
inds = [33-1,153-1,697-1,704-1,747-1,749-1,754-1]
y_ax_labels = ["EGF","Insulin","EGF + Insulin"]

labels = [["E 0.01nM", "E 0.1nM","E 1nM","E 10nM"],["I 0.17nM","I 1.7nM","I 17nM","I 1721nM"],["Low/Low (E/I)","Low/High","High/Low","High/High"]]

# for k in range(1,4):


f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

for k in range(1,4):

    # f = plt.figure()

    # plt.subplot(2, 1, k)
    plt.ylim(0,45)
    plt.yticks([0,20,40])
    # plt.title(y_ax_labels[k-1])

    legend_array = []


    for i in range(0,4):

        t = []

        with open('fig3_output/t' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                t.append(to_append)

        t = np.array(t)/60


        xoutG = []


        with open('fig3_output/xoutG' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutG.append(to_append)

        xoutG = np.array(xoutG)



        xoutS = []

        with open('fig3_output/xoutS' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)





        matlab = []

        with open('fig3_data_matlab/mike_ATK_data' + str(i+1) + str(k) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                matlab.append(to_append[0])


        to_repeat = dataS.VxPARCDL[inds]/dataS.kS[3-1]

        to_repeat = np.matrix.transpose(to_repeat)

        to_repeat = np.repeat(to_repeat,len(t),axis=0)

        y = np.sum(np.multiply(xoutS[:,inds],to_repeat),axis=1)


        # EGF, = plt.plot(t, y, label=labels[k-1][i])
        if k==1:
            # EGF, = ax1.plot(t, y, label=labels[k-1][i])

            EGF, = ax1.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax1.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title(y_ax_labels[k-1] + "  (horizontal dashes = python, vertical dashes = matlab)")


        if k==2:
            # EGF, = ax2.plot(t, y, label=labels[k-1][i])

            EGF, = ax2.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax2.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title(y_ax_labels[k-1])
            ax2.set_ylabel('ppATK (nM)')

        if k==3:
            # EGF, = ax3.plot(t, y, label=labels[k-1][i])

            EGF, = ax3.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax3.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])

            legend_array.append(EGF)

            ax3.legend(handles=legend_array)
            ax3.set_title(y_ax_labels[k-1])

        # plt.ylabel('ppERK (nM)')

        # legend_array.append(EGF)
        plt.xlabel('Time (hours)')


    # plt.legend(handles=legend_array)
f.savefig("fig3_output/" + "3C_ATK.pdf")




# NOTE - 3D EIF4EBP1
inds=727-1; #pEIF4EBP1
y_ax_labels = ["EGF","Insulin","EGF + Insulin"]

labels = [["E 0.01nM", "E 0.1nM","E 1nM","E 10nM"],["I 0.17nM","I 1.7nM","I 17nM","I 1721nM"],["Low/Low (E/I)","Low/High","High/Low","High/High"]]

# for k in range(1,4):


f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

for k in range(1,4):

    # f = plt.figure()

    # plt.subplot(2, 1, k)
    plt.ylim(0,10)
    plt.yticks([0,5,10])
    # plt.title(y_ax_labels[k-1])

    legend_array = []


    for i in range(0,4):

        t = []

        with open('fig3_output/t' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                t.append(to_append)

        t = np.array(t)/60


        xoutG = []


        with open('fig3_output/xoutG' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutG.append(to_append)

        xoutG = np.array(xoutG)



        xoutS = []

        with open('fig3_output/xoutS' + '_' + str(k) + '_' + str(i) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                xoutS.append(to_append)

        xoutS = np.array(xoutS)


        matlab = []
        with open('fig3_data_matlab/mike_4EBP1_data' + str(i+1) + str(k) + '.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                x = ', '.join(row)
                x = x.split(',')

                to_append = []
                for item in x:
                    to_append.append(float(item))

                matlab.append(to_append[0])





        # to_repeat = dataS.VxPARCDL[inds]/dataS.kS[3-1]
        #
        # to_repeat = np.matrix.transpose(to_repeat)
        #
        # to_repeat = np.repeat(to_repeat,len(t),axis=0)
        #
        # y = np.sum(np.multiply(xoutS[:,inds],to_repeat),axis=1)

        y = xoutS[:,inds]
        # sys.exit()


        # EGF, = plt.plot(t, y, label=labels[k-1][i])
        if k==1:
            EGF, = ax1.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax1.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title(y_ax_labels[k-1] + "  (horizontal dashes = python, vertical dashes = matlab)")


        if k==2:
            EGF, = ax2.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax2.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title(y_ax_labels[k-1])
            ax2.set_ylabel('pEIF4EBP1 (nM)')

        if k==3:
            EGF, = ax3.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax3.plot(t, matlab,':', linewidth=5, color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax3.legend(handles=legend_array)
            ax3.set_title(y_ax_labels[k-1])

        # plt.ylabel('ppERK (nM)')

        # legend_array.append(EGF)

        plt.xlabel('Time (hours)')

    # plt.legend(handles=legend_array)
f.savefig("fig3_output/" + "3D_EIF4EBP1.pdf")
