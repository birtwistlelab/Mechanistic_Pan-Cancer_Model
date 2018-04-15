
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
import matplotlib.pyplot as plt


np.set_printoptions(threshold=np.nan)


[dataS, dataG] = RunPrep()


# I=Plot_GetInfo;
# tppERK=I.tppERK;
# inds=tppERK;
# a1=figure;

# for n=1:3; %three conditions
# StD=load(strcat(matpath,'GFdoseresponse1D_EI_',num2str(n),'.mat'));
# condsD=StD.condsD;
# colors=colororder;%cool(4);
# % timepoints plots Determ
# subplot(3,1,n)
#     for i=1:length(condsD)
#         x=condsD{i}.tout_all/60;
#         %y=sum(condsD{i}.xoutG_all(:,292:294),2);
#         %y=sum(condsD{i}.xoutS_all(:,inds).*repmat([dataS.VxPARCDL(inds)/dataS.kS(3)]',length(x),1),2);
#
#         y=sum(condsD{i}.xoutS_all(:,inds).*repmat([dataS.VxPARCDL(inds)/dataS.kS(3)]',length(x),1),2);
#         plot(x,y,'Color',colors(i,:));%,'LineWidth',0.3)
#         hold on
#         xlim([0 360])
#         ylim([0 120])
#         set(gca,'XTick',0:120:360)
#     end
# end


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

            m_EGF, = ax1.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)
            # legend_array.append(m_EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title(y_ax_labels[k-1] + "  (dashes = python, dots = matlab)")

            # plt.legend(handles=legend_array)
            # plt.title(y_ax_labels[k-1])


        if k==2:
            EGF, = ax2.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax2.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])



            legend_array.append(EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title(y_ax_labels[k-1])
            ax2.set_ylabel('ppERK (nM)')

        if k==3:
            EGF, = ax3.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax3.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])

            legend_array.append(EGF)

            ax3.legend(handles=legend_array)
            ax3.set_title(y_ax_labels[k-1])

        # plt.ylabel('ppERK (nM)')
        plt.xlabel('Time (hours)')


        # legend_array.append(EGF)


    # plt.legend(handles=legend_array)
f.savefig("fig3_output/" + "3B_ERK.pdf")










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

            m_EGF, = ax1.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title(y_ax_labels[k-1] + "  (dashes = python, dots = matlab)")


        if k==2:
            # EGF, = ax2.plot(t, y, label=labels[k-1][i])

            EGF, = ax2.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax2.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title(y_ax_labels[k-1])
            ax2.set_ylabel('ppATK (nM)')

        if k==3:
            # EGF, = ax3.plot(t, y, label=labels[k-1][i])

            EGF, = ax3.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax3.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])

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

            m_EGF, = ax1.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax1.legend(handles=legend_array)
            ax1.set_title(y_ax_labels[k-1] + "  (dashes = python, dots = matlab)")


        if k==2:
            EGF, = ax2.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax2.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax2.legend(handles=legend_array)
            ax2.set_title(y_ax_labels[k-1])
            ax2.set_ylabel('pEIF4EBP1 (nM)')

        if k==3:
            EGF, = ax3.plot(t, y, '--', color = colors_array[i], label=labels[k-1][i])

            m_EGF, = ax3.plot(t, matlab,':', color = colors_array[i], label=labels[k-1][i])


            legend_array.append(EGF)

            ax3.legend(handles=legend_array)
            ax3.set_title(y_ax_labels[k-1])

        # plt.ylabel('ppERK (nM)')

        # legend_array.append(EGF)

        plt.xlabel('Time (hours)')

    # plt.legend(handles=legend_array)
f.savefig("fig3_output/" + "3D_EIF4EBP1.pdf")
