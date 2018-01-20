

import pandas
import sys
import numpy as np
from CalcVolumeParams import *
from PARCDL_rateconstants_main import *
from gm_Prep import *
from PARCDL_rateconstants_sd import *
from PARCDL_compartments import *


# This script loads and calculates many of the intial parameters needed to
# run the model.


def RunPrep():
    # going to return (dataS, dataG)



    # GET DATA
    # NOTE - Excel file
    datasheet_gp = pandas.ExcelFile("master_MCF10A.xlsx")
    datasheet_in = pandas.ExcelFile("master_MCF10A.xlsx")



    # Model Essentials
    ts = 30 #Timestep for simulations


    # General params
    datasheet = datasheet_gp
    cellparams = datasheet.parse("cellparams")
    VolumeOfCell = list(cellparams)[1]
    Ve = cellparams.iloc[1,1]



    # NOTE - function call
    Vn,Vc,Vm,mpc2nmcf_Vc,mpc2nmcf_Vm,mpc2nmcf_Vn = CalcVolumeParams(VolumeOfCell)



    mT0 = cellparams.iloc[7,1] * mpc2nmcf_Vc #Total number of mRNAs in single mammalian cell, estimate, convered to nM.
    PIP2_0=cellparams.iloc[8,1];
    M0=cellparams.iloc[9,1];


    tlparams = datasheet.parse("tlparams")
    Rt = list(tlparams)[1]
    kbRi = tlparams.iloc[0,1]
    kdR0 = tlparams.iloc[1,1]


    kbR0 = 0

    nR = tlparams.iloc[2,1]
    nR = tlparams.iloc[2,1]
    k50R = tlparams.iloc[3,1]
    kT1 = tlparams.iloc[4,1]
    kT2 = tlparams.iloc[5,1]
    kT3 = tlparams.iloc[6,1]
    kT4 = tlparams.iloc[7,1]
    k50E = tlparams.iloc[8,1] #This is equal to kT2/kT1; See derivation.






    gene = datasheet.parse("gene")

    kTCd = gene.iloc[:,12] #mRNA degradation rate constants
    kTLd = gene.iloc[:,13] #Protein degradation rate constants
    kTLnat = gene.iloc[:,16] #Translation rate constants
    kGin = gene.iloc[:,17]
    kGac = gene.iloc[:,18]
    #Cyclin D kTLnat adjustment (MCF10A cells)





    kTLnat[9:12] = kTLnat[9:12]*5





    # %Inputs
    datasheet=datasheet_in;
    gene = datasheet.parse("gene")
    gExp_mpc = gene.iloc[:,1] #gene copy numbers experimental (molecules/cell)
    mExp_mpc = gene.iloc[:,4] #mRNA expression experimental (molecules/cell), rounded up to nearest integer,
    pExp_mpc = gene.iloc[:,5] #proteomics expression experimental (molecules/cell)
    gExp_nM = gExp_mpc*mpc2nmcf_Vn
    mExp_nM=mExp_mpc*mpc2nmcf_Vc




    #Important indices
    numberofgenes=141
    numberofTARs=7

    indsCC = []
    for i in range(39,78):
        indsCC.append(i)

    indsDD = []
    for i in range(1,27):
        indsDD.append(i)

    indsM=121
    indsPIP2=690
    indsmT=772



    #  PARCDL prep
    #  PARCDL STOICHIOMETRIC MATRIX



    # original matlab code
    # not doing sparse for now. no easy way to do this in python. if memory becomes a problem, will write something
    # S_PARCDL=csvread('PARCDL_sm18.csv',1,1); S_PARCDL=S_PARCDL(:,1:end-1);
    # S_PARCDL=sparse(S_PARCDL);
    # S_TL=S_PARCDL(:,3:3+numberofgenes-1);
    # S_d=S_PARCDL(:,1844:end);



    # NOTE - CSV file
    data = []
    with open('PARCDL_sm18.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')
            data.append(x)


    S_PARCDL0 = []
    for row in data:
        S_PARCDL0.append(row[1:len(row)-1])

    # just fixing the dimensions of the matrix here

    S_PARCDL = []
    for row in S_PARCDL0:
        tmp = []
        for element in row:
            try:
                tmp.append(int(element))
            except:
                # tmp.append(0)
                pass

        S_PARCDL.append(tmp)






    S_TL = []
    for row in S_PARCDL:
        S_TL.append(row[2:3+numberofgenes-1])

    del S_TL[0]
    # deleting first row to make it match matlab
    S_TL = np.matrix(S_TL)







    S_d = []
    for row in S_PARCDL:
        S_d.append(row[1843:])

    del S_d[0]
    # deleting first row to make it match matlab
    S_d = np.matrix(S_d)




    # RATE CONSTANTS SYNTHESIS AND DEGRADATION
    EIF4Efree= np.multiply(kTLnat[130],mExp_nM[130])/kTLd[130];




    # NOTE - function call
    [kTLCd,kTL,kXd,xp_mpc] = PARCDL_rateconstants_sd(k50E,mExp_mpc,kTLnat,kTLd,EIF4Efree,S_TL,S_d);





    # RATE CONSTANTS MAIN
    # NOTE - function call
    kD,kC,kA,kR,kP, \
        kRP1,kRP2,kRP3,kRP4,kRP5,kRP6,kRP7,kRP8,kRP9,kRP10,kRP11,kRP12,kRP13,kRP14,kRP15,kRP16,kRP17,kRP18,kRP19,kRP20,kRP21,kRP22,kRP23,kRP24,kRP25,kRP26,kRP27,kRP28,kRP29,kRP30,kRP31,kRP32,kRP33,kRP34, \
        kDP,kPA = PARCDL_rateconstants_main(Vc,Ve,Vm,Vn);



    kE = np.zeros(shape=(3,1))
    kE[0,0]=kTLCd[101]*mT0;
    kE[1,0]=kTLCd[101];
    kE[2,0]=kTLCd[101];




    # PARCDL COMPARTMENTS
    # NOTE - function call
    flagOUT=[1,1,1];
    VxPARCDL,VvPARCDL,VxTL=PARCDL_compartments(flagOUT,Vc,Ve,Vm,Vn,S_d);




    # SET MANUAL INITIAL CONDITIONS
    CellCycleSpecies0=[80000,0.0023875,3.2308e-05,11012,0.0013746,0.0036083,0.018044,0.0037528,2.5164,8.7989,27.119,114.09,11.28,1412.9,489.7,160.2,552.84,39.644,138.62,52.721,13.158,207.98,6.0486,1087.9,116.34,42.027,420.6,34.408,38.992,6.8625,711.67,7.3241,94.317,265.18,167.41,0.85635,2.0389e-117,88094,0.0013145];

    CellCycleSpecies = []
    for item in CellCycleSpecies0:
        CellCycleSpecies.append(item/10)

    DNADamageSpecies=[296.62,6.2458,205.62,2.2305,0,0,6.2458,6.2458,6.2458,6.2457,6.2457,6.2457,6.2457,6.2457,6.2457,6.2457,6.2458,6.2458,6.2457,6.2457,6.2457,6.2457,6.2457,6.2457,6.2457,6.2457];



    # SPECIES
    xp_mpc = np.array(xp_mpc)
    # turn list(?) into numpy array

    pExp_nM=xp_mpc*(1E9/(VxTL*6.023E23));



    S_TL = np.array(S_TL)
    # turn list into numpy array




    x0PARCDL= np.dot(S_TL,pExp_nM)
    # IMPORTANT - when doing matrix multiplication (as opposed to element-wise) always use np.dot()
    # don't just say "matrix1 * matrix2"...... that works sometimes but not all the time. leads to weird product dimensions sometimes
    # just play it safe and use np.dot(matrix1,matrix2)


    x0PARCDL[0]=Rt;
    x0PARCDL[indsCC]=CellCycleSpecies;
    x0PARCDL[indsDD]=DNADamageSpecies;
    x0PARCDL[indsM]=M0;
    x0PARCDL[indsPIP2]=PIP2_0;
    x0PARCDL[indsmT]=mT0;




    # PARCDL Rate constant MODIFICATIONS
    # A
    kA[16]=kA[16]/100*10; #pC8 binding C6
    kA[13]=kA[13]/10000*10; #C3 binding pC6
    kA[12]=kA[12]/10000*10; #C8 cleaving pC3
    kA[25]=kA[25]/1000*10; #C8 binding to Bid
    kA[22]=kA[22]/1000*10; #C3 binding to PARP
    kA[[37,41]]=kA[[37,41]]*100000; #Baxm/Bax2 dimerization
    kA[[38,42]]=kA[[38,42]]*10000; #Bax2/Bax4 dissociation
    kA[63]=kA[63]/10000; #Apoptosome cleaving pC3
    kA[27]=kA[27]/10000; #C8 cleaving Bid
    kA[[49,52]]=kA[[49,52]]*1000; #koff CytochromeC Open Mitochondiral Pores.
    kA[[50,53]]=kA[[50,53]]/100; #Catalytic constant for above reaction.
    kA[2]=kA[2]/10; #Ligand-bound receptor becomming activated.
    kA[84]=0.001; #Translocation to mito, BCL2c
    kA[85]=0.1; #Translocation to cyto
    kA[86]=0; #Basal pC8 cleavage. Set during initialization.
    kA[76]=0; #BIM binding Bax


    # P
    kP[102]=0;
    kP[59]=0;
    kP[[116,120,177,178]]=kP[[116,120,177,178]]*0.1;
    kP[153]=kP[153]/10;
    kP[157]=0.001*5;


    # PA
    kPA[3]=kPA[3]*5;

    # C
    kC[[58,45,47,49]]=kC[[58,45,47,49]]/5;



    # kXd
    kXd[1]=kXd[1]*1000;
    kXd[[4,7,9,15,18]]=kXd[[4,7,9,15,18]]*100;
    kXd[43]=kXd[43]*10;
    kXd[45]=kXd[45]*10;
    kXd[561]=kXd[561]*10;




    # gm
    indsD = [5,6,7,8,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]


    # NOTE - function call
    xgac_mpc,xgin_mpc,xgac_mpc_D,xgin_mpc_D,kTCleak,AllGenesVec,GenePositionMatrix = gm_Prep(mExp_mpc,gExp_mpc,kTCd,kGac,kGin,numberofgenes);




    # Set kTCmaxs
    kTCmax=0.1;
    kTCmaxs=np.ones(shape=(numberofgenes,1))*kTCmax;


    # Transcriptional Activators
    tcnas=np.ones(shape = (numberofgenes,numberofTARs)); #Number of genes by number of TARs.
    tcnas[9:12,0]=3; #pcFos_cJun act
    tcnas[98,0]=3; #pcFos_cJun act on cJun
    tcnas[9:12,1]=3; #cMyc act
    tcnas[[25,52,53],2]=4; #p53ac
    tcnas[[54,57,58,59,60,62,64,65,126,127,135,139],3]=4; #FOXOnuc
    tcnas[[67,91,96,97],4]=4; #ppERKnuc
    tcnas[[67,91,96,97],5]=4; #pRSKnuc
    tcnas[99,6]=4; #bCATENIN


    # Transcriptional Repressors
    tcnrs=np.ones(shape = (numberofgenes,numberofTARs));
    tcnrs[97,0]=4;

    # k50 for TAR Activation
    tck50as=np.zeros(shape = (numberofgenes,numberofTARs));


    # pcFos_cJun
    tck50as[9:12,0]=1.25; #CyclinD
    tck50as[98,0]=0.8; #cJun
    # cMyc
    tck50as[9:12,1]=450; #CyclinD
    # p53ac
    tck50as[25,2]=50;#p21
    tck50as[52:54,2]=1350;#PUMA,NOXA
    # FOXO
    tck50as[54,3]=45;#19
    tck50as[[57,58,59,60,62,64,65,126,127,135,139],3]=60; #RTKs
    # ppERKnuc
    tck50as[67,4]=65; #SPRY2
    tck50as[[91,96],4]=40; #DUSPs
    tck50as[97,4]=20; #cFos
    # pRSKnuc
    tck50as[67,5]=20; #SPRY2
    tck50as[[91,96],5]=10; #DUSPs
    tck50as[97,5]=5; #cFos
    # bCATENINnuc
    tck50as[99,6]=250;#cMyc


    # k50 for TAR Repression
    tck50rs = np.zeros(shape = (numberofgenes,numberofTARs))
    tck50rs[97,0]=tck50as[98,0]; #cFos

    # Convert to molecules per cell
    tck50as=tck50as*(1/mpc2nmcf_Vn);
    tck50rs=tck50rs*(1/mpc2nmcf_Vn);



    # SAVE PARAMETERS IN STRUCTURE

    # stuff to flatten
    kS_toAdd=[Rt,
    EIF4Efree,
    Vc,
    Ve,
    Vm,
    Vn,
    kT1,
    kT2,
    kT3,
    kT4,
    k50E,
    kbR0,
    kbRi,
    kdR0,
    nR,
    k50R,
    kTL,
    kTLd,
    kTLCd,
    kD,
    kC,
    kA,
    kR,
    kP,
    kRP1,
    kRP2,
    kRP3,
    kRP4,
    kRP5,
    kRP6,
    kRP7,
    kRP8,
    kRP9,
    kRP10,
    kRP11,
    kRP12,
    kRP13,
    kRP14,
    kRP15,
    kRP16,
    kRP17,
    kRP18,
    kRP19,
    kRP20,
    kRP21,
    kRP22,
    kRP23,
    kRP24,
    kRP25,
    kRP26,
    kRP27,
    kRP28,
    kRP29,
    kRP30,
    kRP31,
    kRP32,
    kRP33,
    kRP34,
    kDP,
    kPA,
    kXd,
    kE];









    kS = []

    # flattening to put into kS array
    for item in kS_toAdd:
        try:
            for element in item:
                kS.append(element)
        except:
            kS.append(item)

    kS = np.array(kS)






    flagE = 1
    class dataS:
        def __init__(self, ts, x0PARCDL, kS, VvPARCDL, VxPARCDL, S_PARCDL, mExp_nM, pExp_nM, flagE):
            self.ts=ts; #time step
            self.x0PARCDL=x0PARCDL;
            self.kS=kS;
            self.VvPARCDL=VvPARCDL;
            self.VxPARCDL=VxPARCDL;
            self.S_PARCDL=S_PARCDL;
            self.mExp_nM=mExp_nM;
            self.mMod=mExp_nM;
            self.pExp_nM=pExp_nM;
            self.flagE=flagE;





    del S_PARCDL[0]
    S_PARCDL = np.matrix(S_PARCDL)
    # need to format S_PARCDL correctly before putting it into dataS object




    dataS_struct = dataS(ts, x0PARCDL, kS, VvPARCDL, VxPARCDL, S_PARCDL, mExp_nM, pExp_nM, flagE)
    # this is one of the objects that will be returned at the end




    # CALCULATE CELL CYCLE mRNAs

    indsccx = [5,6,7,8,12,13,14,15,16,17,18,19,20,21,22,23,24]
    mExp_mpc[indsccx]=17;
    mExp_nM[indsccx]=mExp_mpc[indsccx]*mpc2nmcf_Vc;





    # UPDATE CERTAIN DATA SPECIES
    dataS_struct.mExp_nM=mExp_nM;
    dataS_struct.mMod=mExp_nM;


    # dataG
    x0gm_mpc=[xgac_mpc,xgin_mpc,mExp_mpc];
    x0gm_mpc_D=[xgac_mpc_D,xgin_mpc_D,mExp_mpc];

    # flattening
    new_x0gm_mpc = []
    for item in x0gm_mpc:
        for element in item:
            try:
                new_x0gm_mpc.append(float(element))
            except:
                pass

    new_x0gm_mpc = np.matrix.transpose(np.matrix(new_x0gm_mpc))

    new_x0gm_mpc_D = []
    for item in x0gm_mpc_D:
        for element in item:
            try:
                new_x0gm_mpc_D.append(float(element))
            except:
                pass

    new_x0gm_mpc_D = np.matrix.transpose(np.matrix(new_x0gm_mpc_D))



    class dataG:
        def __init__(self, x0gm_mpc, x0gm_mpc_D, kGin, kGac, kTCleak, kTCmaxs, kTCd, tcnas, tcnrs, tck50as, tck50rs, GenePositionMatrix, AllGenesVec, Vn, indsD):
            self.x0gm_mpc=x0gm_mpc;
            self.x0gm_mpc_D=x0gm_mpc_D;
            self.kGin=kGin;
            self.kGac=kGac;
            self.kTCleak=kTCleak;
            self.kTCmaxs=kTCmaxs;
            self.kTCd=kTCd;
            self.tcnas=tcnas;
            self.tcnrs=tcnrs;
            self.tck50as=tck50as;
            self.tck50rs=tck50rs;
            self.GenePositionMatrix=GenePositionMatrix;
            self.AllGenesVec=AllGenesVec;
            self.Vn=Vn;
            self.indsD=indsD;

    dataG_struct = dataG(new_x0gm_mpc, new_x0gm_mpc_D, kGin, kGac, kTCleak, kTCmaxs, kTCd, tcnas, tcnrs, tck50as, tck50rs, GenePositionMatrix, AllGenesVec, Vn, np.array(indsD))
    # this is the second object that will be returned




    return dataS_struct, dataG_struct








# testing

# print(RunPrep()[1].x0gm_mpc.shape)
# print(RunPrep()[1].x0gm_mpc_D.shape)

# # RunPrep()
#
# print("done")
