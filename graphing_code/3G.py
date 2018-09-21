import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *


np.set_printoptions(threshold=np.nan)




# Figure 3G
# TRAIL dose response Time Course




# # NOTE - generating data
th=200;
flagD=1;

i=0

traildoses=[0.000385, 0.001925, 0.00385, 0.01925, 0.0385, 0.1925, 0.385, 1.9250, 3.85, 19.25, 38.5]
# # traildoses=[0.001925,  0.385, 1.9250, 19.25, 38.5]







[dataS, dataG] = RunPrep()



STIM = np.zeros(shape = (775));
STIM [84-1] = traildoses[0]



# starting with only 5 sims instead of the 20 in matlab
# for k in range(0,5):

dataS_up = dataS


[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, dataG.kTCleak, dataG.kTCmaxs)







np.savetxt('3G_output/t'+'_' + str(i)  + '.csv', t, delimiter=',')
np.savetxt('3G_output/xoutG' +'_' + str(i)  + '.csv', xoutG, delimiter=',')
np.savetxt('3G_output/xoutS' +'_' + str(i)  + '.csv', xoutS, delimiter=',')



# NOTE - plot data



fig,ax = plt.subplots()


doses = []
tds = []

# nums = [0,1,3,5,7]
# nums = [1,3,5,7,9]

for i in range(0,len(traildoses)):
# for i in nums:




    xoutG = []
    with open('3G_output/xoutG' +'_' + str(i)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutG.append(to_append)

    xoutG = np.array(xoutG)









    t = []
    with open('3G_output/t.csv' +'_' + str(i)  + '.csv', newline='') as csvfile:
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
    with open('3G_output/xoutS' +'_' + str(i)  + '.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutS.append(to_append)

    xoutS = np.array(xoutS)


    x = t/3600

    y = xoutS[:,106-1]

    line1, = ax.plot(x, y)


    ax.set_ylabel('[cPARP]')
    ax.set_xlabel('Time (hours)')

    doses.append(xoutS[0,84-1])


    try:
        tds.append(float(x[np.amin(np.where(y>100))]))

    except:
        tds.append(72)


print("good")

# plt.show()
plt.title('<-- Increasing TRAIL <-- ')
plt.savefig('3G_output/plot01.pdf')




fig,ax = plt.subplots()

doses = np.array(doses)




# b2=figure;
dosesngperml=doses*2.597402597402597e+01;


# line1, = ax.plot(np.log10(dosesngperml), tds)
line1, = ax.plot(dosesngperml, tds)

ax.set_xscale('log')


ax.set_ylabel('ttd (hours)')
ax.set_xlabel('[TRAIL] (ng/mL) ')


ax.set_yticks[0,50,100]

# plt.show()

plt.savefig('3G_output/plot02.pdf')


# FO = fit(log10(dosesngperml'), tds', 'exp2');
# h=plot(FO,log10(dosesngperml),tds,'r.');
# legend off; xlabel(''); ylabel('');
# xlim([-2 3])
# set(gca,'XTick',[-2 0 3])
# set(gca,'XTickLabels',{'10^{-2}','10^{0}','10^{3}'});%[1E-2,1E-1,1E0,1E1,1E3])
# set(h(1),'MarkerSize',10)
# set(h(2),'Color','r')




print("done")
