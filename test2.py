import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *


np.set_printoptions(threshold=np.nan)



# deterministic
th=12;
flagD=1;
[dataS, dataG] = RunPrep()
STIM = np.zeros(shape = (775));
STIM [84-1] = 0.00385
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
np.savetxt('t_deterministic.csv', t, delimiter=',')
np.savetxt('xoutG_deterministic.csv', xoutG, delimiter=',')
np.savetxt('xoutS_deterministic.csv', xoutS, delimiter=',')




# stochastic
th=12;
flagD=0
STIM = np.zeros(shape = (775));
STIM[156-1:162]=[3.3,100,100,100,100,100,1721]
[dataS, dataG] = RunPrep()
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
np.savetxt('t_stochastic.csv', t, delimiter=',')
np.savetxt('xoutG_stochastic.csv', xoutG, delimiter=',')
np.savetxt('xoutS_stochastic.csv', xoutS, delimiter=',')








print("done")
