# function [tout_all,xoutG_all,xoutS_all]=RunModel(flagD,th,STIM,xoutS,xoutG,dataS,dataG,kTCleak,kTCmaxs)
import pandas
import sys
import numpy as np
from RunPrep import *
from gm import *
from scipy.integrate import odeint
from scipy.integrate import ode
from createODEs import *

from numba import jit

# from skel_createODEs import skel_createODEs


import time
start_time = time.time()



def RunModel(flagD,th,STIM,xoutS,xoutG,dataS,dataG,kTCleak,kTCmaxs, inds_to_watch = []):
    # going to return [tout_all,xoutG_all,xoutS_all]


# This function runs the model and outputs timecourse simulation results.
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



    try:
      dataS
    except NameError:
      dataS = RunPrep()[0]
    else:
      pass

    try:
      dataG
    except NameError:
      dataG = RunPrep()[1]
    else:
      pass




    # %% RUN
    ts=dataS.ts;
    ts_up=ts;
    N_STEPS=th*3600/ts;


    # % IMPORT INITIALIZED PARAMETERS
    pathi='initialized/';





    # % for PARCDL
    kbR0 = float(open(pathi + "i_kbR0.txt").read())


    kTL = []
    with open(pathi + 'i_kTLF.txt') as f:
        for line in f:
            kTL.append(float(line))
    kTL = np.array(kTL)



    kC173 = float(open(pathi + "i_kC173.txt").read())
    kC82 = float(open(pathi + "i_kC82.txt").read())
    kA77 = float(open(pathi + "i_kA77.txt").read())*5

    # ^ forgot to add the *5 to this line and spent sooooo long looking for this mistake lol


    kA87 = float(open(pathi + "i_kA87.txt").read())
    Rt = float(open(pathi + "i_Rt.txt").read())
    EIF4Efree = float(open(pathi + "i_EIF4Efree.txt").read())
    kDDbasal = float(open(pathi + "i_kDDbasal.txt").read())
    Vc = dataS.kS[2]





    # % for gm

    try:
      kTCleak
    except NameError:
      kTCleak = []

      for line in open(pathi + "i_kTCleakF.txt").readlines():
          kTCleak.append(float(line))
    else:
      pass


    try:
      kTCleak
    except NameError:
      kTCmaxs = []

      for line in open(pathi + "i_kTCmaxsF.txt").readlines():
          kTCmaxs.append(float(line))
    else:
      pass


    # % modifying data.S structure
    dataS.kS[0]=Rt;
    dataS.kS[1]=EIF4Efree;
    dataS.kS[11]=kbR0;
    dataS.kS[16:157]=kTL;
    dataS.kS[631]=kC173;
    dataS.kS[540]=kC82;
    dataS.kS[708]=kA77;
    dataS.kS[718]=kA87;
    dataS.kS[449]=kDDbasal;


    # % modifying data.G structure
    dataG.kTCleak=kTCleak;
    dataG.kTCmaxs=kTCmaxs;



    # %species


    xoutS = []

    with open(pathi + 'i_xoutF.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')

            to_append = []
            for item in x:
                to_append.append(float(item))

            xoutS.append(to_append)





    xoutS = np.matrix(xoutS)

    xoutS = xoutS[24,:]



    if len(xoutG) == 0:
        if flagD:
            # need to make this an np array
            xoutG = dataG.x0gm_mpc_D
        else:
            xoutG = dataG.x0gm_mpc
            indsD=dataG.indsD

            xoutG[indsD] = dataG.x0gm_mpc_D[indsD]
            xoutG[indsD+141] = dataG.x0gm_mpc_D[indsD+141]
            xoutG[indsD+141*2] = dataG.x0gm_mpc_D[indsD+141*2]




    # % Apply STIM
    Etop = STIM[len(STIM)-1]

    STIM = STIM[0:len(STIM)-1]




    # xoutS(logical(STIM))=STIM(logical(STIM));

    # code for logical
    if np.any(STIM):

        xoutS[0,STIM.astype(bool)] = STIM[STIM.astype(bool)]

        # TODO - not sure if this is working
        # this only runs if STIM has nonzero values



    dataS.kS[452] = Etop





    # TODO - ODE stuff
    # % Instantiation
    t0 = 0;
    # optionscvodes = CVodeSetOptions('UserData', dataS,...
    #                           'RelTol',1.e-3,...
    #                           'LinearSolver','Dense',...
    #                           'JacobianFn',@Jeval774);
    # CVodeInit(@createODEs, 'BDF', 'Newton', t0, xoutS', optionscvodes);
    #
    # %ODE15s options
    # %optionsode15s=odeset('RelTol',1e-3,'Jacobian',@Jeval774ode15s);
    #


    tout_all = np.zeros(shape=(N_STEPS+1,1))
    xoutG_all = np.zeros(shape=(N_STEPS+1,len(xoutG)))
    xoutS_all = np.zeros(shape=(N_STEPS+1,xoutS.shape[1]))
    tout_all[0] = 0
    xoutG_all[0,:] = np.matrix.transpose(xoutG)

    xoutS_all[0,:] = xoutS







    # % Starting simulations
    print("... Starting Sims")



    for i in range(1,int(N_STEPS)+1):

        # gm
        [xginN,xgacN,AllGenesVecN,xmN,vTC] = gm(flagD,dataG,ts,xoutG,xoutS);



        xoutG = np.append(np.append(np.squeeze(np.asarray(xgacN)),np.squeeze(np.asarray(xginN))),np.squeeze(np.asarray(xmN)))
        # NOTE - matrix to array syntax
        xoutG = np.matrix.transpose(np.matrix(xoutG))


        dataS.mMod=xmN*(1E9/(Vc*6.023E+23)); #convert mRNAs from mpc to nM
        dataG.AllGenesVec=AllGenesVecN;




        xoutG_all[i,:] = np.matrix.transpose(xoutG)

        try:
            xoutS_all[i,:] = np.squeeze(np.asarray(xoutS))
        except:
            xoutS_all[i,:] = np.squeeze(np.asarray(xoutS[0]))



        if xoutS[0,103]<xoutS[0,105]:
            print("Apoptosis happened")
            tout_all = tout_all[0:i+1]
            xoutG_all = xoutG_all[0:i+1]
            xoutS_all = xoutS_all[0:i+1]




        # NOTE - testing purposes, comment out
        # createODEs(xoutS_all[i,:],ts_up,dataS,0)
        # sys.exit()



        #NOTE odeint attempt
        # xoutS = odeint(createODEs, xoutS_all[i,:],[ts_up-ts, ts_up], args=(dataS,0))
        xoutS = odeint(createODEs, xoutS_all[i,:],ts_up, args=(dataS,0))





        try:
            print(xoutS[0,inds_to_watch])
        except:
            print(xoutS)




        print(i/N_STEPS)
        print()




        xoutG_all[i,:] = np.matrix.transpose(xoutG);

        xoutS_all[i,:] = xoutS[xoutS.shape[0]-1,:]



        ts_up = ts_up + ts



    print("ODEs done")
    print("--- %s seconds ---" % (time.time() - start_time))
