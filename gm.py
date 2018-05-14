
import numpy as np
import sys
import scipy.stats
from random import *

def gm(flagD,dataG,ts,xoutG,xoutS):
    # going to return [xginN,xgacN,AllGenesVecN,xmN,vTC]


    Vn = dataG.Vn

    mpc2nmcf_Vn=1E9/(Vn*6.023E+23);


    # % Defining Terms
    kGin=dataG.kGin;
    kGac=dataG.kGac;
    kTCleak=dataG.kTCleak;
    kTCmaxs=dataG.kTCmaxs;
    kTCd=dataG.kTCd;
    tcnas=dataG.tcnas;
    tcnrs=dataG.tcnrs;
    tck50as=dataG.tck50as;
    tck50rs=dataG.tck50rs;
    GenePositionMatrix=dataG.GenePositionMatrix;
    AllGenesVec=dataG.AllGenesVec;
    indsD=dataG.indsD;




    numberofgenes = tck50as.shape[0]
    numberofTARs = tck50as.shape[1]



    # gm species
    a=0
    xgac=xoutG[a:a+numberofgenes];
    a=a+numberofgenes;

    xgin=xoutG[a:a+numberofgenes];
    a=a+numberofgenes;

    xm=xoutG[a:a+numberofgenes];



    # Gene switching constants
    kGin_1=kGin[0];
    kGac_1=kGac[0];

    # vTC and vTCd
    TAs=np.zeros(shape = (numberofgenes,numberofTARs));
    TRs=np.zeros(shape = (numberofgenes,numberofTARs));

    # TARs
    pcFos_cJun=xoutS[0,684]; #1

    cMyc=xoutS[0,685]; #2
    p53ac=xoutS[0,2]; #3
    FOXOnuc=xoutS[0,767]; #4
    ppERKnuc=xoutS[0,675]; #5
    pRSKnuc=xoutS[0,678]; #6
    bCATENINnuc=xoutS[0,686]; #7

    # activators

    TAs[9:12,0] = pcFos_cJun




    TAs[98,0] = pcFos_cJun

    TAs[9:12,1]=cMyc;
    TAs[[25,52,53],2]=p53ac;
    TAs[[54,57,58,59,60,62,64,65,126,127,135,139],3]=FOXOnuc;
    TAs[[67,91,96,97],4]=ppERKnuc;
    TAs[[67,91,96,97],5]=pRSKnuc;
    TAs[99,6]=bCATENINnuc;
    TAs=TAs*(1/mpc2nmcf_Vn);


    # # repressors
    TRs[97,0]=pcFos_cJun;
    TRs=TRs*(1/mpc2nmcf_Vn);




    # make hills
    TFa=(TAs/tck50as)**tcnas;



    TFa[np.isnan(TFa)]=0;
    TFr=(TRs/tck50rs)**tcnrs;
    TFr[np.isnan(TFr)]=0;
    hills = np.sum(TFa,axis=1)/(1 + np.sum(TFa,axis=1) + np.sum(TFr,axis=1))




    # With AP1*cMYC exception:
    # hills(10:12)=(TFa(10:12,1)./      (1+TFa(10:12,1))) .*    (TFa(10:12,2)./(1+TFa(10:12,2)));

    hills[9:12]= np.multiply((TFa[9:12,0]/(1+TFa[9:12,0])),(TFa[9:12,1]/(1+TFa[9:12,1])));
    # so many parenthese :-/




    # vTC

    hills = np.matrix(hills)
    hills = np.matrix.transpose(hills)

    induced=np.multiply(np.multiply(xgac,kTCmaxs),hills);



    leak= np.multiply(xgac,kTCleak);


    vTC=leak+induced;








    # vTCd
    vTCd= np.multiply(np.matrix.transpose(np.matrix(kTCd)),xm);





    try:
      AllGenesVec[0]
    except :
        xginN=[];
        xgacN=[];
        AllGenesVecN=[];
        xmN=[];



    # # %% Poisson Stuff
    poff = scipy.stats.poisson.pmf(0,kGin_1*ts)
    pon = scipy.stats.poisson.pmf(0,kGac_1*ts)



    # # % Generating random numbers and deciding which genes should turn off and on
    #
    # # RandomNumbers=rand(length(AllGenesVec),1);
    RandomNumbers = []
    for i in range(len(AllGenesVec)):
        RandomNumbers.append(random())


    RandomNumbers = np.matrix.transpose(np.matrix(RandomNumbers))



    # # geneson=logical(AllGenesVec);
    geneson = AllGenesVec.astype(bool).astype(int)

    genesoff = np.logical_not(geneson).astype(int)



    ac2in = np.logical_and(geneson,RandomNumbers>=poff)
    in2ac = np.logical_and(genesoff,RandomNumbers>=pon)


    # # % Generating new AllGenesVec and allocating active and inactive genes
    AllGenesVecN=AllGenesVec;


    # AllGenesVecN[ac2in-1]=0;
    # AllGenesVecN[in2ac-1]=1;
    AllGenesVecN[ac2in]=0;
    AllGenesVecN[in2ac]=1;

    xgacN = np.dot(GenePositionMatrix,AllGenesVecN);
    xginN=(xgac+xgin)-xgacN;




    # # mRNA



    Nb=np.random.poisson(vTC*ts);
    Nd=np.random.poisson(vTCd*ts);






    # # These genes and mRNAs we don't allow to fluctuate
    # # Nb(indsD)=vTC(indsD)*ts;
    Nb[indsD]=vTC[indsD]*ts;



    Nd[indsD]=vTCd[indsD]*ts;

    xgacN[indsD]=xoutG[indsD];



    xginN[indsD]=xoutG[indsD+numberofgenes];



    # # % OUTPUT deterministic results instead:

    if flagD:
        Nb=vTC*ts;
        Nd=vTCd*ts;
        xgacN = xoutG[0:numberofgenes]
        xginN = xoutG[numberofgenes:numberofgenes*2]



    # # % Finish mRNA
    xmN=xm+Nb-Nd;
    xmN[xmN<0]=0;


    return [xginN,xgacN,AllGenesVecN,xmN,vTC]
