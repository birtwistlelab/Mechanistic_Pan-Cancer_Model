# gm_Prep.py

# import sys
import numpy as np


# had to write this myself
def sample_without_replacement(lower_bound, upper_bound, size):
    import numpy as np
    sample = []
    i = 0
    while i < size:
        draw = np.random.random_integers(lower_bound,upper_bound,1)[0]

        if draw not in sample:
            sample.append(draw)
            i = i + 1
    return(sample)


def gm_Prep(mExp_mpc,gExp_mpc,kTCd,kGac,kGin,numberofgenes):

    # going to return [xgac_mpc,xgin_mpc,xgac_mpc_D,xgin_mpc_D,kTCleak,AllGenesVec,GenePositionMatrix]



    # Make Gene Position Matrix
    GenePositionMatrix = np.zeros(shape = (numberofgenes,sum(gExp_mpc)));
    ind=0;

    for i in range(numberofgenes):

        GenePositionMatrix[i, ind:ind+gExp_mpc[i]] = 1

        ind = ind + gExp_mpc[i]



    # xg Deterministic
    xgac_mpc_D = (kGac*gExp_mpc)/(kGin+kGac); #active genes initial condition
    xgin_mpc_D = gExp_mpc - xgac_mpc_D; #inactive genes initial condition


    # xg Stochastic
    AllGenesVec = np.zeros(shape = (sum(gExp_mpc),1));


    IndsGenesOn=sample_without_replacement(0,sum(gExp_mpc)-1,round(sum(gExp_mpc)*kGac[0]/kGin[0]));

    AllGenesVec[IndsGenesOn]=1;

    # Calculate Concentration of Active and Inactive Genes for each gene
    xgac_mpc= np.dot(GenePositionMatrix,AllGenesVec)


    gExp_mpc = np.matrix.transpose(np.matrix(gExp_mpc))


    xgin_mpc=gExp_mpc-xgac_mpc;


    # kTCleak (deterministic)
    kTCleak = (np.multiply(kTCd,mExp_mpc)/xgac_mpc_D)


    kTCleak[np.isnan(kTCleak)] = 0
    kTCleak[np.isinf(kTCleak)] = 0


    return [xgac_mpc,xgin_mpc,xgac_mpc_D,xgin_mpc_D,kTCleak,AllGenesVec,GenePositionMatrix]
