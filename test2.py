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




dataS_up = dataS


[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS_up, dataG, dataG.kTCleak, dataG.kTCmaxs)







np.savetxt('t'+'_' + str(i)  + '.csv', t, delimiter=',')
np.savetxt('xoutG' +'_' + str(i)  + '.csv', xoutG, delimiter=',')
np.savetxt('xoutS' +'_' + str(i)  + '.csv', xoutS, delimiter=',')








print("done")
