# testing file

import sys
import numpy as np
from RunPrep import *
from RunModel import *



# setting things up

[dataS, dataG] = RunPrep()
xoutS = []
xoutG = []
STIM= np.zeros(shape = (775));



# Required Inputs:
# flagD: 1 for deterministic simulations, 0 for stochastic simulations.
# th: simulation time (hours)
# STIM: stimulus vector
#
# Outputs:
# tout_all: n-by-1 vector of time values (seconds)
# xoutG_all: n-by-g matrix of species (g) through time (n) (g indices lines up to gm tab in Names.xls sheet)
# xoutS_all: n-by-p matrix of speices (p) through time (n) (p indices lines up to PARCDL tab in Names.xls sheet)
#

# RunModel params - (flagD,th,STIM,xoutS,xoutG,dataS,dataG,kTCleak,kTCmaxs)
#
# flagD = 0 # can also be 1, test for both
# th = 24
#
# # test
# STIM = np.zeros(shape=(775))
# # That makes a vector of zeros with the column length equal to number of species. This adds ligands or drugs or whatever else you want to add. Later we should
# # maybe try with ligands or drugs added. To add some EGF set STIM(156)=10.  To add some drug set STIM(769)=10000.
#
#
#
#
# RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)



# NOTE - original test, to compare with ydot values that Mehdi sent
# flagD = 0
# th = 24
# RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)





# NOTE -1.  no stimuli

# flagD=1;
# th=6;
# RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)








# NOTE - 2. Growth factor stimulus to assess ERK and AKT. Here let’s look at ppERK (index 718) and ppAKT (index 697)
# time courses over the 6 hours. They should go up and back down. We can compare to Matlab output.
#
flagD=1;
th=6;
STIM[155:162]=[10,10,10,10,10,10,1000];
RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs,[696,717])







# NOTE - 4. Cause apoptosis via TRAIL. Here let’s look at cPARP, which should
# abruptly increase when the cell dies (index 106)

# flagD=1;
# th=24;
# STIM[83]=100;
# RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs,[105])





print("done")
