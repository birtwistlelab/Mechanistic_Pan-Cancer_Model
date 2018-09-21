# replicate figures


import numpy as np
from RunPrep import *
from RunModel import *



# fig 2b

# flagD=0;
# th=24;
# STIM=zeros(NumSpecies,1);
# [tout_all,xoutG_all,xoutS_all]=RunModel(flagD,th,STIM,[],[],[],[]);
# tout_all=tout_all;
# xoutG_all=xoutG_all;
# xoutS_all=xoutS_all;

#
[dataS, dataG] = RunPrep()
flagD = 0
th = 24
xoutS = []
xoutG = []
STIM= np.zeros(shape = (775));
#
out = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
#
t = out[0]
xoutG = out[1]
xoutS = out[2]
#
# print(len(t))
# print(len(xoutG))
# print(len(xoutS))
#
#
# # NOTE - save to csv
np.savetxt('figs_output/t4.csv', t, delimiter=',')
np.savetxt('figs_output/xoutG4.csv', xoutG, delimiter=',')
np.savetxt('figs_output/xoutS4.csv', xoutS, delimiter=',')


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

with open("figs_output/" + 'xoutG.csv', newline='') as csvfile:
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

with open("figs_output/" + 'xoutS.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        x = ', '.join(row)
        x = x.split(',')

        to_append = []
        for item in x:
            to_append.append(float(item))

        xoutS.append(to_append)


xoutS = np.array(xoutS)








#  # NOTE - fig 2 B MAPK1 and MAPK3
# f = plt.figure()
#
# plt.subplot(2, 1, 1)
# plt.xticks([0,4,8,12,16,20,24])
# plt.yticks([0,1,2])
# ERK1, = plt.plot(t/3600, xoutG[:,115], label='ERK1')
# plt.ylabel('MAPK1 g*')
#
#
# plt.subplot(2, 1, 2)
# plt.xticks([0,4,8,12,16,20,24])
# plt.yticks([0,1,2])
# ERK2, = plt.plot(t/3600, xoutG[:,116], label='ERK2')
# plt.setp(ERK1, linewidth=3, color='b')
# plt.setp(ERK2, linewidth=3, color='r')
# plt.ylabel('MAPK3 g*')
# plt.xlabel('Time (hours)')
#
# plt.show()
#
#
#
#
# f.savefig("figs_output/fig2_python_new.pdf")
#
#
# sys.exit()





# # NOTE - fig 2 mRNA
#
# f = plt.figure()
#
# # plt.subplot(2, 1, 1)
# plt.xticks([0,4,8,12,16,20,24])
# plt.yticks([0,5,10])
# MAPK1, = plt.plot(t/3600, xoutG[:,397], label='MAPK1')
# MAPK3, = plt.plot(t/3600, xoutG[:,398], label='MAPK3')
# plt.legend(handles=[MAPK1, MAPK3])
# plt.ylabel('mRNA')
#
#
# # plt.subplot(2, 1, 2)
# #
# # plt.xticks([0,4,8,12,16,20,24])
# # ERK2, = plt.plot(t/3600, xoutG[:,116], label='ERK2')
# # plt.setp(ERK1, linewidth=3, color='b')
# # plt.setp(ERK1, linewidth=3, color='r')
# # plt.ylabel('MAPK3 g*')
# # plt.show()
#
# f.savefig("figs_output/fig2_mrna_4.pdf")
#
#
#
# sys.exit()


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
plt.xticks([0,4,8,12,16,20,24])

MAPK1, = plt.plot(t/3600, to_plot, label='test')
# # plt.legend(handles=[MAPK1, MAPK3])
plt.ylabel('[ERK] (nM)')
#
plt.show()



f.savefig("figs_output/fig2_ERK_new.pdf")



print("done")
