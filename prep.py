from RunPrep import *
import pickle

[dataS, dataG] = RunPrep()

with open('dataS.pickle', 'wb') as f:
    pickle.dump(dataS, f)

with open('dataG.pickle', 'wb') as f:
    pickle.dump(dataG, f)
