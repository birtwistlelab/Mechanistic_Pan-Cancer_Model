# testing file

import sys
import numpy as np
from RunPrep import *
from RunModel import *


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

flagD = 0 # can also be 1, test for both
th = 24

# test
STIM = np.zeros(shape=(775))
# That makes a vector of zeros with the column length equal to number of species. This adds ligands or drugs or whatever else you want to add. Later we should
# maybe try with ligands or drugs added. To add some EGF set STIM(156)=10.  To add some drug set STIM(769)=10000.


xoutS = []
xoutG = []

[dataS, dataG] = RunPrep()


RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)


print("done")
