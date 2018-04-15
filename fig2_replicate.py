# plot figs

import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

np.set_printoptions(threshold=np.nan)
















t = []

with open("figs_output/" + 't.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')

        to_append = []
        for item in x:
            to_append.append(float(item))

        t.append(to_append)

t = np.array(t)


xoutG = []

with open("figs_output/" + 'xoutG4.csv', newline='') as csvfile:
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

with open("figs_output/" + 'xoutS4.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')

        to_append = []
        for item in x:
            to_append.append(float(item))

        xoutS.append(to_append)


xoutS = np.array(xoutS)








 # NOTE - fig 2 B MAPK1 and MAPK3
# f = plt.figure()
#
# plt.subplot(2, 1, 1)
# ERK1, = plt.plot(t/3600, xoutG[:,115], label='ERK1')
# plt.ylabel('MAPK1 g*')
#
#
# plt.subplot(2, 1, 2)
#
# ERK2, = plt.plot(t/3600, xoutG[:,116], label='ERK2')
# plt.setp(ERK1, linewidth=3, color='b')
# plt.setp(ERK1, linewidth=3, color='r')
# plt.ylabel('MAPK3 g*')
# plt.show()


# print(xoutG[:,115])
#
# print(t.shape)
# print(xoutG.shape)

# f.savefig("figs_output/fig2_python_4.pdf")





# NOTE - fig 2 mRNA

# f = plt.figure()
#
# # plt.subplot(2, 1, 1)
# MAPK1, = plt.plot(t/3600, xoutG[:,397], label='MAPK1')
# MAPK3, = plt.plot(t/3600, xoutG[:,398], label='MAPK3')
# plt.legend(handles=[MAPK1, MAPK3])
# plt.ylabel('mRNA')


# plt.subplot(2, 1, 2)
#
# ERK2, = plt.plot(t/3600, xoutG[:,116], label='ERK2')
# plt.setp(ERK1, linewidth=3, color='b')
# plt.setp(ERK1, linewidth=3, color='r')
# plt.ylabel('MAPK3 g*')
# plt.show()
#
# f.savefig("figs_output/fig2_mrna_4.pdf")






obs_mat = []

with open("observables_mat_18.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')

        to_append = []
        for item in x:
            try:
                to_append.append(float(item))
            except:
                to_append.append(item)

        obs_mat.append(to_append)

obs_mat = np.array(obs_mat)



tERK = []

for row in obs_mat:
    try:
        tERK.append(float(row[95]))
    except:
        pass

tERK = np.array(tERK)




data = xoutS[:,np.nonzero(tERK)]


to_plot = []

for row in data:
    to_plot.append(np.sum(row))




# NOTE - figure 2B -- ERK graph
f = plt.figure()
#
# # plt.subplot(2, 1, 1)
MAPK1, = plt.plot(t/3600, to_plot, label='test')
# # plt.legend(handles=[MAPK1, MAPK3])
plt.ylabel('[ERK] (nM)')
#
plt.show()



f.savefig("figs_output/fig2_ERK_4.pdf")



print("done")
