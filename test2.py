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



# stochastic
th=12;
flagD=0
STIM = np.zeros(shape = (775));
STIM[156-1:162]=[3.3,100,100,100,100,100,1721]
[dataS, dataG] = RunPrep()
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS_up, xoutG_up, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)









print("done")
