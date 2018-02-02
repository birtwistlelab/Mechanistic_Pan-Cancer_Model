import numpy as np
import sys
from RunPrep import *

from assimulo.solvers import CVode
from assimulo.solvers import LSODAR

from assimulo.problem import Explicit_Problem


class MyProblem(Explicit_Problem):
    def __init__(self, y0,dataS):
        Explicit_Problem.__init__(self,y0=y0)
        self.dataS = dataS



    #Define the rhs

    def rhs(self,t,x):

        # returns [ydot,flag,newdata,v]


        # data = RunPrep()[0]
        #
        # kC173 = float(open(pathi + "i_kC173.txt").read())
        # kC82 = float(open(pathi + "i_kC82.txt").read())
        # kA77 = float(open(pathi + "i_kA77.txt").read())*5
        #
        # # ^ forgot to add the *5 to this line and spent sooooo long looking for this mistake lol
        #
        #
        # kA87 = float(open(pathi + "i_kA87.txt").read())
        # Rt = float(open(pathi + "i_Rt.txt").read())
        # EIF4Efree = float(open(pathi + "i_EIF4Efree.txt").read())
        # kDDbasal = float(open(pathi + "i_kDDbasal.txt").read())
        #
        #
        # data.kS[0]=Rt;
        # data.kS[1]=EIF4Efree;
        # data.kS[11]=kbR0;
        # data.kS[16:157]=kTL;
        # data.kS[631]=kC173;
        # data.kS[540]=kC82;
        # data.kS[708]=kA77;
        # data.kS[718]=kA87;
        # data.kS[449]=kDDbasal;


        data = self.dataS

        # # unpacking
        kS=data.kS;
        VvPARCDL=data.VvPARCDL;
        VxPARCDL=data.VxPARCDL;
        S_PARCDL=data.S_PARCDL;
        mExp_nM=data.mExp_nM;
        mMod=data.mMod;
        flagE=data.flagE;


        # k
        a=0;
        u=1;Rt=kS[a:a+u];a=a+u;
        u=1;EIF4Efree=kS[a:a+u];a=a+u;
        u=1;Vc=kS[a:a+u];a=a+u;
        u=1;Ve=kS[a:a+u];a=a+u;
        u=1;Vm=kS[a:a+u];a=a+u;
        u=1;Vn=kS[a:a+u];a=a+u;
        u=1;kT1=kS[a:a+u];a=a+u;
        u=1;kT2=kS[a:a+u];a=a+u;
        u=1;kT3=kS[a:a+u];a=a+u;
        u=1;kT4=kS[a:a+u];a=a+u;
        u=1;k50E=kS[a:a+u];a=a+u;
        u=1;kbR0=kS[a:a+u];a=a+u;
        u=1;kbRi=kS[a:a+u];a=a+u;
        u=1;kdR0=kS[a:a+u];a=a+u;
        u=1;nR=kS[a:a+u];a=a+u;
        u=1;k50R=kS[a:a+u];a=a+u;
        u=141;kTL=kS[a:a+u];a=a+u;
        u=141;kTLd=kS[a:a+u];a=a+u;
        u=102;kTLCd=kS[a:a+u];a=a+u;
        u=59;kD=kS[a:a+u];a=a+u;
        u=173;kC=kS[a:a+u];a=a+u;


        u=87;kA=kS[a:a+u];a=a+u;



        u=158;kR=kS[a:a+u];a=a+u;
        u=190;kP=kS[a:a+u];a=a+u;
        u=29;kRP1=kS[a:a+u];a=a+u;
        u=29;kRP2=kS[a:a+u];a=a+u;
        u=29;kRP3=kS[a:a+u];a=a+u;
        u=29;kRP4=kS[a:a+u];a=a+u;
        u=29;kRP5=kS[a:a+u];a=a+u;
        u=29;kRP6=kS[a:a+u];a=a+u;
        u=29;kRP7=kS[a:a+u];a=a+u;
        u=29;kRP8=kS[a:a+u];a=a+u;
        u=29;kRP9=kS[a:a+u];a=a+u;
        u=29;kRP10=kS[a:a+u];a=a+u;
        u=29;kRP11=kS[a:a+u];a=a+u;
        u=29;kRP12=kS[a:a+u];a=a+u;
        u=29;kRP13=kS[a:a+u];a=a+u;
        u=29;kRP14=kS[a:a+u];a=a+u;
        u=29;kRP15=kS[a:a+u];a=a+u;
        u=29;kRP16=kS[a:a+u];a=a+u;
        u=29;kRP17=kS[a:a+u];a=a+u;
        u=29;kRP18=kS[a:a+u];a=a+u;
        u=29;kRP19=kS[a:a+u];a=a+u;
        u=29;kRP20=kS[a:a+u];a=a+u;
        u=29;kRP21=kS[a:a+u];a=a+u;
        u=29;kRP22=kS[a:a+u];a=a+u;
        u=29;kRP23=kS[a:a+u];a=a+u;
        u=29;kRP24=kS[a:a+u];a=a+u;
        u=29;kRP25=kS[a:a+u];a=a+u;
        u=29;kRP26=kS[a:a+u];a=a+u;
        u=29;kRP27=kS[a:a+u];a=a+u;
        u=29;kRP28=kS[a:a+u];a=a+u;
        u=29;kRP29=kS[a:a+u];a=a+u;
        u=29;kRP30=kS[a:a+u];a=a+u;
        u=29;kRP31=kS[a:a+u];a=a+u;
        u=29;kRP32=kS[a:a+u];a=a+u;
        u=29;kRP33=kS[a:a+u];a=a+u;
        u=16;kRP34=kS[a:a+u];a=a+u;
        u=4;kDP=kS[a:a+u];a=a+u;
        u=11;kPA=kS[a:a+u];a=a+u;
        u=606;kXd=kS[a:a+u];a=a+u;




        u=3;kE=kS[a-1:a+u];
        # fixed kE bug here




        # ## Defining Entities
        a=0;
        xRibosome=x[a];a=a+1;
        xD=x[a:a+38];a=a+38;
        xC=x[a:a+44];a=a+44;
        xA=x[a:a+72];a=a+72;
        xR=x[a:a+73];a=a+73;
        xRP=x[a:a+414];a=a+414;
        xP=x[a:a+130];a=a+130;
        xE=x[a:a+2];


        # ## xD **
        p53inac =xD[1-1];
        p53ac =xD[2-1];
        Mdm2 =xD[3-1];
        Wip1 =xD[4-1];
        ATMP =xD[5-1];
        ATRac =xD[6-1];
        Mdm2product1=xD[7-1];
        Mdm2product2=xD[8-1];
        Mdm2product3=xD[9-1];
        Mdm2product4=xD[10-1];
        Mdm2product5=xD[11-1];
        Mdm2product6=xD[12-1];
        Mdm2product7=xD[13-1];
        Mdm2product8=xD[14-1];
        Mdm2product9=xD[15-1];
        Mdm2pro =xD[16-1];
        Wip1product1=xD[17-1];
        Wip1product2=xD[18-1];
        Wip1product3=xD[19-1];
        Wip1product4=xD[20-1];
        Wip1product5=xD[21-1];
        Wip1product6=xD[22-1];
        Wip1product7=xD[23-1];
        Wip1product8=xD[24-1];
        Wip1product9=xD[25-1];
        Wip1pro =xD[26-1];
        BRCA2=xD[27-1];
        MSH6=xD[28-1];
        MGMT=xD[29-1];
        damageDSB=xD[30-1];
        damageSSB=xD[31-1];
        ppAKT_Mdm2=xD[32-1];
        pMdm2=xD[33-1];
        ARF=xD[34-1];
        MDM4=xD[35-1];
        p53ac_MDM4=xD[36-1];
        ATMinac=xD[37-1];
        ATRinac=xD[38-1];



        # ## xC **
        pRB=xC[1-1];
        pRBp=xC[2-1];
        pRBpp=xC[3-1];
        E2F=xC[4-1];
        Cd=xC[5-1];
        Mdi=xC[6-1];
        Md=xC[7-1];
        Mdp27=xC[8-1];
        Ce=xC[9-1];
        Mei=xC[10-1];
        Me=xC[11-1];
        Skp2=xC[12-1];
        Mep27=xC[13-1];
        Pe=xC[14-1];
        Pai=xC[15-1];
        Pei=xC[16-1];
        Pbi=xC[17-1];
        Ca=xC[18-1];
        Mai=xC[19-1];
        Ma=xC[20-1];
        Map27=xC[21-1];
        p27=xC[22-1];
        Cdh1i=xC[23-1];
        Cdh1a=xC[24-1];
        E2Fp=xC[25-1];
        p27p=xC[26-1];
        Pa=xC[27-1];
        Cb=xC[28-1];
        Mbi=xC[29-1];
        Mb=xC[30-1];
        Cdc20i=xC[31-1];
        Cdc20a=xC[32-1];
        Pb=xC[33-1];
        Wee1=xC[34-1];
        Wee1p=xC[35-1];
        Mbp27=xC[36-1];
        Chk1=xC[37-1];
        pRBc1=xC[38-1];
        pRBc2=xC[39-1];
        p21=xC[40-1];
        Mdp21=xC[41-1];
        Mep21=xC[42-1];
        Map21=xC[43-1];
        Mbp21=xC[44-1];



        # ## xA **
        L =xA[1-1];
        R =xA[2-1];
        L_R =xA[3-1];
        Ractive =xA[4-1];
        flip =xA[5-1];
        Ractive_flip =xA[6-1];
        pC8 =xA[7-1];
        Ractive_pC8 =xA[8-1];
        C8 =xA[9-1];
        Bar =xA[10-1];
        C8_Bar =xA[11-1];
        pC3 =xA[12-1];
        C8_pC3 =xA[13-1];
        C3 =xA[14-1];
        pC6 =xA[15-1];
        C3_pC6 =xA[16-1];
        C6 =xA[17-1];
        C6_C8 =xA[18-1];
        XIAP =xA[19-1];
        C3_XIAP =xA[20-1];
        PARP =xA[21-1];
        C3_PARP =xA[22-1];
        cPARP =xA[23-1];
        Bid =xA[24-1];
        C8_Bid =xA[25-1];
        tBid =xA[26-1];
        Bcl2c =xA[27-1];
        tBid_Bcl2c =xA[28-1];
        Bax =xA[29-1];
        tBid_Bax =xA[30-1];
        Baxactive =xA[31-1];
        Baxm =xA[32-1];
        Bcl2 =xA[33-1];
        Baxm_Bcl2 =xA[34-1];
        Bax2 =xA[35-1];
        Bax2_Bcl2 =xA[36-1];
        Bax4 =xA[37-1];
        Bax4_Bcl2 =xA[38-1];
        M =xA[39-1];
        Bax4_M =xA[40-1];
        Mactive =xA[41-1];
        CytoCm =xA[42-1];
        Mactive_CytoCm =xA[43-1];
        CytoCr =xA[44-1];
        Smacm =xA[45-1];
        Mactive_Smacm =xA[46-1];
        Smacr =xA[47-1];
        CytoC =xA[48-1];
        Apaf =xA[49-1];
        CytoC_Apaf =xA[50-1];
        Apafactive =xA[51-1];
        pC9 =xA[52-1];
        Apop =xA[53-1];
        Apop_C3 =xA[54-1];
        Smac =xA[55-1];
        Apop_XIAP =xA[56-1];
        Smac_XIAP =xA[57-1];
        C3_Ub =xA[58-1];
        BAD=xA[59-1];
        PUMA=xA[60-1];
        NOXA=xA[61-1];
        Bcl2c_BAD=xA[62-1];
        Bcl2c_PUMA=xA[63-1];
        Bcl2c_NOXA=xA[64-1];
        BIM=xA[65-1];
        BIM_Bax=xA[66-1];
        Bcl2c_BIM=xA[67-1];
        ppERK_BIM=xA[68-1];
        pBIM=xA[69-1];
        ppAKT_BAD=xA[70-1];
        pBAD=xA[71-1];
        ppERK_BAD=xA[72-1]


        ### xR **
        E=xR[1-1];
        H=xR[2-1];
        HGF=xR[3-1];
        P=xR[4-1];
        F=xR[5-1];
        I=xR[6-1];
        IN=xR[7-1];
        E1=xR[8-1];
        pE1=xR[9-1];
        E2=xR[10-1];
        pE2=xR[11-1];
        E3=xR[12-1];
        E4=xR[13-1];
        pE4=xR[14-1];
        Ev3=xR[15-1];
        Met=xR[16-1];
        Pr=xR[17-1];
        Fr=xR[18-1];
        Ir=xR[19-1];
        Isr =xR[20-1];
        E1E1=xR[21-1];
        E1E2=xR[22-1];
        E1E3=xR[23-1];
        E1E4=xR[24-1];
        E2E2=xR[25-1];
        E2E3=xR[26-1];
        E2E4=xR[27-1];
        E3E4=xR[28-1];
        E4E4=xR[29-1];
        Met_Met=xR[30-1];
        FrFr=xR[31-1];
        IrIr=xR[32-1];
        Isr_Isr=xR[33-1];
        EE1=xR[34-1];
        HE3=xR[35-1];
        HE4=xR[36-1];
        HGF_Met=xR[37-1];
        PPr=xR[38-1];
        FFr=xR[39-1];
        EE1E2=xR[40-1];
        EE1Ev3=xR[41-1];
        EE1E1=xR[42-1];
        EE1E3=xR[43-1];
        EE1E4=xR[44-1];
        E2HE3=xR[45-1];
        E1HE3=xR[46-1];
        HE3E3=xR[47-1];
        HE3Ev3=xR[48-1];
        HE3E4=xR[49-1];
        E2HE4=xR[50-1];
        HE4Ev3=xR[51-1];
        E1HE4=xR[52-1];
        E3HE4=xR[53-1];
        HE4E4=xR[54-1];
        HGF_Met_Met=xR[55-1];
        PPrPr=xR[56-1];
        FFrFr=xR[57-1];
        IIrIr=xR[58-1];
        IN_Isr_Isr=xR[59-1];
        EE1EE1=xR[60-1];
        EE1HE3=xR[61-1];
        EE1HE4=xR[62-1];
        HE3HE3=xR[63-1];
        HE3HE4=xR[64-1];
        HE4HE4=xR[65-1];
        HGF_Met_HGF_Met=xR[66-1];
        PPrPPr=xR[67-1];
        FFrFFr=xR[68-1];
        IIrIrI=xR[69-1];
        IN_Isr_Isr_IN=xR[70-1];
        E1_ppERK=xR[71-1];
        E2_ppERK=xR[72-1];
        E4_ppERK=xR[73-1];


        # ## xRP **
        a=0;
        SCD = [EE1E2,EE1Ev3,EE1E1,EE1EE1,EE1E3,EE1HE3,EE1E4,EE1HE4,E2HE3,HE3Ev3,E1HE3,HE3E4,HE3HE4,E2HE4,HE4Ev3,E1HE4,E3HE4,HE4E4,HE4HE4,HGF_Met_Met,HGF_Met_HGF_Met,PPrPPr,PPrPr,FFrFFr,FFrFr,IIrIr,IN_Isr_Isr,IIrIrI,IN_Isr_Isr_IN];
        SCD = np.array(SCD)




        pSCD = xRP[a:a+29]; a=a+33;


        Sp_SCD = xRP[a:a+29]; a=a+29;#[Sp_EE1E2,Sp_EE1Ev3,Sp_EE1E1,Sp_EE1EE1,Sp_EE1E3,Sp_EE1HE3,Sp_EE1E4,Sp_EE1HE4,Sp_E2HE3,Sp_HE3Ev3,Sp_E1HE3,Sp_HE3E4,Sp_HE3HE4,Sp_E2HE4,Sp_HE4Ev3,Sp_E1HE4,Sp_E3HE4,Sp_HE4E4,Sp_HE4HE4,Sp_HGF_Met_Met,Sp_HGF_Met_HGF_Met,Sp_PPrPPr,Sp_PPrPr,Sp_FFrFFr,Sp_FFrFr,Sp_IIrIr,Sp_IIrIIr];


        SCDint = xRP[a:a+29]; a=a+29;#[EE1E2int,EE1Ev3int,EE1E1int,EE1EE1int,EE1E3int,EE1HE3int,EE1E4int,EE1HE4int,E2HE3int,HE3Ev3int,E1HE3int,HE3E4int,HE3HE4int,E2HE4int,HE4Ev3int,E1HE4int,E3HE4int,HE4E4int,HE4HE4int,HGF_Met_Metint,HGF_Met_HGF_Metint,PPrPPrint,PPrPrint,FFrFFrint,FFrFrint,IIrIrint,IIrIIrint];


        pSCDint = xRP[a:a+29]; a=a+33;#[pEE1E2int,pEE1Ev3int,pEE1E1int,pEE1EE1int,pEE1E3int,pEE1HE3int,pEE1E4int,pEE1HE4int,pE2HE3int,pHE3Ev3int,pE1HE3int,pHE3E4int,pHE3HE4int,pE2HE4int,pHE4Ev3int,pE1HE4int,pE3HE4int,pHE4E4int,pHE4HE4int,pHGF_Met_Metint,pHGF_Met_HGF_Metint,pPPrPPrint,pPPrPrint,pFFrFFrint,pFFrFrint,pIIrIrint,pIIrIIrint];


        pSCD_bind = np.append(xRP[0:25],xRP[29:33]); #[pEE1E2,pEE1Ev3,pEE1E1,pEE1EE1,pEE1E3,pEE1HE3,pEE1E4,pEE1HE4,pE2HE3,pHE3Ev3,pE1HE3,pHE3E4,pHE3HE4,pE2HE4,pHE4Ev3,pE1HE4,pE3HE4,pHE4E4,pHE4HE4,pHGF_Met_Met,pHGF_Met_HGF_Met,pPPrPPr,pPPrPr,pFFrFFr,pFFrFr,pIIrIr_IRS,pIIrIIr_IRS]; #Same as pSCD but with the IRS on the IGF1R. Had to do this because it has an extra step (binding of IRS)
        pSCDint_bind = np.append(xRP[91:116],xRP[120:124]); #[pEE1E2int,pEE1Ev3int,pEE1E1int,pEE1EE1int,pEE1E3int,pEE1HE3int,pEE1E4int,pEE1HE4int,pE2HE3int,pHE3Ev3int,pE1HE3int,pHE3E4int,pHE3HE4int,pE2HE4int,pHE4Ev3int,pE1HE4int,pE3HE4int,pHE4E4int,pHE4HE4int,pHGF_Met_Metint,pHGF_Met_HGF_Metint,pPPrPPrint,pPPrPrint,pFFrFFrint,pFFrFrint,pIIrIrint_IRS,pIIrIIrint_IRS];




        pSCD_G2_SOS = xRP[a:a+29]; a=a+29; #[pEE1E2_G2_SOS,pEE1Ev3_G2_SOS,pEE1E1_G2_SOS,pEE1EE1_G2_SOS,pEE1E3_G2_SOS,pEE1HE3_G2_SOS,pEE1E4_G2_SOS,pEE1HE4_G2_SOS,pE2HE3_G2_SOS,pHE3Ev3_G2_SOS,pE1HE3_G2_SOS,pHE3E4_G2_SOS,pHE3HE4_G2_SOS,pE2HE4_G2_SOS,pHE4Ev3_G2_SOS,pE1HE4_G2_SOS,pE3HE4_G2_SOS,pHE4E4_G2_SOS,pHE4HE4_G2_SOS,pHGF_Met_Met_G2_SOS,pHGF_Met_HGF_Met_G2_SOS,pPPrPPr_G2_SOS,pPPrPr_G2_SOS,pFFrFFr_G2_SOS,pFFrFr_G2_SOS,pIIrIr_IRS_G2_SOS,pIIrIIr_IRS_G2_SOS];
        pSCDint_G2_SOS = xRP[a:a+29]; a=a+29; #[pEE1E2int_G2_SOS,pEE1Ev3int_G2_SOS,pEE1E1int_G2_SOS,pEE1EE1int_G2_SOS,pEE1E3int_G2_SOS,pEE1HE3int_G2_SOS,pEE1E4int_G2_SOS,pEE1HE4int_G2_SOS,pE2HE3int_G2_SOS,pHE3Ev3int_G2_SOS,pE1HE3int_G2_SOS,pHE3E4int_G2_SOS,pHE3HE4int_G2_SOS,pE2HE4int_G2_SOS,pHE4Ev3int_G2_SOS,pE1HE4int_G2_SOS,pE3HE4int_G2_SOS,pHE4E4int_G2_SOS,pHE4HE4int_G2_SOS,pHGF_Met_Metint_G2_SOS,pHGF_Met_HGF_Metint_G2_SOS,pPPrPPrint_G2_SOS,pPPrPrint_G2_SOS,pFFrFFrint_G2_SOS,pFFrFrint_G2_SOS,pIIrIrint_IRS_G2_SOS,pIIrIIrint_IRS_G2_SOS];




        pSCD_PLCg = xRP[a:a+29]; a=a+29; #[pEE1E2_PLCg,pEE1Ev3_PLCg,pEE1E1_PLCg,pEE1EE1_PLCg,pEE1E3_PLCg,pEE1HE3_PLCg,pEE1E4_PLCg,pEE1HE4_PLCg,pE2HE3_PLCg,pHE3Ev3_PLCg,pE1HE3_PLCg,pHE3E4_PLCg,pHE3HE4_PLCg,pE2HE4_PLCg,pHE4Ev3_PLCg,pE1HE4_PLCg,pE3HE4_PLCg,pHE4E4_PLCg,pHE4HE4_PLCg,pHGF_Met_Met_PLCg,pHGF_Met_HGF_Met_PLCg,pPPrPPr_PLCg,pPPrPr_PLCg,pFFrFFr_PLCg,pFFrFr_PLCg,pIIrIr_IRS_PLCg,pIIrIIr_IRS_PLCg];
        pSCD_PI3K1 = xRP[a:a+29]; a=a+29; #[pEE1E2_PI3K1,pEE1Ev3_PI3K1,pEE1E1_PI3K1,pEE1EE1_PI3K1,pEE1E3_PI3K1,pEE1HE3_PI3K1,pEE1E4_PI3K1,pEE1HE4_PI3K1,pE2HE3_PI3K1,pHE3Ev3_PI3K1,pE1HE3_PI3K1,pHE3E4_PI3K1,pHE3HE4_PI3K1,pE2HE4_PI3K1,pHE4Ev3_PI3K1,pE1HE4_PI3K1,pE3HE4_PI3K1,pHE4E4_PI3K1,pHE4HE4_PI3K1,pHGF_Met_Met_PI3K1,pHGF_Met_HGF_Met_PI3K1,pPPrPPr_PI3K1,pPPrPr_PI3K1,pFFrFFr_PI3K1,pFFrFr_PI3K1,pIIrIr_IRS_PI3K1,pIIrIIr_IRS_PI3K1];
        pSCD_PI3K2 = xRP[a:a+29]; a=a+29; #[pEE1E2_PI3K2,pEE1Ev3_PI3K2,pEE1E1_PI3K2,pEE1EE1_PI3K2,pEE1E3_PI3K2,pEE1HE3_PI3K2,pEE1E4_PI3K2,pEE1HE4_PI3K2,pE2HE3_PI3K2,pHE3Ev3_PI3K2,pE1HE3_PI3K2,pHE3E4_PI3K2,pHE3HE4_PI3K2,pE2HE4_PI3K2,pHE4Ev3_PI3K2,pE1HE4_PI3K2,pE3HE4_PI3K2,pHE4E4_PI3K2,pHE4HE4_PI3K2,pHGF_Met_Met_PI3K2,pHGF_Met_HGF_Met_PI3K2,pPPrPPr_PI3K2,pPPrPr_PI3K2,pFFrFFr_PI3K2,pFFrFr_PI3K2,pIIrIr_IRS_PI3K2,pIIrIIr_IRS_PI3K2];




        pSCDint_G2_SOS_RasD = xRP[a:a+29]; a=a+29; #[pEE1E2int_G2_SOS_RasDint,pEE1Ev3int_G2_SOS_RasDint,pEE1E1int_G2_SOS_RasDint,pEE1EE1int_G2_SOS_RasDint,pEE1E3int_G2_SOS_RasDint,pEE1HE3int_G2_SOS_RasDint,pEE1E4int_G2_SOS_RasDint,pEE1HE4int_G2_SOS_RasDint,pE2HE3int_G2_SOS_RasDint,pHE3Ev3int_G2_SOS_RasDint,pE1HE3int_G2_SOS_RasDint,pHE3E4int_G2_SOS_RasDint,pHE3HE4int_G2_SOS_RasDint,pE2HE4int_G2_SOS_RasDint,pHE4Ev3int_G2_SOS_RasDint,pE1HE4int_G2_SOS_RasDint,pE3HE4int_G2_SOS_RasDint,pHE4E4int_G2_SOS_RasDint,pHE4HE4int_G2_SOS_RasDint,pHGF_Met_Metint_G2_SOS_RasDint,pHGF_Met_HGF_Metint_G2_SOS_RasDint,pPPrPPrint_G2_SOS_RasDint,pPPrPrint_G2_SOS_RasDint,pFFrFFrint_G2_SOS_RasDint,pFFrFrint_G2_SOS_RasDint,pIIrIrint_IRS_G2_SOS_RasDint,pIIrIIrint_IRS_G2_SOS_RasDint];
        pSCD_G2_SOS_RasD = xRP[a:a+29]; a=a+29; #[pEE1E2_G2_SOS_RasD,pEE1Ev3_G2_SOS_RasD,pEE1E1_G2_SOS_RasD,pEE1EE1_G2_SOS_RasD,pEE1E3_G2_SOS_RasD,pEE1HE3_G2_SOS_RasD,pEE1E4_G2_SOS_RasD,pEE1HE4_G2_SOS_RasD,pE2HE3_G2_SOS_RasD,pHE3Ev3_G2_SOS_RasD,pE1HE3_G2_SOS_RasD,pHE3E4_G2_SOS_RasD,pHE3HE4_G2_SOS_RasD,pE2HE4_G2_SOS_RasD,pHE4Ev3_G2_SOS_RasD,pE1HE4_G2_SOS_RasD,pE3HE4_G2_SOS_RasD,pHE4E4_G2_SOS_RasD,pHE4HE4_G2_SOS_RasD,pHGF_Met_Met_G2_SOS_RasD,pHGF_Met_HGF_Met_G2_SOS_RasD,pPPrPPr_G2_SOS_RasD,pPPrPr_G2_SOS_RasD,pFFrFFr_G2_SOS_RasD,pFFrFr_G2_SOS_RasD,pIIrIr_IRS_G2_SOS_RasD,pIIrIIr_IRS_G2_SOS_RasD];
        pSCD_PLCg_PIP2 = xRP[a:a+29]; a=a+29; #[pEE1E2_PLCg_PIP2,pEE1Ev3_PLCg_PIP2,pEE1E1_PLCg_PIP2,pEE1EE1_PLCg_PIP2,pEE1E3_PLCg_PIP2,pEE1HE3_PLCg_PIP2,pEE1E4_PLCg_PIP2,pEE1HE4_PLCg_PIP2,pE2HE3_PLCg_PIP2,pHE3Ev3_PLCg_PIP2,pE1HE3_PLCg_PIP2,pHE3E4_PLCg_PIP2,pHE3HE4_PLCg_PIP2,pE2HE4_PLCg_PIP2,pHE4Ev3_PLCg_PIP2,pE1HE4_PLCg_PIP2,pE3HE4_PLCg_PIP2,pHE4E4_PLCg_PIP2,pHE4HE4_PLCg_PIP2,pHGF_Met_Met_PLCg_PIP2,pHGF_Met_HGF_Met_PLCg_PIP2,pPPrPPr_PLCg_PIP2,pPPrPr_PLCg_PIP2,pFFrFFr_PLCg_PIP2,pFFrFr_PLCg_PIP2,pIIrIr_IRS_PLCg_PIP2,pIIrIIr_IRS_PLCg_PIP2];
        pSCD_PI3K1_PIP2 = xRP[a:a+29]; a=a+29; #[pEE1E2_PI3K1_PIP2,pEE1Ev3_PI3K1_PIP2,pEE1E1_PI3K1_PIP2,pEE1EE1_PI3K1_PIP2,pEE1E3_PI3K1_PIP2,pEE1HE3_PI3K1_PIP2,pEE1E4_PI3K1_PIP2,pEE1HE4_PI3K1_PIP2,pE2HE3_PI3K1_PIP2,pHE3Ev3_PI3K1_PIP2,pE1HE3_PI3K1_PIP2,pHE3E4_PI3K1_PIP2,pHE3HE4_PI3K1_PIP2,pE2HE4_PI3K1_PIP2,pHE4Ev3_PI3K1_PIP2,pE1HE4_PI3K1_PIP2,pE3HE4_PI3K1_PIP2,pHE4E4_PI3K1_PIP2,pHE4HE4_PI3K1_PIP2,pHGF_Met_Met_PI3K1_PIP2,pHGF_Met_HGF_Met_PI3K1_PIP2,pPPrPPr_PI3K1_PIP2,pPPrPr_PI3K1_PIP2,pFFrFFr_PI3K1_PIP2,pFFrFr_PI3K1_PIP2,pIIrIr_IRS_PI3K1_PIP2,pIIrIIr_IRS_PI3K1_PIP2];
        pSCD_PI3K2_PIP = xRP[a:a+29]; #[pEE1E2_PI3K2_PIP,pEE1Ev3_PI3K2_PIP,pEE1E1_PI3K2_PIP,pEE1EE1_PI3K2_PIP,pEE1E3_PI3K2_PIP,pEE1HE3_PI3K2_PIP,pEE1E4_PI3K2_PIP,pEE1HE4_PI3K2_PIP,pE2HE3_PI3K2_PIP,pHE3Ev3_PI3K2_PIP,pE1HE3_PI3K2_PIP,pHE3E4_PI3K2_PIP,pHE3HE4_PI3K2_PIP,pE2HE4_PI3K2_PIP,pHE4Ev3_PI3K2_PIP,pE1HE4_PI3K2_PIP,pE3HE4_PI3K2_PIP,pHE4E4_PI3K2_PIP,pHE4HE4_PI3K2_PIP,pHGF_Met_Met_PI3K2_PIP,pHGF_Met_HGF_Met_PI3K2_PIP,pPPrPPr_PI3K2_PIP,pPPrPr_PI3K2_PIP,pFFrFFr_PI3K2_PIP,pFFrFr_PI3K2_PIP,pIIrIr_IRS_PI3K2_PIP,pIIrIIr_IRS_PI3K2_PIP];




        # # Need these independently because of binding to IRS
        pIIrIr=xRP[26-1];
        pIN_Isr_Isr=xRP[27-1];
        pIIrIrI=xRP[28-1];
        pIN_Isr_Isr_IN=xRP[29-1];
        pIIrIr_IRS=xRP[30-1];
        pIN_Isr_Isr_IRS=xRP[31-1];
        pIIrIrI_IRS=xRP[32-1];
        pIN_Isr_Isr_IN_IRS=xRP[33-1];



        pIIrIr_int=xRP[117-1];
        pIN_Isr_Isr_int=xRP[118-1];
        pIIrIrI_int=xRP[119-1];
        pIN_Isr_Isr_IN_int=xRP[120-1];
        pIIrIr_int_IRS=xRP[121-1];
        pIN_Isr_Isr_int_IRS=xRP[122-1];
        pIIrIrI_int_IRS=xRP[123-1];
        pIN_Isr_Isr_IN_int_IRS=xRP[124-1];



        # ## xP **
        IRS=xP[1-1];
        Sp=xP[2-1];
        Cbl=xP[3-1];
        G2=xP[4-1];
        G2_SOS=xP[5-1];
        G2_pSOS=xP[6-1];
        PLCg=xP[7-1];
        PI3KC1=xP[8-1];
        PI3KR1=xP[9-1];
        PI3K1=xP[10-1];
        pPI3K1=xP[11-1];
        PI3K2=xP[12-1];
        mTORC1=xP[13-1];
        mTORC1active=xP[14-1];
        PIP=xP[15-1];




        PI3P=xP[16-1];
        DAG=xP[17-1];
        GRP=xP[18-1];
        DAG_GRP=xP[19-1];
        RasT=xP[20-1];
        RasD=xP[21-1];
        NF1=xP[22-1];
        pNF1=xP[23-1];
        pCRaf=xP[24-1];
        CRaf=xP[25-1];
        RasT_CRaf=xP[26-1];
        BRaf=xP[27-1];
        RasT_CRaf_BRaf=xP[28-1];
        MEK=xP[29-1];
        pMEK=xP[30-1];
        ppMEK=xP[31-1];
        MKP3=xP[32-1];
        ERKnuc=xP[33-1];
        ppERKnuc=xP[34-1];
        RSK=xP[35-1];
        pRSK=xP[36-1];
        pRSKnuc=xP[37-1];
        MKP1=xP[38-1];
        pMKP1=xP[39-1];
        cFos=xP[40-1];
        pcFos=xP[41-1];
        cJun=xP[42-1];
        pcFos_cJun=xP[43-1];
        cMyc=xP[44-1];
        bCATENINnuc=xP[45-1];
        bCATENIN=xP[46-1];
        pbCATENIN=xP[47-1];
        IP3=xP[48-1];
        PIP2=xP[49-1];
        PIP3=xP[50-1];
        PTEN=xP[51-1];
        PIP3_AKT=xP[52-1];
        AKT=xP[53-1];


        pAKT=xP[54-1];
        ppAKT=xP[55-1];
        PDK1=xP[56-1];
        PIP3_PDK1=xP[57-1];
        PIP3_pAKT=xP[58-1];
        Rictor=xP[59-1];
        mTOR=xP[60-1];
        mTORC2=xP[61-1];
        PIP3_ppAKT=xP[62-1];
        GSK3b=xP[63-1];
        pGSK3b=xP[64-1];
        TSC1=xP[65-1];
        TSC2=xP[66-1];
        pTSC2=xP[67-1];
        TSC=xP[68-1];
        PKC=xP[69-1];
        DAG_PKC=xP[70-1];
        pRKIP=xP[71-1];
        RKIP=xP[72-1];
        RKIP_CRaf=xP[73-1];
        ERK=xP[74-1];
        pERK=xP[75-1];
        ppERK=xP[76-1];
        FOXO=xP[77-1];
        pFOXO=xP[78-1];
        RhebD=xP[79-1];
        RhebT=xP[80-1];
        Raptor=xP[81-1];
        S6K=xP[82-1];
        pS6K=xP[83-1];
        EIF4EBP1=xP[84-1];
        pEIF4EBP1=xP[85-1];
        SOS=xP[86-1];
        G2_SOS_ppERK=xP[87-1];
        CRaf_ppERK=xP[88-1];
        RasD_DAG_GRP=xP[89-1];
        RasT_NF1=xP[90-1];
        NF1_ppERK=xP[91-1];
        MEK_RasT_CRaf_BRaf=xP[92-1];
        pMEK_RasT_CRaf_BRaf=xP[93-1];
        ERK_ppMEK=xP[94-1];
        pERK_ppMEK=xP[95-1];
        RSK_ppERK=xP[96-1];
        pRSKnuc_MKP1=xP[97-1];
        ppERKnuc_MKP1=xP[98-1];
        cFos_pRSKnuc=xP[99-1];
        cFos_ppERKnuc=xP[100-1];
        RKIP_DAG_PKC=xP[101-1];
        PIP3_PTEN=xP[102-1];
        PIP3_AKT_PIP3_PDK1=xP[103-1];
        PIP3_pAKT_mTORC2=xP[104-1];
        GSK3b_ppAKT=xP[105-1];
        bCATENIN_GSK3b=xP[106-1];
        TSC2_ppAKT=xP[107-1];
        TSC2_ppERK=xP[108-1];
        RhebT_TSC=xP[109-1];
        EIF4EBP1_mTORC1active=xP[110-1];
        S6K_mTORC1active=xP[111-1];
        FOXO_ppAKT=xP[112-1];
        PI3K1_mTORC1active=xP[113-1];
        pERK_MKP3=xP[114-1];
        ppERK_MKP3=xP[115-1];
        ppERKnuc_pMKP1=xP[116-1];
        RasT_BRaf=xP[117-1];
        RasT_BRaf_BRaf=xP[118-1];
        MEK_RasT_BRaf_BRaf=xP[119-1];
        pMEK_RasT_BRaf_BRaf=xP[120-1];
        EIF4E=xP[121-1];
        EIF4EBP1_EIF4E=xP[122-1];
        RasT_CRaf_CRaf=xP[123-1];
        MEK_RasT_CRaf_CRaf=xP[124-1];
        pMEK_RasT_CRaf_CRaf=xP[125-1];
        FOXOnuc=xP[126-1];

        MEKi=xP[127-1];
        MEKi_ppMEK=xP[128-1];
        AKTi=xP[129-1];
        AKTi_AKT=xP[130-1];



        # ###### RATE CONSTANTS ASSIGNMENT

        # ###DNA Damage Rate Constants
        bp=kD[1-1];
        ampi=kD[2-1];
        api=kD[3-1];
        bsp=kD[4-1];
        ns=kD[5-1];
        Ts=kD[6-1];
        ampa=kD[7-1];
        awpa=kD[8-1];
        bm=kD[9-1];
        bmi=kD[10-1];
        am=kD[11-1];
        asm=kD[12-1];
        bw=kD[13-1];
        aw=kD[14-1];
        asm2=kD[15-1];
        aws=kD[16-1];
        nw=kD[17-1];
        Tw=kD[18-1];



        as_=kD[19-1];
        # NOTE - had to change name of this variable because "as" is a reserved word in python


        bs=kD[20-1];
        bs2=kD[21-1];
        tau1=kD[22-1];
        tau2=kD[23-1];
        tau3=kD[24-1];
        tau4=kD[25-1];
        tau5=kD[26-1];
        tau6=kD[27-1];
        tau7=kD[28-1];
        tau8=kD[29-1];
        tau9=kD[30-1];
        tau10=kD[31-1];
        tau11=kD[32-1];
        tau12=kD[33-1];
        tau13=kD[34-1];
        tau14=kD[35-1];
        tau15=kD[36-1];
        tau16=kD[37-1];
        tau17=kD[38-1];
        tau18=kD[39-1];
        tau19=kD[40-1];
        tau20=kD[41-1];



        kD[42-1]=kD[42-1];
        kD[43-1]=kD[43-1];
        kD[44-1]=kD[44-1];
        kD[45-1]=kD[45-1];
        fixdsb1 =kD[46-1];
        fixmsh =kD[47-1];
        fixmgmt =kD[48-1];
        basalp53act=kD[49-1];
        kDDbasal=kD[50-1];
        kDDE=kD[51-1];
        kDEtop=kD[52-1];
        Etop=kD[53-1];
        kDnSP=kD[54-1];
        kDkmSP=kD[55-1];
        kDnSS=kD[56-1];
        kDnDS=kD[57-1];
        kDkmSS=kD[58-1];
        kDkmDS=kD[59-1];




        # ### Cell Cycle Rate Constants
        aa=kC[1-1];
        ab=kC[2-1];
        ae=kC[3-1];
        cdk1tot=kC[4-1];
        cdk2tot=kC[5-1];
        cdk4tot=kC[6-1];
        Chk1tot=kC[7-1];
        eps=kC[8-1];
        ib=kC[9-1];
        ib1=kC[10-1];
        ib2=kC[11-1];
        ib3=kC[12-1];
        K1=kC[13-1];
        K1a=kC[14-1];
        K1b=kC[15-1];
        K1cdh1=kC[16-1];
        K1chk=kC[17-1];
        K1d=kC[18-1];
        K1e=kC[19-1];
        K1e2f=kC[20-1];
        K1p27=kC[21-1];
        K2=kC[22-1];
        K2a=kC[23-1];
        K2b=kC[24-1];
        K2cdh1=kC[25-1];
        K2chk=kC[26-1];
        K2d=kC[27-1];
        K2e=kC[28-1];
        K2e2f=kC[29-1];
        K2p27=kC[30-1];
        K3=kC[31-1];
        K3b=kC[32-1];
        K4=kC[33-1];
        K4b=kC[34-1];
        K5a=kC[35-1];
        K5b=kC[36-1];
        K5e=kC[37-1];
        K6a=kC[38-1];
        K6b=kC[39-1];
        K6e=kC[40-1];
        K7b=kC[41-1];
        K8b=kC[42-1];
        Kacdc20=kC[43-1];
        kc1=kC[44-1];
        kc10=kC[45-1];
        kc11=kC[46-1];
        kc12=kC[47-1];
        kc13=kC[48-1];
        kc14=kC[49-1];
        kc15=kC[50-1];



        kc16=kC[51-1];
        kc2=kC[52-1];
        kc3=kC[53-1];
        kc4=kC[54-1];
        kc5=kC[55-1];
        kc6=kC[56-1];
        kc7=kC[57-1];
        kc8=kC[58-1];
        kc9=kC[59-1];
        kca=kC[60-1];
        kcd2=kC[61-1];
        Kcdh1=kC[62-1];
        kce=kC[63-1];
        kcom1=kC[64-1];
        kcom2=kC[65-1];
        kcom3=kC[66-1];
        kcom4=kC[67-1];
        Kda=kC[68-1];
        Kdb=kC[69-1];
        Kdbcdc20=kC[70-1];
        Kdbcdh1=kC[71-1];
        kdcdc20a=kC[72-1];
        kdcdc20i=kC[73-1];
        kdcdh1a=kC[74-1];
        kdcdh1i=kC[75-1];
        Kdceskp2=kC[76-1];
        Kdd=kC[77-1];
        kdda=kC[78-1];
        kddb=kC[79-1];
        kddd=kC[80-1];
        kdde=kC[81-1];
        kddp21=kC[82-1];
        kddp27=kC[83-1];
        kddp27p=kC[84-1];
        kddskp2=kC[85-1];
        Kde=kC[86-1];
        kde2f=kC[87-1];
        kde2fp=kC[88-1];
        kdecom1=kC[89-1];
        kdecom2=kC[90-1];
        kdecom3=kC[91-1];
        kdecom4=kC[92-1];
        Kdp27p=kC[93-1];
        Kdp27skp2=kC[94-1];
        kdpa=kC[95-1];
        kdpai=kC[96-1];
        kdpb=kC[97-1];
        kdpbi=kC[98-1];
        kdpe=kC[99-1];
        kdpei=kC[100-1];
        kdprb=kC[101-1];
        kdprbp=kC[102-1];
        kdprbpp=kC[103-1];
        Kdskp2=kC[104-1];
        kdWee1=kC[105-1];
        kdWee1p=kC[106-1];
        Ki10=kC[107-1];
        Ki11=kC[108-1];
        Ki12=kC[109-1];
        Ki13=kC[110-1];
        Ki14=kC[111-1];
        Ki7=kC[112-1];
        Ki8=kC[113-1];
        Ki9=kC[114-1];
        kpc1=kC[115-1];
        kpc2=kC[116-1];
        kpc3=kC[117-1];
        kpc4=kC[118-1];
        V1=kC[119-1];
        V1cdh1=kC[120-1];
        V1chk=kC[121-1];
        V1e2f=kC[122-1];
        V1p27=kC[123-1];
        V2=kC[124-1];
        V2cdh1=kC[125-1];
        V2chk=kC[126-1];
        V2e2f=kC[127-1];
        V2p27=kC[128-1];
        V3=kC[129-1];
        V4=kC[130-1];
        V6a=kC[131-1];
        V6b=kC[132-1];
        V6e=kC[133-1];
        vcb=kC[134-1];
        Vda=kC[135-1];
        Vdb=kC[136-1];
        Vdd=kC[137-1];
        Vde=kC[138-1];
        Vdp27p=kC[139-1];
        Vdskp2=kC[140-1];
        Vm1a=kC[141-1];
        Vm1b=kC[142-1];
        Vm1d=kC[143-1];
        Vm1e=kC[144-1];
        Vm2a=kC[145-1];
        Vm2b=kC[146-1];





        Vm2d=kC[147-1];
        Vm2e=kC[148-1];
        Vm3b=kC[149-1];
        Vm4b=kC[150-1];
        Vm5a=kC[151-1];
        Vm5b=kC[152-1];
        Vm5e=kC[153-1];
        Vm7b=kC[154-1];
        Vm8b=kC[155-1];
        vs1p27=kC[156-1];
        vs2p27=kC[157-1];
        vscdc20i=kC[158-1];
        vscdh1a=kC[159-1];
        vse2f=kC[160-1];
        vspai=kC[161-1];
        vspbi=kC[162-1];
        vspei=kC[163-1];
        vsprb=kC[164-1];
        vsskp2=kC[165-1];
        vswee1=kC[166-1];
        xa1=kC[167-1];
        xa2=kC[168-1];
        xb1=kC[169-1];
        xb2=kC[170-1];
        xe1=kC[171-1];
        xe2=kC[172-1];
        kcd1=kC[173-1];




        # #### RATE LAWS

        # ## EIF4E sequestration by total mRNA in cell
        mT=xE[0];




        EIF4E_mT=xE[1];
        ksynth_mT=kE[0];
        kdeg_mT=kE[1];
        kdeg_EIF4E_mT=kE[2];




        vE = np.zeros(shape=(5))
        vE[0]=kT1*EIF4E*mT;
        vE[1]=kT2*EIF4E_mT;
        vE[2]=ksynth_mT;
        vE[3]=kdeg_mT*mT;
        vE[4]=kdeg_EIF4E_mT*EIF4E_mT;




        # ## vRIBOSOME **
        f1=((pS6K**nR)/(k50R**nR+pS6K**nR));
        vbR=kbR0+(kbRi*f1);
        vdR=kdR0*xRibosome;

        # ## vTL **
        rhs=(1/((EIF4Efree/(k50E+EIF4Efree))))*(Vn/Vc);


        # # # DNA Damage Mods
        kTL[0]=bp/mExp_nM[0]*rhs;
        kTL[1]=(bmi+bm*Mdm2pro)/mExp_nM[1]*rhs;
        kTL[2]=(bw*Wip1pro)/mExp_nM[2]*rhs;



        # # Cell Cycle Mods
        kTL[5]=vsprb/mExp_nM[5]*rhs*eps;
        kTL[6:9]=vse2f/sum(mExp_nM[6:9])*rhs*eps;
        kTL[9:12]=(kcd1+kcd2*E2F*(Ki7/(Ki7+pRB))*(Ki8/(Ki8+pRBp)))/sum(mExp_nM[9:12])*rhs*eps;
        kTL[12:14]=kce*E2F*(Ki9/(Ki9+pRB))*(Ki10/(Ki10+pRBp))/sum(mExp_nM[12:14])*rhs*eps;
        kTL[14]=vsskp2/mExp_nM[14]*rhs*eps;
        kTL[15]=vspei/mExp_nM[15]*rhs*eps;
        kTL[16]=vspai/mExp_nM[16]*rhs*eps;
        kTL[17]=vspbi/mExp_nM[17]*rhs*eps;
        kTL[18]=kca*E2F*(Ki11/(Ki11+pRB))*(Ki12/(Ki12+pRBp))/mExp_nM[18]*rhs*eps;
        kTL[19]=(vs1p27+(vs2p27*E2F*(Ki13/(Ki13+pRB))*(Ki14/(Ki14+pRBp))))/mExp_nM[19]*rhs*eps;
        kTL[20]=vscdh1a/mExp_nM[20]*rhs*eps;
        kTL[21]=vcb/mExp_nM[21]*rhs*eps;
        kTL[22]=vscdc20i/mExp_nM[22]*rhs*eps;
        kTL[23]=vswee1/mExp_nM[23]*rhs*eps;


        kTLcdk1tot=(cdk1tot/mExp_nM[26])*kTLd[26];
        cdk1tot=(kTLcdk1tot*mExp_nM[26])/kTLd[26];
        kTLcdk2tot=(cdk2tot/mExp_nM[27])*kTLd[27];
        cdk2tot=(kTLcdk2tot*mExp_nM[27])/kTLd[27];


        avgktl=np.mean(kTLd[28:30]);
        summExp=sum(mExp_nM[28:30]);
        kTLcdk4tot=(cdk4tot/summExp)*avgktl;
        cdk4tot=(kTLcdk4tot*summExp)/avgktl;



        kTLChk1tot=(kTLd[24]*Chk1tot)/mExp_nM[24];
        Chk1tot=(kTLChk1tot*mExp_nM[24])/kTLd[24];


        # syntax for flattening stuff
        mMod = np.squeeze(np.asarray(mMod))


        if flagE:
            vTL=np.multiply(kTL,mMod)*(EIF4E/(k50E+EIF4E));
        else:
            vTL=np.multiply(kTL,mMod)*(EIF4Efree/(k50E+EIF4Efree));



        # # Cell cycle proteins should not be affected by EIF4E, nor SGE.
        vTL[5:9]=np.multiply(kTL[5:9],mMod[5:9])*(EIF4Efree/(k50E+EIF4Efree));
        vTL[12:30]=np.multiply(kTL[12:30],mMod[12:30])*(EIF4Efree/(k50E+EIF4Efree));



        # ## vTLCd Protein Conglomerates Degradation Reactions
        vTLCd = np.zeros(shape=(102))
        vTLCd[1-1]=kTLCd[1-1]*p53inac;
        vTLCd[2-1]=kTLCd[2-1]*Mdm2 ;
        vTLCd[3-1]=kTLCd[3-1]*Wip1 ;
        vTLCd[4-1]=kTLCd[4-1]*BRCA2;
        vTLCd[5-1]=kTLCd[5-1]*MSH6;
        vTLCd[6-1]=kTLCd[6-1]*MGMT;
        vTLCd[7-1]=kTLCd[7-1]*ARF;
        vTLCd[8-1]=kTLCd[8-1]*MDM4;
        vTLCd[9-1]=kTLCd[9-1]*ATMinac;
        vTLCd[10-1]=kTLCd[10-1]*ATRinac;
        vTLCd[11-1]=0;#kTLCd[11-1]*pRB;
        vTLCd[12-1]=0;#kTLCd[12-1]*E2F;
        vTLCd[13-1]=0;#kTLCd[13-1]*Cd;
        vTLCd[14-1]=0;#kTLCd[14-1]*Ce;
        vTLCd[15-1]=0;#kTLCd[15-1]*Skp2;
        vTLCd[16-1]=0;#kTLCd[16-1]*Pai;
        vTLCd[17-1]=0;#kTLCd[17-1]*Pei;
        vTLCd[18-1]=0;#kTLCd[18-1]*Pbi;
        vTLCd[19-1]=0;#kTLCd[19-1]*Ca;
        vTLCd[20-1]=0;#kTLCd[20-1]*p27;
        vTLCd[21-1]=0;#kTLCd[21-1]*Cdh1a;
        vTLCd[22-1]=0;#kTLCd[22-1]*Cb;
        vTLCd[23-1]=0;#kTLCd[23-1]*Cdc20i;
        vTLCd[24-1]=0;#kTLCd[24-1]*Wee1;
        vTLCd[25-1]=0;#kTLCd[25-1]*Chk1;
        vTLCd[26-1]=0;#kTLCd[26-1]*p21;
        vTLCd[27-1]=kTLCd[27-1]*L ;
        vTLCd[28-1]=kTLCd[28-1]*R ;
        vTLCd[29-1]=kTLCd[29-1]*flip ;
        vTLCd[30-1]=kTLCd[30-1]*pC8 ;
        vTLCd[31-1]=kTLCd[31-1]*Bar ;
        vTLCd[32-1]=kTLCd[32-1]*pC3 ;
        vTLCd[33-1]=kTLCd[33-1]*pC6 ;
        vTLCd[34-1]=kTLCd[34-1]*XIAP ;
        vTLCd[35-1]=kTLCd[35-1]*PARP ;
        vTLCd[36-1]=kTLCd[36-1]*Bid ;
        vTLCd[37-1]=kTLCd[37-1]*Bcl2c ;
        vTLCd[38-1]=kTLCd[38-1]*Bax ;
        vTLCd[39-1]=kTLCd[39-1]*CytoCm ;
        vTLCd[40-1]=kTLCd[40-1]*Smacm ;
        vTLCd[41-1]=kTLCd[41-1]*Apaf ;
        vTLCd[42-1]=kTLCd[42-1]*pC9 ;
        vTLCd[43-1]=kTLCd[43-1]*BAD;
        vTLCd[44-1]=kTLCd[44-1]*PUMA;
        vTLCd[45-1]=kTLCd[45-1]*NOXA;
        vTLCd[46-1]=kTLCd[46-1]*BIM;
        vTLCd[47-1]=kTLCd[47-1]*E;
        vTLCd[48-1]=kTLCd[48-1]*H;
        vTLCd[49-1]=kTLCd[49-1]*HGF;
        vTLCd[50-1]=kTLCd[50-1]*P;
        vTLCd[51-1]=kTLCd[51-1]*F;
        vTLCd[52-1]=kTLCd[52-1]*I;
        vTLCd[53-1]=kTLCd[53-1]*IN;
        vTLCd[54-1]=kTLCd[54-1]*E1;
        vTLCd[55-1]=kTLCd[55-1]*E2;
        vTLCd[56-1]=kTLCd[56-1]*E3;
        vTLCd[57-1]=kTLCd[57-1]*E4;
        vTLCd[58-1]=kTLCd[58-1]*Ev3;
        vTLCd[59-1]=kTLCd[59-1]*Met;
        vTLCd[60-1]=kTLCd[60-1]*Pr;
        vTLCd[61-1]=kTLCd[61-1]*Fr;
        vTLCd[62-1]=kTLCd[62-1]*Ir;
        vTLCd[63-1]=kTLCd[63-1]*Isr;
        vTLCd[64-1]=kTLCd[64-1]*IRS;
        vTLCd[65-1]=kTLCd[65-1]*Sp;
        vTLCd[66-1]=kTLCd[66-1]*Cbl;
        vTLCd[67-1]=kTLCd[67-1]*G2;
        vTLCd[68-1]=kTLCd[68-1]*PLCg;
        vTLCd[69-1]=kTLCd[69-1]*PI3KC1;
        vTLCd[70-1]=kTLCd[70-1]*PI3KR1;
        vTLCd[71-1]=kTLCd[71-1]*PI3K2;
        vTLCd[72-1]=kTLCd[72-1]*GRP;
        vTLCd[73-1]=kTLCd[73-1]*RasD;
        vTLCd[74-1]=kTLCd[74-1]*NF1;
        vTLCd[75-1]=kTLCd[75-1]*CRaf;
        vTLCd[76-1]=kTLCd[76-1]*BRaf;
        vTLCd[77-1]=kTLCd[77-1]*MEK;
        vTLCd[78-1]=kTLCd[78-1]*MKP3;
        vTLCd[79-1]=kTLCd[79-1]*RSK;
        vTLCd[80-1]=kTLCd[80-1]*MKP1;
        vTLCd[81-1]=kTLCd[81-1]*cFos;
        vTLCd[82-1]=kTLCd[82-1]*cJun;
        vTLCd[83-1]=kTLCd[83-1]*cMyc;
        vTLCd[84-1]=kTLCd[84-1]*bCATENIN;
        vTLCd[85-1]=kTLCd[85-1]*PTEN;
        vTLCd[86-1]=kTLCd[86-1]*AKT;
        vTLCd[87-1]=kTLCd[87-1]*PDK1;
        vTLCd[88-1]=kTLCd[88-1]*Rictor;
        vTLCd[89-1]=kTLCd[89-1]*mTOR;
        vTLCd[90-1]=kTLCd[90-1]*GSK3b;
        vTLCd[91-1]=kTLCd[91-1]*TSC1;
        vTLCd[92-1]=kTLCd[92-1]*TSC2;
        vTLCd[93-1]=kTLCd[93-1]*PKC;
        vTLCd[94-1]=kTLCd[94-1]*RKIP;
        vTLCd[95-1]=kTLCd[95-1]*ERK;
        vTLCd[96-1]=kTLCd[96-1]*FOXO;
        vTLCd[97-1]=kTLCd[97-1]*RhebD;
        vTLCd[98-1]=kTLCd[98-1]*Raptor;
        vTLCd[99-1]=kTLCd[99-1]*S6K;
        vTLCd[100-1]=kTLCd[100-1]*EIF4EBP1;
        vTLCd[101-1]=kTLCd[101-1]*SOS;
        vTLCd[102-1]=kTLCd[102-1]*EIF4E;




        # ## vD **
        # some of these were commented out in the original matlab file, so i kept them commented out
        vD = np.zeros(shape=(66))
        #vD[1-1]= bp;
        vD[2-1]= ampi*Mdm2*p53inac;
        vD[3-1]= basalp53act + bsp*p53inac*(ATMP**ns/(ATMP**ns+Ts**ns)+ATRac**ns/(ATRac**ns+Ts**ns));
        vD[4-1]= awpa*Wip1*p53ac;
        vD[5-1]= api*p53inac;
        vD[6-1]= ampa*Mdm2*p53ac;
        #vD[7-1]= bm*Mdm2pro;
        #vD[8-1]= bmi;
        vD[9-1]= asm*Mdm2*ATMP;
        vD[10-1]= asm2*Mdm2*ATRac;
        vD[11-1]= am*Mdm2;
        #vD[12-1]= bw*Wip1pro;
        vD[13-1]= aw*Wip1;


        vD[14-1]= bs*((damageDSB**kDnDS)/((kDkmDS**kDnDS)+(damageDSB**kDnDS)));
        vD[15-1]= aws*ATMP*Wip1**nw/(Wip1**nw+Tw**nw);
        vD[16-1]= as_*ATMP;
        vD[17-1]= bs2*((damageSSB**kDnSS)/((kDkmSS**kDnSS)+(damageSSB**kDnSS)));
        vD[18-1]= as_*ATRac;
        vD[19-1]= Mdm2product1/tau1;
        vD[20-1]= p53ac/tau1;
        vD[21-1]= Mdm2product2/tau2;
        vD[22-1]= Mdm2product1/tau2;
        vD[23-1]= Mdm2product3/tau3;
        vD[24-1]= Mdm2product2/tau3;
        vD[25-1]= Mdm2product4/tau4;
        vD[26-1]= Mdm2product3/tau4;
        vD[27-1]= Mdm2product5/tau5;
        vD[28-1]= Mdm2product4/tau5;
        vD[29-1]= Mdm2product6/tau6;
        vD[30-1]= Mdm2product5/tau6;
        vD[31-1]= Mdm2product7/tau7;
        vD[32-1]= Mdm2product6/tau7;
        vD[33-1]= Mdm2product8/tau8;
        vD[34-1]= Mdm2product7/tau8;
        vD[35-1]= Mdm2product9/tau9;
        vD[36-1]= Mdm2product8/tau9;
        vD[37-1]= Mdm2pro/tau10;
        vD[38-1]= Mdm2product9/tau10;
        vD[39-1]= Wip1product1/tau11;
        vD[40-1]= p53ac/tau11;
        vD[41-1]= Wip1product2/tau12;
        vD[42-1]= Wip1product1/tau12;
        vD[43-1]= Wip1product3/tau13;
        vD[44-1]= Wip1product2/tau13;
        vD[45-1]= Wip1product4/tau14;
        vD[46-1]= Wip1product3/tau14;
        vD[47-1]= Wip1product5/tau15;
        vD[48-1]= Wip1product4/tau15;
        vD[49-1]= Wip1product6/tau16;
        vD[50-1]= Wip1product5/tau16;
        vD[51-1]= Wip1product7/tau17;
        vD[52-1]= Wip1product6/tau17;
        vD[53-1]= Wip1product8/tau18;
        vD[54-1]= Wip1product7/tau18;
        vD[55-1]= Wip1product9/tau19;
        vD[56-1]= Wip1product8/tau19;
        vD[57-1]= Wip1pro/tau20;
        vD[58-1]= Wip1product9/tau20;
        vD[59-1]=kD[42-1]*ARF*Mdm2;
        vD[60-1]=kD[43-1]*ARF*pMdm2;
        vD[61-1]=kD[44-1]*MDM4*p53ac;
        vD[62-1]=kD[45-1]*p53ac_MDM4;
        vD[63-1]=fixdsb1*BRCA2*damageDSB;
        vD[64-1]=fixmsh*MSH6*damageSSB;
        vD[65-1]=fixmgmt*MGMT*damageSSB;
        vD[66-1]=(kDDbasal+kDDE*(Etop/(Etop+kDEtop)))*(((Ma+Me)**kDnSP)/(((Ma+Me)**kDnSP)+(kDkmSP**kDnSP)));




        # ## vC **
        vC = np.zeros(shape=(104))
        #vC[1-1]=vsprb; #pRb(Rb) synthesis
        vC[2-1]=kpc1*pRB*E2F; #pRb binding to E2F
        vC[3-1]=kpc2*pRBc1; #dissociation of that pRbE2F complex
        vC[4-1]=V1*(pRB/(K1+pRB))*(Md+Mdp27); #pRb phosphorylation
        vC[5-1]=V2*(pRBp/(K2+pRBp)); #pRb dephosphorylation
        vC[6-1]=kdprb*pRB; #pRb degradation
        vC[7-1]=V3*(pRBp/(K3+pRBp))*Me; #pRbp phosphorylating to pRbpp
        vC[8-1]=V4*(pRBpp/(K4+pRBpp)); #pRbpp dephosphorylation to pRbp
        vC[9-1]=kpc3*pRBp*E2F; #pRbp binding to E2F
        vC[10-1]=kpc4*pRBc2; #pRbp dissociation from E2F
        vC[11-1]=kdprbp*pRBp; #pRbp degradation
        vC[12-1]=kdprbpp*pRBpp; #pRbpp degradation
        #vC[13-1]=vse2f; #E2F synthesis
        vC[14-1]=V1e2f*Ma*(E2F/(E2F+K1e2f)); #E2F phosphorylation by active CYCACDK2
        vC[15-1]=V2e2f*(E2Fp/(E2Fp+K2e2f)); #pE2F dephosphorylation to E2F
        vC[16-1]=kde2f*E2F; #E2F degradation
        vC[17-1]=kde2fp*E2Fp; #pE2F degradation
        #vC[18-1]=kcd1+kcd2*E2F*(Ki7/(Ki7+pRB))*(Ki8/(Ki8+pRBp)); #cycd synthesis due to E2f inhibited by pRb and pRbp
        vC[19-1]=kcom1*Cd*(cdk4tot-(Mdi+Md+Mdp27+Mdp21)); #cycd binding to cdk4/6
        vC[20-1]=kdecom1*Mdi; #dissociation of CYCD from CYCDCDK4/6(i) complex
        vC[21-1]=Vdd*(Cd/(Kdd+Cd)); #maximum cycd degradation
        vC[22-1]=kddd*Cd; #non specific cycd degradation
        vC[23-1]=Vm2d*(Md/(K2d+Md)); #inactivation of CYCDCK4/6(a) or Md
        vC[24-1]=Vm1d*(Mdi/(K1d+Mdi)); #activation of CYCDCDK4/6(i) or Mdi
        vC[25-1]=kc1*Md*p27; #CYCDCDK4/6(a) or Md binding to p27
        vC[26-1]=kc2*Mdp27; #dissociation of CYCDCDK4/6p27 coplex or Mdp27 to Md
        #vC[27-1]=kce*E2F*(Ki9/(Ki9+pRB))*(Ki10/(Ki10+pRBp)); #CYCE synthesis ##Keep like this for now.
        vC[28-1]=kcom2*Ce*(cdk2tot-(Mei+Me+Mep27+Mep21+Mai+Ma+Map27+Map21)); #CYCE going into complex with cdk2
        vC[29-1]=kdecom2*Mei; #dissociation of complex CYCECDK2(i)
        vC[30-1]=Vde*(Skp2/(Kdceskp2+Skp2))*(Ce/(Kde+Ce)); #CYCE degradation
        vC[31-1]=Vm2e*(Wee1+ib2)*(Me/(K2e+Me)); #inactivation of CYCECDK2
        vC[32-1]=Vm1e*Pe*(Mei/(K1e+Mei)); #activation of CYCECDK2
        vC[33-1]=kc3*Me*p27; #CYCECDK2 binding to p27
        vC[34-1]=kc4*Mep27; #dissociation of CYCECDK2p27
        #vC[35-1]=vsskp2; #synthesis of SKP2
        vC[36-1]=Vdskp2*(Skp2/(Kdskp2+Skp2))*(Cdh1a/(Kcdh1+Cdh1a)); #max SKP2 degradation
        vC[37-1]=kddskp2*Skp2; #non-specific SKP2 degradation
        #vC[38-1]=vspei; #synthesis of inactivated CDC25(i) or pei
        vC[39-1]=V6e*(xe1+xe2*Chk1)*(Pe/(K6e+Pe)); #Pei inactivation
        vC[40-1]=Vm5e*(Me+ae)*(Pei/(K5e+Pei)); #Pei activation
        vC[41-1]=kdpei*Pei; #Pei degradation
        vC[42-1]=kdpe*Pe; #Pe degradation
        #vC[43-1]=kca*E2F*(Ki11/(Ki11+pRB))*(Ki12/(Ki12+pRBp)); #CYCA synthesis induced by E2F inhibited by pRb and pRbp ##Keep like this for now.
        vC[44-1]=kcom3*Ca*(cdk2tot-(Mei+Me+Mep27+Mep21+Mai+Ma+Map27+Map21)); #CYCA binding to CDK2 making CYCACDK2(i) Mai
        vC[45-1]=kdecom3*Mai; #dissociation of Mai complex
        vC[46-1]=Vda*(Ca/(Kda+Ca))*(Cdc20a/(Kacdc20+Cdc20a)); #CYCA degradation induced by Cdc20(a)
        vC[47-1]=kdda*Ca; #non specific CYCA degradation
        vC[48-1]=Vm2a*(Wee1+ib3)*(Ma/(K2a+Ma)); #inactivation of CYCACDK2(a) or Ma complex
        vC[49-1]=Vm1a*Pa*(Mai/(K1a+Mai)); #activation of CYCACDK2(i) or Mai complex
        vC[50-1]=kc5*Ma*p27; #Ma binding to P27 making CYCACDK2p27
        vC[51-1]=kc6*Map27; #dissociation of Map27 to Map and p27
        vC[52-1]=V1p27*Me*(p27/(p27+K1p27)); #inactivation of p27 by CYCECDK2(a)
        vC[53-1]=V2p27*(p27p/(p27p+K2p27)); #activation of p27
        vC[54-1]=Vdp27p*(Skp2/(Skp2+Kdp27skp2))*(p27p/(p27p+Kdp27p)); #max p27p degradation
        vC[55-1]=kddp27p*p27p; #non specific p27p degradation
        vC[56-1]=V2cdh1*(Cdh1a/(K2cdh1+Cdh1a))*(Ma+Mb); #inactivation of Cdh1(a)
        vC[57-1]=V1cdh1*(Cdh1i/(K1cdh1+Cdh1i)); #activation of Cdh1(1)
        vC[58-1]=kdcdh1i*Cdh1i; #inactive Cdh1(i) degradation
        #vC[59-1]=vscdh1a; #synthesis of Cdh1(a)
        vC[60-1]=kdcdh1a*Cdh1a; #Cdh1(a) degradation
        #vC[61-1]=vspai; #CDC25(i) Pai synthesis
        vC[62-1]=V6a*(xa1+xa2*Chk1)*(Pa/(K6a+Pa)); #Pa Cdc25(a) inactivation to Pai
        vC[63-1]=Vm5a*(Ma+aa)*(Pai/(K5a+Pai)); #Pai activation to Pa
        vC[64-1]=kdpai*Pai; #Pai degradation
        vC[65-1]=kdpa*Pa; #Pa degradation
        #vC[66-1]=vcb; #CYCB synthesis
        vC[67-1]=kcom4*Cb*(cdk1tot-(Mbi+Mb+Mbp27+Mbp21)); #CYCB forming CYCBCDK1(i) complex
        vC[68-1]=kdecom4*Mbi; #dissociation of CYCBCDK1(i) complex
        vC[69-1]=Vdb*(Cb/(Kdb+Cb))*((Cdc20a/(Kdbcdc20+Cdc20a))+(Cdh1a/(Kdbcdh1+Cdh1a))); #max CYCB degradation induced by Cdc20(a)
        vC[70-1]=kddb*Cb; #non specific CYCB degradation
        vC[71-1]=Vm2b*(Wee1+ib1)*(Mb/(K2b+Mb)); #Mb inactivation to Mbi
        vC[72-1]=Vm1b*Pb*(Mbi/(K1b+Mbi)); #Mbi becoming active
        vC[73-1]=kc7*Mb*p27; #Mb (active CYCBCDK1) binding to p27
        vC[74-1]=kc8*Mbp27; #dissociation of Mb and p27
        #vC[75-1]=vscdc20i; #cdc20(i) synthesis
        vC[76-1]=Vm3b*Mb*(Cdc20i/(K3b+Cdc20i)); #activation of cdc20(i) through phosphorylation by CYCBCDK1
        vC[77-1]=Vm4b*(Cdc20a/(K4b+Cdc20a)); #cdc20(a) inactivation to cdc20(i)
        vC[78-1]=kdcdc20i*Cdc20i; #cdc20i degradation
        vC[79-1]=kdcdc20a*Cdc20a; #degradation of cdc20a
        #vC[80-1]=vspbi; #synthesis of inactive CDC25 Pbi
        vC[81-1]=V6b*(xb1+xb2*Chk1)*(Pb/(K6b+Pb)); #inactivation of CDC25 (Pb)
        vC[82-1]=Vm5b*(Mb+ab)*(Pbi/(K5b+Pbi)); #activation of CDC25(i) (Pbi)
        vC[83-1]=kdpbi*Pbi; #degradation of inactive CDC25 (Pbi)
        vC[84-1]=kdpb*Pb; #degradation of active CDC25 (Pb)
        #vC[85-1]=vswee1; #Wee1 synthesis
        vC[86-1]=Vm7b*(Mb+ib)*(Wee1/(K7b+Wee1)); #wee1 inactivation through phosphorylation due to CYCBCDK1
        vC[87-1]=Vm8b*(Wee1p/(K8b+Wee1p)); #wee1p(wee1(i)) activation through dephosphorylation
        vC[88-1]=kdWee1*Wee1; #wee1 degradation
        vC[89-1]=kdWee1p*Wee1p; #wee1p degradation
        vC[90-1]=V1chk*ATRac*((Chk1tot-Chk1)/(K1chk+(Chk1tot-Chk1))); #activation of Chk1 through phosphorylation by kinase ATR
        vC[91-1]=V2chk*(Chk1/(K2chk+Chk1)); #Chk1 inactivation through dephosphorylation
        vC[92-1]=kdde*Ce;#non-specific cycE degradation
        #vC[93-1]=vs1p27; #+ basal p27 synthesis
        #vC[94-1]=vs2p27*E2F*(Ki13/(Ki13+pRB))*(Ki14/(Ki14+pRBp)); #+ synthesis of p27 induced by E2F, inhibited by pRB and pRBp ##Keep like this for now.
        vC[95-1]=kddp27*p27; #- non-specific p27 degradation.
        vC[96-1]=kc9*Md*p21; #CYCDCDK4/6(a) or Md binding to p21
        vC[97-1]=kc10*Mdp21; #dissociation of CYCDCDK4/6p21 coplex or Mdp21 to Md
        vC[98-1]=kc11*Me*p21; #CYCECDK2 binding to p21
        vC[99-1]=kc12*Mep21; #dissociation of CYCECDK2p21
        vC[100-1]=kc13*Ma*p21; #Ma binding to P21 making CYCACDK2p21
        vC[101-1]=kc14*Map21; #dissociation of Map21 to Map and p21
        vC[102-1]=kc15*Mb*p21; #Mb (active CYCBCDK1) binding to p21
        vC[103-1]=kc16*Mbp21; #dissociation of Mb and p21


        vC[103]=kddp21*p21; #-non-specific p21 degradation
        vC[0:104]=vC[0:104]*eps;






        # ## vA **
        vA = np.zeros(shape=(87))
        vA[1-1]=kA[1-1]*L*R *Vc/Ve;
        vA[2-1]=kA[2-1]*L_R;
        vA[3-1]=kA[3-1]*L_R;
        vA[4-1]=kA[4-1]*Ractive*flip;
        vA[5-1]=kA[5-1]*Ractive_flip;
        vA[6-1]=kA[6-1]*Ractive*pC8;
        vA[7-1]=kA[7-1]*Ractive_pC8;
        vA[8-1]=kA[8-1]*Ractive_pC8;
        vA[9-1]=kA[9-1]*C8*Bar;
        vA[10-1]=kA[10-1]*C8_Bar;
        vA[11-1]=kA[11-1]*C8*pC3;
        vA[12-1]=kA[12-1]*C8_pC3;
        vA[13-1]=kA[13-1]*C8_pC3;
        vA[14-1]=kA[14-1]*C3*pC6;
        vA[15-1]=kA[15-1]*C3_pC6;
        vA[16-1]=kA[16-1]*C3_pC6;
        vA[17-1]=kA[17-1]*pC8*C6;
        vA[18-1]=kA[18-1]*C6_C8;
        vA[19-1]=kA[19-1]*C6_C8;
        vA[20-1]=kA[20-1]*C3*XIAP;
        vA[21-1]=kA[21-1]*C3_XIAP;
        vA[22-1]=kA[22-1]*C3_XIAP;
        vA[23-1]=kA[23-1]*C3*PARP;
        vA[24-1]=kA[24-1]*C3_PARP;
        vA[25-1]=kA[25-1]*C3_PARP;
        vA[26-1]=kA[26-1]*C8*Bid;
        vA[27-1]=kA[27-1]*C8_Bid;
        vA[28-1]=kA[28-1]*C8_Bid;
        vA[29-1]=kA[29-1]*tBid*Bcl2c;
        vA[30-1]=kA[30-1]*tBid_Bcl2c;
        vA[31-1]=kA[31-1]*tBid*Bax;
        vA[32-1]=kA[32-1]*tBid_Bax;
        vA[33-1]=kA[33-1]*tBid_Bax;
        vA[34-1]=kA[34-1]*Baxactive;
        vA[35-1]=kA[35-1]*Baxm;
        vA[36-1]=kA[36-1]*Baxm*Bcl2;
        vA[37-1]=kA[37-1]*Baxm_Bcl2;
        vA[38-1]=kA[38-1]*Baxm**2;
        vA[39-1]=kA[39-1]*Bax2;
        vA[40-1]=kA[40-1]*Bcl2*Bax2;
        vA[41-1]=kA[41-1]*Bax2_Bcl2;
        vA[42-1]=kA[42-1]*Bax2**2;
        vA[43-1]=kA[43-1]*Bax4;
        vA[44-1]=kA[44-1]*Bcl2*Bax4;
        vA[45-1]=kA[45-1]*Bax4_Bcl2;
        vA[46-1]=kA[46-1]*M*Bax4;
        vA[47-1]=kA[47-1]*Bax4_M;
        vA[48-1]=kA[48-1]*Bax4_M;
        vA[49-1]=kA[49-1]*Mactive*CytoCm;
        vA[50-1]=kA[50-1]*Mactive_CytoCm;
        vA[51-1]=kA[51-1]*Mactive_CytoCm;
        vA[52-1]=kA[52-1]*Mactive*Smacm;
        vA[53-1]=kA[53-1]*Mactive_Smacm;
        vA[54-1]=kA[54-1]*Mactive_Smacm;
        vA[55-1]=kA[55-1]*CytoCr;
        vA[56-1]=kA[56-1]*CytoC;
        vA[57-1]=kA[57-1]*CytoC*Apaf;
        vA[58-1]=kA[58-1]*CytoC_Apaf;
        vA[59-1]=kA[59-1]*CytoC_Apaf;
        vA[60-1]=kA[60-1]*Apafactive*pC9;
        vA[61-1]=kA[61-1]*Apop;
        vA[62-1]=kA[62-1]*pC3*Apop;
        vA[63-1]=kA[63-1]*Apop_C3;
        vA[64-1]=kA[64-1]*Apop_C3;
        vA[65-1]=kA[65-1]*Smacr;
        vA[66-1]=kA[66-1]*Smac;
        vA[67-1]=kA[67-1]*XIAP*Apop;
        vA[68-1]=kA[68-1]*Apop_XIAP;
        vA[69-1]=kA[69-1]*XIAP*Smac;
        vA[70-1]=kA[70-1]*Smac_XIAP;
        vA[71-1]=kA[71-1]*Bcl2c*BAD;
        vA[72-1]=kA[72-1]*Bcl2c_BAD;
        vA[73-1]=kA[73-1]*Bcl2c*PUMA;
        vA[74-1]=kA[74-1]*Bcl2c_PUMA;
        vA[75-1]=kA[75-1]*Bcl2c*NOXA;
        vA[76-1]=kA[76-1]*Bcl2c_NOXA;


        vA[77-1]=kA[77-1]*BIM*Bax;

        vA[78-1]=kA[78-1]*BIM_Bax;
        vA[79-1]=kA[79-1]*BIM_Bax;
        vA[80-1]=kA[80-1]*Bcl2c*BIM;
        vA[81-1]=kA[81-1]*Bcl2c_BIM;
        vA[82-1]=kA[82-1]*Mactive;
        vA[83-1]=kA[83-1]*Smacr;
        vA[84-1]=kA[84-1]*CytoCr;
        vA[85-1]=kA[85-1]*Bcl2c;
        vA[86-1]=kA[86-1]*Bcl2;
        vA[87-1]=kA[87-1]*pC8;



        # ## vR **
        vR = np.zeros(shape=(158))
        vR[1-1]=kR[1-1]*E1*E *Vc/Ve;
        vR[2-1]=kR[2-1]*EE1 ;
        vR[3-1]=kR[3-1]*EE1*E2 ;
        vR[4-1]=kR[4-1]*EE1E2 ;
        vR[5-1]=kR[5-1]*EE1*E1 ;
        vR[6-1]=kR[6-1]*EE1E1 ;
        vR[7-1]=kR[7-1]*EE1E1*E *Vc/Ve;
        vR[8-1]=2*kR[8-1]*EE1EE1 ;
        vR[9-1]=kR[9-1]*EE1EE1 ;
        vR[10-1]=kR[10-1]*EE1*EE1 ;
        vR[11-1]=kR[11-1]*EE1*E3 ;
        vR[12-1]=kR[12-1]*EE1E3 ;
        vR[13-1]=kR[13-1]*EE1E3*H *Vc/Ve;
        vR[14-1]=kR[14-1]*EE1HE3 ;
        vR[15-1]=kR[15-1]*EE1HE3 ;
        vR[16-1]=kR[16-1]*EE1*HE3 ;
        vR[17-1]=kR[17-1]*EE1*Ev3 ;
        vR[18-1]=kR[18-1]*EE1Ev3 ;
        vR[19-1]=kR[19-1]*EE1*E4 ;
        vR[20-1]=kR[20-1]*EE1E4 ;
        vR[21-1]=kR[21-1]*EE1E4*H *Vc/Ve;
        vR[22-1]=kR[22-1]*EE1HE4 ;
        vR[23-1]=kR[23-1]*EE1HE4 ;
        vR[24-1]=kR[24-1]*EE1*HE4 ;
        vR[25-1]=kR[25-1]*H*E3 *Vc/Ve;
        vR[26-1]=kR[26-1]*HE3 ;
        vR[27-1]=kR[27-1]*HE3*E2 ;
        vR[28-1]=kR[28-1]*E2HE3 ;
        vR[29-1]=kR[29-1]*HE3*E1 ;
        vR[30-1]=kR[30-1]*E1HE3 ;
        vR[31-1]=kR[31-1]*E1HE3*E *Vc/Ve;
        vR[32-1]=kR[32-1]*EE1HE3 ;
        vR[33-1]=kR[33-1]*HE3*E3 ;
        vR[34-1]=kR[34-1]*HE3E3 ;
        vR[35-1]=kR[35-1]*HE3E3*H *Vc/Ve;
        vR[36-1]=2*kR[36-1]*HE3HE3 ;
        vR[37-1]=kR[37-1]*HE3HE3 ;
        vR[38-1]=kR[38-1]*HE3*HE3 ;
        vR[39-1]=kR[39-1]*HE3*Ev3 ;
        vR[40-1]=kR[40-1]*HE3Ev3 ;
        vR[41-1]=kR[41-1]*HE3*E4 ;
        vR[42-1]=kR[42-1]*HE3E4 ;
        vR[43-1]=kR[43-1]*HE3E4*H *Vc/Ve;
        vR[44-1]=kR[44-1]*HE3HE4 ;
        vR[45-1]=kR[45-1]*HE3HE4 ;
        vR[46-1]=kR[46-1]*HE3*HE4 ;
        vR[47-1]=kR[47-1]*H*E4 *Vc/Ve;
        vR[48-1]=kR[48-1]*HE4 ;
        vR[49-1]=kR[49-1]*HE4*E2 ;
        vR[50-1]=kR[50-1]*E2HE4 ;
        vR[51-1]=kR[51-1]*HE4*E1 ;
        vR[52-1]=kR[52-1]*E1HE4 ;
        vR[53-1]=kR[53-1]*E1HE4*E *Vc/Ve;
        vR[54-1]=kR[54-1]*EE1HE4 ;
        vR[55-1]=kR[55-1]*HE4*E3 ;
        vR[56-1]=kR[56-1]*E3HE4 ;
        vR[57-1]=kR[57-1]*E3HE4*H *Vc/Ve;
        vR[58-1]=kR[58-1]*HE3HE4 ;
        vR[59-1]=kR[59-1]*HE4*Ev3 ;
        vR[60-1]=kR[60-1]*HE4Ev3 ;
        vR[61-1]=kR[61-1]*HE4*E4 ;
        vR[62-1]=kR[62-1]*HE4E4 ;
        vR[63-1]=kR[63-1]*HE4E4*H *Vc/Ve;
        vR[64-1]=2*kR[64-1]*HE4HE4 ;
        vR[65-1]=kR[65-1]*HE4HE4 ;
        vR[66-1]=kR[66-1]*HE4*HE4 ;
        vR[67-1]=kR[67-1]*E1*ppERK ;
        vR[68-1]=kR[68-1]*pE1 ;
        vR[69-1]=kR[69-1]*E2*ppERK ;
        vR[70-1]=kR[70-1]*pE2 ;
        vR[71-1]=kR[71-1]*E4*ppERK ;
        vR[72-1]=kR[72-1]*pE4 ;
        vR[73-1]=kR[73-1]*Met*HGF *Vc/Ve;
        vR[74-1]=kR[74-1]*HGF_Met ;
        vR[75-1]=kR[75-1]*HGF_Met*Met ;
        vR[76-1]=kR[76-1]*HGF_Met_Met ;
        vR[77-1]=kR[77-1]*HGF_Met_Met*HGF *Vc/Ve;
        vR[78-1]=2*kR[78-1]*HGF_Met_HGF_Met ;
        vR[79-1]=kR[79-1]*HGF_Met_HGF_Met ;
        vR[80-1]=kR[80-1]*HGF_Met*HGF_Met ;
        vR[81-1]=kR[81-1]*Pr*P *Vc/Ve;
        vR[82-1]=kR[82-1]*PPr ;
        vR[83-1]=kR[83-1]*PPr*PPr ;
        vR[84-1]=kR[84-1]*PPrPPr ;
        vR[85-1]=2*kR[85-1]*PPrPPr ;
        vR[86-1]=kR[86-1]*PPrPr ;
        vR[87-1]=kR[87-1]*Fr*F *Vc/Ve;
        vR[88-1]=kR[88-1]*FFr;
        vR[89-1]=kR[89-1]*FFr*FFr;
        vR[90-1]=kR[90-1]*FFrFFr;
        vR[91-1]=2*kR[91-1]*FFrFFr;
        vR[92-1]=kR[92-1]*F*FFrFr *Vc/Ve;
        vR[93-1]=kR[93-1]*FFrFr;
        vR[94-1]=kR[94-1]*Fr*FFr;
        vR[95-1]=kR[95-1]*Ir*Ir;
        vR[96-1]=kR[96-1]*IrIr;
        vR[97-1]=kR[97-1]*Isr*Isr;
        vR[98-1]=kR[98-1]*Isr_Isr;
        vR[99-1]=kR[99-1]*E1_ppERK;
        vR[100-1]=kR[100-1]*E1_ppERK;
        vR[101-1]=kR[101-1]*E2_ppERK;
        vR[102-1]=kR[102-1]*E2_ppERK;
        vR[103-1]=kR[103-1]*E4_ppERK;
        vR[104-1]=kR[104-1]*E4_ppERK;
        vR[105-1]=kR[105-1]*E1*E1;
        vR[106-1]=kR[106-1]*E1E1;
        vR[107-1]=kR[107-1]*E1*E2;
        vR[108-1]=kR[108-1]*E1E2;
        vR[109-1]=kR[109-1]*E1*E3;
        vR[110-1]=kR[110-1]*E1E3;
        vR[111-1]=kR[111-1]*E1*E4;
        vR[112-1]=kR[112-1]*E1E4;
        vR[113-1]=kR[113-1]*E2*E2;
        vR[114-1]=kR[114-1]*E2E2;
        vR[115-1]=kR[115-1]*E2*E3;
        vR[116-1]=kR[116-1]*E2E3;
        vR[117-1]=kR[117-1]*E2*E4;
        vR[118-1]=kR[118-1]*E2E4;
        vR[119-1]=kR[119-1]*E3*E4;
        vR[120-1]=kR[120-1]*E3E4;
        vR[121-1]=kR[121-1]*E4*E4;
        vR[122-1]=kR[122-1]*E4E4;
        vR[123-1]=2*kR[123-1]*E*E1E1 *Vc/Ve;
        vR[124-1]=kR[124-1]*EE1E1;
        vR[125-1]=kR[125-1]*E*E1E2 *Vc/Ve;
        vR[126-1]=kR[126-1]*EE1E2;
        vR[127-1]=kR[127-1]*E*E1E3 *Vc/Ve;
        vR[128-1]=kR[128-1]*EE1E3;
        vR[129-1]=kR[129-1]*H*E1E3 *Vc/Ve;
        vR[130-1]=kR[130-1]*E1HE3;
        vR[131-1]=kR[131-1]*E*E1E4 *Vc/Ve;
        vR[132-1]=kR[132-1]*EE1E4;
        vR[133-1]=kR[133-1]*H*E1E4 *Vc/Ve;
        vR[134-1]=kR[134-1]*E1HE4;
        vR[135-1]=kR[135-1]*H*E2E3 *Vc/Ve;
        vR[136-1]=kR[136-1]*E2HE3;
        vR[137-1]=kR[137-1]*H*E2E4 *Vc/Ve;
        vR[138-1]=kR[138-1]*E2HE4;
        vR[139-1]=2*kR[139-1]*H*E3E4 *Vc/Ve;
        vR[140-1]=kR[140-1]*E3HE4;
        vR[141-1]=2*kR[141-1]*H*E4E4 *Vc/Ve;
        vR[142-1]=kR[142-1]*HE4E4;
        vR[143-1]=kR[143-1]*Met*Met;
        vR[144-1]=kR[144-1]*Met_Met;
        vR[145-1]=2*kR[145-1]*HGF*Met_Met;
        vR[146-1]=kR[146-1]*HGF_Met_Met;
        vR[147-1]=kR[147-1]*Fr*Fr;
        vR[148-1]=kR[148-1]*FrFr;
        vR[149-1]=2*kR[149-1]*F*FrFr;
        vR[150-1]=kR[150-1]*FFrFr;
        vR[151-1]=kR[151-1]*IrIr*I *Vc/Ve;
        vR[152-1]=kR[152-1]*IIrIr;
        vR[153-1]=kR[153-1]*IIrIr*I *Vc/Ve;
        vR[154-1]=kR[154-1]*IIrIrI;
        vR[155-1]=kR[155-1]*Isr_Isr*IN *Vc/Ve;
        vR[156-1]=kR[156-1]*IN_Isr_Isr;
        vR[157-1]=kR[157-1]*IN_Isr_Isr*IN *Vc/Ve;
        vR[158-1]=kR[158-1]*IN_Isr_Isr_IN;


        # ## vRP **
        fac=1;

        ps_G2_SOS= np.array([9,10,10,10,8,8,11,11,7,8,8,9,9,10,11,11,9,12,12,2,2,1,1,8,8,5,7,5,7])*fac;
        ps_PI3K1= np.array([4,2,2,2,10,10,4,4,12,10,10,12,12,6,4,4,12,6,6,6,6,6,6,14,16,10.5,14.5,10.5,14.5])*fac;
        ps_PI3K2=ps_PI3K1;
        ps_PLCg= np.array([4,4,4,4,3,3,3,3,3,3,3,2,2,3,3,3,2,2,2,4,4,5,5,2,6,1.5,3.5,1.5,3.5])*fac;



        # # Equations
        vRP1 = np.multiply(kRP1,SCD); # Phosphorylation
        vRP2 = np.multiply(kRP2,pSCD); # Dephosphorylation


        vRP3 = np.multiply(kRP3,SCD)*Sp; # Binding Spouty

        vRP4 = np.multiply(kRP4,Sp_SCD); # Dissociation Sprouty
        kmCblint=2;
        vRP5 = np.multiply(kRP5,(pSCD/(kmCblint+pSCD)))*Cbl + np.multiply(kRP5[8],pSCD); # Internalization
        vRP6 = np.multiply(kRP6,pSCDint); # Dephosphorylation
        vRP7 = np.multiply(kRP7,SCDint); # Phosphorylation
        vRP8 = np.multiply(kRP8,SCDint); # Recycling
        vRP9 = np.multiply(np.multiply(ps_G2_SOS,kRP9),pSCDint_bind)*G2_SOS; # Int binding G2-SOS
        vRP10 = np.multiply(kRP10,pSCDint_G2_SOS); # Int dissociating from G2-SOS
        vRP11 = np.multiply(np.multiply(np.multiply(ps_G2_SOS,kRP11),pSCD_bind),G2_SOS); #pSCD binding G2-SOS
        vRP12 = np.multiply(kRP12,pSCD_G2_SOS); #pSCD dissociating G2-SOS
        vRP13 = np.multiply(np.multiply(np.multiply(ps_PLCg,kRP13),pSCD_bind),PLCg);
        vRP14 = np.multiply(kRP14,pSCD_PLCg);
        vRP15 = np.multiply(np.multiply(np.multiply(ps_PI3K1,kRP15),pSCD_bind),PI3K1);
        vRP16 = np.multiply(kRP16,pSCD_PI3K1);
        vRP17 = np.multiply(np.multiply(np.multiply(ps_PI3K2,kRP17),pSCD_bind),PI3K2);
        vRP18 = np.multiply(kRP18,pSCD_PI3K2);
        vRP19 = np.multiply(np.multiply(kRP19,pSCDint_G2_SOS),RasD); #Binding to RasDint
        vRP20 = np.multiply(kRP20,pSCDint_G2_SOS_RasD); #Dissociation
        vRP21 = np.multiply(kRP21,pSCDint_G2_SOS_RasD); #Making product
        vRP22 = np.multiply(np.multiply(kRP22,pSCD_G2_SOS),RasD); #Binding to RasD
        vRP23 = np.multiply(kRP23,pSCD_G2_SOS_RasD); #Dissociation
        vRP24 = np.multiply(kRP24,pSCD_G2_SOS_RasD); #Making product
        vRP25 = np.multiply(np.multiply(kRP25,pSCD_PLCg),PIP2); #Binding to PIP2
        vRP26 = np.multiply(kRP26,pSCD_PLCg_PIP2); #Dissociation
        vRP27 = np.multiply(kRP27,pSCD_PLCg_PIP2); #Making product
        vRP28 = np.multiply(np.multiply(kRP28,pSCD_PI3K1),PIP2); #Binding to PIP2
        vRP29 = np.multiply(kRP29,pSCD_PI3K1_PIP2); #Dissociation
        vRP30 = np.multiply(kRP30,pSCD_PI3K1_PIP2); #Making product
        vRP31 = np.multiply(np.multiply(kRP31,pSCD_PI3K2),PIP); #Binding to PIP2
        vRP32 = np.multiply(kRP32,pSCD_PI3K2_PIP); #Dissociation
        vRP33 = np.multiply(kRP33,pSCD_PI3K2_PIP); #Making product



        # # IGFR and INSR binding IRS
        ps_IRS=2*4;
        vRP34 = np.zeros(shape=(16))
        vRP34[0]=ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[0]),pIIrIr),IRS);
        vRP34[1]=np.multiply(kRP34[1],pIIrIr_IRS);
        vRP34[2]=ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[2]),pIN_Isr_Isr),IRS);
        vRP34[3]=np.multiply(kRP34[3],pIN_Isr_Isr_IRS);


        vRP34[4]=ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[4]),pIIrIrI),IRS);
        vRP34[5]=np.multiply(kRP34[5],pIIrIrI_IRS);
        vRP34[6]= ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[6]),pIN_Isr_Isr_IN),IRS);
        vRP34[7]=np.multiply(kRP34[7],pIN_Isr_Isr_IN_IRS);

        vRP34[8]= ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[8]),pIIrIr_int),IRS);
        vRP34[9]=np.multiply(kRP34[9],pIIrIr_int_IRS);
        vRP34[10]=ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[10]),pIN_Isr_Isr_int),IRS);
        vRP34[11]= np.multiply(kRP34[11],pIN_Isr_Isr_int_IRS);
        vRP34[12]=ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[12]),pIIrIrI_int),IRS);
        vRP34[13]=np.multiply(kRP34[13],pIIrIrI_int_IRS);
        vRP34[14]=ps_IRS * np.multiply(np.multiply(np.multiply(fac,kRP34[14]),pIN_Isr_Isr_IN_int),IRS);
        vRP34[15]=np.multiply(kRP34[15],pIN_Isr_Isr_IN_int_IRS);
        vRP34= np.matrix.transpose(vRP34)



        # ## vP **
        vP = np.zeros(shape=(190))
        vP[1-1]=kP[1-1]*RasT*CRaf;
        vP[2-1]=kP[2-1]*RasT_CRaf;
        vP[3-1]=kP[3-1]*RasT*BRaf;
        vP[4-1]=kP[4-1]*RasT_BRaf;
        vP[5-1]=kP[5-1]*RasT_CRaf*RasT_CRaf;
        vP[6-1]=kP[6-1]*RasT_CRaf_CRaf;
        vP[7-1]=kP[7-1]*RasT_BRaf*RasT_BRaf;
        vP[8-1]=kP[8-1]*RasT_BRaf_BRaf;
        vP[9-1]=kP[9-1]*RasT_CRaf*RasT_BRaf;
        vP[10-1]=kP[10-1]*RasT_CRaf_BRaf;
        vP[11-1]=0;#kP[11-1]*RasT_BRaf*CRaf;
        vP[12-1]=0;#kP[12-1]*RasT_CRaf_BRaf;
        vP[13-1]=kP[13-1]*MEK*RasT_CRaf_CRaf;
        vP[14-1]=kP[14-1]*MEK_RasT_CRaf_CRaf;
        vP[15-1]=kP[15-1]*MEK_RasT_CRaf_CRaf;
        vP[16-1]=kP[16-1]*pMEK*RasT_CRaf_CRaf;
        vP[17-1]=kP[17-1]*pMEK_RasT_CRaf_CRaf;
        vP[18-1]=kP[18-1]*pMEK_RasT_CRaf_CRaf;
        vP[19-1]=kP[19-1]*MEK*RasT_BRaf_BRaf;
        vP[20-1]=kP[20-1]*MEK_RasT_BRaf_BRaf;
        vP[21-1]=kP[21-1]*MEK_RasT_BRaf_BRaf;
        vP[22-1]=kP[22-1]*pMEK*RasT_BRaf_BRaf;
        vP[23-1]=kP[23-1]*pMEK_RasT_BRaf_BRaf;
        vP[24-1]=kP[24-1]*pMEK_RasT_BRaf_BRaf;
        vP[25-1]=kP[25-1]*MEK*RasT_CRaf_BRaf;
        vP[26-1]=kP[26-1]*MEK_RasT_CRaf_BRaf;
        vP[27-1]=kP[27-1]*MEK_RasT_CRaf_BRaf;
        vP[28-1]=kP[28-1]*pMEK*RasT_CRaf_BRaf;
        vP[29-1]=kP[29-1]*pMEK_RasT_CRaf_BRaf;
        vP[30-1]=kP[30-1]*pMEK_RasT_CRaf_BRaf;
        vP[31-1]=kP[31-1]*pMEK;
        vP[32-1]=kP[32-1]*ppMEK;
        vP[33-1]=kP[33-1]*ERK*ppMEK;
        vP[34-1]=kP[34-1]*ERK_ppMEK;
        vP[35-1]=kP[35-1]*ERK_ppMEK;
        vP[36-1]=kP[36-1]*pERK*ppMEK;
        vP[37-1]=kP[37-1]*pERK_ppMEK;
        vP[38-1]=kP[38-1]*pERK_ppMEK;
        vP[39-1]=kP[39-1]*ppERKnuc*MKP1;
        vP[40-1]=kP[40-1]*ppERKnuc_MKP1;
        vP[41-1]=kP[41-1]*ppERKnuc_MKP1;
        vP[42-1]=kP[42-1]*pMKP1;
        vP[43-1]=kP[43-1]*pcFos;
        vP[44-1]=kP[44-1]*pTSC2;
        vP[45-1]=kP[45-1]*pRSKnuc;
        vP[46-1]=kP[46-1]*G2_SOS*ppERK;
        vP[47-1]=kP[47-1]*G2_SOS_ppERK;
        vP[48-1]=kP[48-1]*G2_SOS_ppERK;
        vP[49-1]=kP[49-1]*G2_pSOS;
        vP[50-1]=kP[50-1]*CRaf*ppERK;
        vP[51-1]=kP[51-1]*CRaf_ppERK;
        vP[52-1]=kP[52-1]*CRaf_ppERK;
        vP[53-1]=kP[53-1]*pCRaf;
        vP[54-1]=kP[54-1]*RasD*DAG_GRP;
        vP[55-1]=kP[55-1]*RasD_DAG_GRP;
        vP[56-1]=kP[56-1]*RasD_DAG_GRP;
        vP[57-1]=kP[57-1]*RasT*NF1;
        vP[58-1]=kP[58-1]*RasT_NF1;
        vP[59-1]=kP[59-1]*RasT_NF1;
        vP[60-1]=kP[60-1]*NF1*ppERK;
        vP[61-1]=kP[61-1]*NF1_ppERK;
        vP[62-1]=kP[62-1]*NF1_ppERK;
        vP[63-1]=kP[63-1]*pNF1;
        vP[64-1]=kP[64-1]*pERK*MKP3;
        vP[65-1]=kP[65-1]*pERK_MKP3;
        vP[66-1]=kP[66-1]*pERK_MKP3;
        vP[67-1]=kP[67-1]*ppERK*MKP3;
        vP[68-1]=kP[68-1]*ppERK_MKP3;
        vP[69-1]=kP[69-1]*ppERK_MKP3;
        vP[70-1]=kP[70-1]*RSK*ppERK;
        vP[71-1]=kP[71-1]*RSK_ppERK;
        vP[72-1]=kP[72-1]*RSK_ppERK;
        vP[73-1]=kP[73-1]*pRSK;
        vP[74-1]=kP[74-1]*ppERK;
        vP[75-1]=kP[75-1]*ERKnuc;
        vP[76-1]=kP[76-1]*ppERKnuc*pMKP1;
        vP[77-1]=kP[77-1]*ppERKnuc_pMKP1 ;
        vP[78-1]=kP[78-1]*ppERKnuc_pMKP1 ;
        vP[79-1]=kP[79-1]*ERKnuc;
        vP[80-1]=kP[80-1]*pRSK;
        vP[81-1]=kP[81-1]*MKP1*pRSKnuc;
        vP[82-1]=kP[82-1]*pRSKnuc_MKP1;
        vP[83-1]=kP[83-1]*pRSKnuc_MKP1;
        vP[84-1]=kP[84-1]*MKP1*ppERKnuc;
        vP[85-1]=kP[85-1]*ppERKnuc_MKP1;
        vP[86-1]=kP[86-1]*ppERKnuc_MKP1;
        vP[87-1]=kP[87-1]*cFos*pRSKnuc;
        vP[88-1]=kP[88-1]*cFos_pRSKnuc;
        vP[89-1]=kP[89-1]*cFos_pRSKnuc;
        vP[90-1]=kP[90-1]*cFos*ppERKnuc;
        vP[91-1]=kP[91-1]*cFos_ppERKnuc;
        vP[92-1]=kP[92-1]*cFos_ppERKnuc;
        vP[93-1]=kP[93-1]*pcFos*cJun;
        vP[94-1]=kP[94-1]*pcFos_cJun;
        vP[95-1]=kP[95-1]*GRP*DAG;
        vP[96-1]=kP[96-1]*DAG_GRP;
        vP[97-1]=kP[97-1]*DAG*PKC;
        vP[98-1]=kP[98-1]*DAG_PKC;
        vP[99-1]=kP[99-1]*RKIP*DAG_PKC;
        vP[100-1]=kP[100-1]*RKIP_DAG_PKC;
        vP[101-1]=kP[101-1]*RKIP_DAG_PKC;
        vP[102-1]=kP[102-1]*pRKIP;
        vP[103-1]=kP[103-1]*RKIP*CRaf;
        vP[104-1]=kP[104-1]*RKIP_CRaf;
        vP[105-1]=kP[105-1]*PIP3*PTEN;
        vP[106-1]=kP[106-1]*PIP3_PTEN;
        vP[107-1]=kP[107-1]*PIP3_PTEN;
        vP[108-1]=kP[108-1]*PIP3*AKT;
        vP[109-1]=kP[109-1]*PIP3_AKT;
        vP[110-1]=kP[110-1]*PIP3*PDK1;
        vP[111-1]=kP[111-1]*PIP3_PDK1;
        vP[112-1]=kP[112-1]*Rictor*mTOR;
        vP[113-1]=kP[113-1]*mTORC2;
        vP[114-1]=kP[114-1]*PIP3_AKT*PIP3_PDK1;
        vP[115-1]=kP[115-1]*PIP3_AKT_PIP3_PDK1;
        vP[116-1]=kP[116-1]*PIP3_AKT_PIP3_PDK1;
        vP[117-1]=kP[117-1]*PIP3_pAKT;
        vP[118-1]=kP[118-1]*PIP3_pAKT*mTORC2;
        vP[119-1]=kP[119-1]*PIP3_pAKT_mTORC2;
        vP[120-1]=kP[120-1]*PIP3_pAKT_mTORC2;
        vP[121-1]=kP[121-1]*PIP3_ppAKT;
        vP[122-1]=kP[122-1]*PIP3_ppAKT;
        vP[123-1]=kP[123-1]*PIP3*ppAKT;
        vP[124-1]=kP[124-1]*GSK3b*ppAKT;
        vP[125-1]=kP[125-1]*GSK3b_ppAKT;
        vP[126-1]=kP[126-1]*GSK3b_ppAKT;
        vP[127-1]=kP[127-1]*pGSK3b;


        vP[127]=(kP[127]*bCATENIN*GSK3b**4)/(200**4+GSK3b**4);

        vP[131-1]=kP[131-1]*pbCATENIN;
        vP[132-1]=kP[132-1]*bCATENIN;
        vP[133-1]=kP[133-1]*bCATENINnuc;
        vP[134-1]=kP[134-1]*TSC2*ppAKT;
        vP[135-1]=kP[135-1]*TSC2_ppAKT;
        vP[136-1]=kP[136-1]*TSC2_ppAKT;
        vP[137-1]=kP[137-1]*TSC2*ppERK;
        vP[138-1]=kP[138-1]*TSC2_ppERK;
        vP[139-1]=kP[139-1]*TSC2_ppERK;
        vP[140-1]=kP[140-1]*TSC1*TSC2;
        vP[141-1]=kP[141-1]*TSC;
        vP[142-1]=0;
        vP[143-1]=0;
        vP[144-1]=0;
        vP[145-1]=0;
        vP[146-1]=kP[146-1]*mTORC1;

        vP[146]=(kP[146]*mTORC1active*TSC**4)/(.1+TSC**4);

        vP[148-1]=kP[148-1]*Raptor*mTOR;
        vP[149-1]=kP[149-1]*mTORC1;
        vP[150-1]=kP[150-1]*EIF4EBP1*mTORC1active;
        vP[151-1]=kP[151-1]*EIF4EBP1_mTORC1active;
        vP[152-1]=kP[152-1]*EIF4EBP1_mTORC1active;
        vP[153-1]=kP[153-1]*pEIF4EBP1;
        vP[154-1]=kP[154-1]*S6K*mTORC1active;
        vP[155-1]=kP[155-1]*S6K_mTORC1active;
        vP[156-1]=kP[156-1]*S6K_mTORC1active;
        vP[157-1]=kP[157-1]*pS6K;
        vP[158-1]=kP[158-1]*FOXO*ppAKT;
        vP[159-1]=kP[159-1]*FOXO_ppAKT;
        vP[160-1]=kP[160-1]*FOXO_ppAKT;
        vP[161-1]=kP[161-1]*pFOXO;
        vP[162-1]=kP[162-1]*PI3K1*mTORC1active;
        vP[163-1]=kP[163-1]*PI3K1_mTORC1active;
        vP[164-1]=kP[164-1]*PI3K1_mTORC1active;
        vP[165-1]=kP[165-1]*pPI3K1;
        vP[166-1]=kP[166-1]*PI3KC1*PI3KR1;
        vP[167-1]=kP[167-1]*PI3K1;
        vP[168-1]=kP[168-1]*PI3P;
        vP[169-1]=kP[169-1]*SOS*G2;
        vP[170-1]=kP[170-1]*G2_SOS;
        vP[171-1]=kP[171-1]*EIF4E*EIF4EBP1;
        vP[172-1]=kP[172-1]*EIF4EBP1_EIF4E;
        vP[173-1]=kP[173-1];
        vP[174-1]=kP[174-1]*pbCATENIN*TSC;
        vP[175-1]=kP[175-1]*pERK;
        vP[176-1]=kP[176-1]*ppERK;
        vP[177-1]=kP[177-1]*ppERKnuc;
        vP[178-1]=kP[178-1]*ppAKT;
        vP[179-1]=kP[179-1]*pAKT;
        vP[180-1]=kP[180-1]*RhebT;
        vP[181-1]=kP[181-1]*FOXO;
        vP[182-1]=kP[182-1]*FOXOnuc;
        vP[183-1]=kP[183-1]*PIP2;
        vP[184-1]=kP[184-1]*PIP3;
        vP[185-1]=kP[185-1]*RasD;
        vP[186-1]=kP[186-1]*RasT;
        vP[187-1]=kP[187-1]*MEKi*ppMEK;
        vP[188-1]=kP[188-1]*MEKi_ppMEK;
        vP[189-1]=kP[189-1]*AKTi*AKT;
        vP[190-1]=kP[190-1]*AKTi_AKT;


        # ## vDA **
        # # NONE as these are all transcriptional control mechanisms.


        # ## vDP **
        vDP = np.zeros(shape=(4))
        vDP[0]=kDP[0]*ppAKT*Mdm2;
        vDP[1]=kDP[1]*ppAKT_Mdm2;
        vDP[2]=kDP[2]*ppAKT_Mdm2;
        vDP[3]=kDP[3]*pMdm2;


        # ## vPA **
        vPA = np.zeros(shape=(11))
        vPA[1-1]=kPA[1-1]*ppERK*BIM;
        vPA[2-1]=kPA[2-1]*ppERK_BIM;
        vPA[3-1]=kPA[3-1]*ppERK_BIM;
        vPA[4-1]=kPA[4-1]*pBIM;
        vPA[5-1]=kPA[5-1]*ppAKT*BAD;
        vPA[6-1]=kPA[6-1]*ppAKT_BAD;
        vPA[7-1]=kPA[7-1]*ppAKT_BAD;
        vPA[8-1]=kPA[8-1]*ppERK*BAD;
        vPA[9-1]=kPA[9-1]*ppERK_BAD;
        vPA[10-1]=kPA[10-1]*ppERK_BAD;
        vPA[11-1]=kPA[11-1]*pBAD;



        # ## vPC **
        # # NONE as these are all transcriptional control mechanisms.
        #
        # ## vDC **
        # # NONE as these are all transcriptional control mechanisms.
        #
        #
        # ## vDd (none)
        # # Removed all Dd and Cd degradation reactions. These are controlled from
        # # within these submodels, respectively.
        #
        # ## vCd (none)
        # # # removed all degradation reactions because cell cycle model handles that
        # # # internally.
        #


        # ## vAd
        Ads= np.matrix([L_R,
        Ractive,
        Ractive_flip,
        Ractive_pC8,
        C8,
        C8_Bar,
        C8_pC3,
        C3,
        C3_pC6,
        C6,
        C6_C8,
        C3_XIAP,
        C3_PARP,
        cPARP,
        C8_Bid,
        tBid,
        tBid_Bcl2c,
        tBid_Bax,
        Baxactive,
        Baxm,
        Bcl2,
        Baxm_Bcl2,
        Bax2,
        Bax2_Bcl2,
        Bax4,
        Bax4_Bcl2,
        CytoCr,
        Smacr,
        CytoC,
        CytoC_Apaf,
        Apafactive,
        Apop,
        Apop_C3,
        Smac,
        Apop_XIAP,
        Smac_XIAP,
        C3_Ub,
        Bcl2c_BAD,
        Bcl2c_PUMA,
        Bcl2c_NOXA,
        BIM_Bax,
        Bcl2c_BIM,
        ppERK_BIM,
        pBIM,
        ppAKT_BAD,
        pBAD,
        ppERK_BAD]);

        Ads = np.matrix.transpose(Ads)


        Rds= np.matrix([pE1,
        pE2,
        pE4,
        E1E1,
        E1E2,
        E1E3,
        E1E4,
        E2E2,
        E2E3,
        E2E4,
        E3E4,
        E4E4,
        Met_Met,
        FrFr,
        IrIr,
        Isr_Isr,
        EE1,
        HE3,
        HE4,
        HGF_Met,
        PPr,
        FFr,
        EE1E2,
        EE1Ev3,
        EE1E1,
        EE1E3,
        EE1E4,
        E2HE3,
        E1HE3,
        HE3E3,
        HE3Ev3,
        HE3E4,
        E2HE4,
        HE4Ev3,
        E1HE4,
        E3HE4,
        HE4E4,
        HGF_Met_Met,
        PPrPr,
        FFrFr,
        IIrIr,
        IN_Isr_Isr,
        EE1EE1,
        EE1HE3,
        EE1HE4,
        HE3HE3,
        HE3HE4,
        HE4HE4,
        HGF_Met_HGF_Met,
        PPrPPr,
        FFrFFr,
        IIrIrI,
        IN_Isr_Isr_IN,
        E1_ppERK,
        E2_ppERK,
        E4_ppERK]);

        Rds = np.matrix.transpose(Rds)




        RPds=xRP;

        Pds= np.matrix([G2_SOS,
        G2_pSOS,
        PI3K1,
        pPI3K1,
        mTORC1,
        mTORC1active,
        PIP,
        PI3P,
        DAG,
        DAG_GRP,
        RasT,
        pNF1,
        pCRaf,
        RasT_CRaf,
        RasT_CRaf_BRaf,
        pMEK,
        ppMEK,
        ERKnuc,
        ppERKnuc,
        pRSK,
        pRSKnuc,
        pMKP1,
        pcFos,
        pcFos_cJun,
        bCATENINnuc,
        pbCATENIN,
        IP3,
        PIP2,
        PIP3,
        PIP3_AKT,
        pAKT,
        ppAKT,
        PIP3_PDK1,
        PIP3_pAKT,
        mTORC2,
        PIP3_ppAKT,
        pGSK3b,
        pTSC2,
        TSC,
        DAG_PKC,
        pRKIP,
        RKIP_CRaf,
        pERK,
        ppERK,
        pFOXO,
        RhebT,
        pS6K,
        pEIF4EBP1,
        G2_SOS_ppERK,
        CRaf_ppERK,
        RasD_DAG_GRP,
        RasT_NF1,
        NF1_ppERK,
        MEK_RasT_CRaf_BRaf,
        pMEK_RasT_CRaf_BRaf,
        ERK_ppMEK,
        pERK_ppMEK,
        RSK_ppERK,
        pRSKnuc_MKP1,
        ppERKnuc_MKP1,
        cFos_pRSKnuc,
        cFos_ppERKnuc,
        RKIP_DAG_PKC,
        PIP3_PTEN,
        PIP3_AKT_PIP3_PDK1,
        PIP3_pAKT_mTORC2,
        GSK3b_ppAKT,
        bCATENIN_GSK3b,
        TSC2_ppAKT,
        TSC2_ppERK,
        RhebT_TSC,
        EIF4EBP1_mTORC1active,
        S6K_mTORC1active,
        FOXO_ppAKT,
        PI3K1_mTORC1active,
        pERK_MKP3,
        ppERK_MKP3,
        ppERKnuc_pMKP1,
        RasT_BRaf,
        RasT_BRaf_BRaf,
        MEK_RasT_BRaf_BRaf,
        pMEK_RasT_BRaf_BRaf,
        EIF4EBP1_EIF4E,
        RasT_CRaf_CRaf,
        MEK_RasT_CRaf_CRaf,
        pMEK_RasT_CRaf_CRaf,
        FOXOnuc,
        MEKi_ppMEK,
        AKTi_AKT]);

        Pds = np.matrix.transpose(Pds)



        to_flatten = [Ads,Rds,RPds,Pds]




        Xds = np.array([])

        for item in to_flatten:
            Xds = np.append(Xds,item)


        vXd= np.multiply(kXd,Xds);



        # ## PUTTING IT TOGETHER  ##

        to_flatten = [vRP1,vRP2,vRP3,vRP4,vRP5,vRP6,vRP7,vRP8,vRP9,vRP10,vRP11,vRP12,vRP13,vRP14,vRP15,vRP16,vRP17,vRP18,vRP19,vRP20,vRP21,vRP22,vRP23,vRP24,vRP25,vRP26,vRP27,vRP28,vRP29,vRP30,vRP31,vRP32,vRP33,vRP34]


        vRP = np.array([])

        for item in to_flatten:
            vRP = np.append(vRP,item)


        # v=[vbR;vdR;vTL;vTLCd';vE';vD';vC';vA';vR';vRP;vP';vDP';vPA';vXd];
        v_temp = [vbR,vdR,vTL,np.matrix.transpose(vTLCd),np.matrix.transpose(vE),np.matrix.transpose(vD),np.matrix.transpose(vC),np.matrix.transpose(vA),np.matrix.transpose(vR),vRP,np.matrix.transpose(vP),np.matrix.transpose(vDP),np.matrix.transpose(vPA),vXd]


        v = np.array([])

        for item in v_temp:
            v = np.append(v,item)


        v = np.matrix(v);
        v = np.matrix.transpose(v)


        v = v[0:2448,:]
        # getting rid of two 0s on the end to get the sizes to match



        ndot=S_PARCDL * (np.multiply(v,(VvPARCDL*1E12)));



        temp = S_PARCDL[772,:]




        ydot=ndot/(VxPARCDL*1E12);


        flag=0;
        new_data = [];


        ydot[np.isnan(ydot)] = 0
        to_return = []
        for i in range(0,774):
            to_return.append(ydot[i,0])



        return to_return
