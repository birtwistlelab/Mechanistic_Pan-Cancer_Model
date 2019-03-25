import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
from RunPrep import *
from RunModel import *

import pickle
import sys

np.set_printoptions(threshold=sys.maxsize)

# deterministic
th=0.1;
flagD=1;

with open('dataS.pickle', 'rb') as f:
    dataS = pickle.load(f)

with open('dataG.pickle', 'rb') as f:
    dataG = pickle.load(f)

STIM = np.zeros(shape = (775));
STIM [84-1] = 0.00385
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
np.savetxt('t_deterministic.csv', t, delimiter=',')
np.savetxt('xoutG_deterministic.csv', xoutG, delimiter=',')
np.savetxt('xoutS_deterministic.csv', xoutS, delimiter=',')

print("done ")
