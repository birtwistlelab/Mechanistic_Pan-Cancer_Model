import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *

from scipy.signal import *

import peakutils



np.set_printoptions(threshold=np.nan)

numcells = 30


# No GFs data in
#
ttd = np.zeros(shape = (numcells));

f = plt.figure()


for k in range(numcells):



    # Only 2 because we're graphing time post-etoposide treatment
    t = []
    with open('4A_output/no_gfs/t_'+str(k)+'_1.csv', newline='') as csvfile:
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
    with open('4A_output/no_gfs/xoutS_'+str(k)+'_1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutS.append(to_append)

    xoutS = np.array(xoutS)

    #
    # xoutG = []
    # with open('4A_output/no_gfs/xoutG_'+str(k)+'_1.csv', newline='') as csvfile:
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



    # calc TTD
    time = np.where(xoutS[:,106-1]>100)[0]



    if time.size>0:
        ttd[k] = t[min(time)]/3600

        print(k)
        print(t[min(time)]/3600)
        print()


    # trying somethingn else

    # ttd[k] = t[len(t)-1]/3600









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

# make bar graph




objects = ("24h","48h")
y_pos = np.arange(len(objects))
performance = to_graph

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks([0,20,40,60,80,100])

plt.ylabel('Percent Death')
plt.xlabel('Time Post Etoposide Treatment')

plt.title('Cells without Growth Factors')

# plt.show()


f.savefig("4A_output/nogfs_graph.pdf")



sys.exit("done no gfs")
























f = plt.figure()


# GFs data in

ttd = np.zeros(shape = (numcells));



# TODO - comment back in
for k in range(numcells):



    # Only 2 because we're graphing time post-etoposide treatment
    t = []
    with open('4A_output/gfs/t_'+str(k)+'_2.csv', newline='') as csvfile:
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
    with open('4A_output/gfs/xoutS_'+str(k)+'_2.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutS.append(to_append)

    xoutS = np.array(xoutS)


    # xoutG = []
    # with open('4A_output/gfs/xoutG_'+str(k)+'_2.csv', newline='') as csvfile:
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



    # calc TTD
    time = np.where(xoutS[:,106-1]>100)[0]

    if time.size>0:
        ttd[k] = t[min(time)]/3600

        # print(k)
        # print(ttd[k])
        # print()

    print(k)


# TODO - testing, delete






to_graph = []


# 24h
count = 0
for item in ttd:
    if item>0 and int(item)<=24:
        count = count+1
to_graph.append(count/numcells*100)

# 48h
count = 0
for item in ttd:
    if item>0 and int(item)<=48:
        count = count+1
to_graph.append(count/numcells*100)

# 72h
count = 0
for item in ttd:
    if item>0 and int(item)<=72:
        count = count+1
to_graph.append(count/numcells*100)







# make bar graph




objects = ("24h","48h","72h")
y_pos = np.arange(len(objects))
performance = to_graph

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.yticks([0,20,40,60,80,100])

plt.ylabel('Percent Death')
plt.xlabel('Time Post Etoposide Treatment')

plt.title('Cells with Growth Factors')

# plt.show()


f.savefig("4A_output/new_gfs_graph2.pdf")
