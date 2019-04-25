import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from random import randint
from RunPrep import *
from RunModel import *
import sys


np.set_printoptions(threshold=np.nan)
cdir = os.getcwd()
ext = str(sys.argv[1])		#will likely be fixed with command line args in future versions
ndir = cdir + "/op/"+ext
os.makedirs(ndir,exist_ok=True)

# deterministic
th=12;
flagD=1;
[dataS, dataG] = RunPrep()
STIM = np.zeros(shape = (775));
STIM [84-1] = 0.00385
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
np.savetxt(ndir+'/t_deterministic.csv', t, delimiter=',')
np.savetxt(ndir+'/xoutG_deterministic.csv', xoutG, delimiter=',')
np.savetxt(ndir+'/xoutS_deterministic.csv', xoutS, delimiter=',')




# stochastic
th=12;
flagD=0
STIM = np.zeros(shape = (775));
STIM[156-1:162]=[3.3,100,100,100,100,100,1721]
[dataS, dataG] = RunPrep()
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, [], [], dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
np.savetxt(ndir+'/t_stochastic.csv', t, delimiter=',')
np.savetxt(ndir+'/xoutG_stochastic.csv', xoutG, delimiter=',')
np.savetxt(ndir+'/xoutS_stochastic.csv', xoutS, delimiter=',')




print("done ")