# this file adds our system of ODEs to teh Explicit_Problem class in assimulo


import numpy as np
from assimulo.problem import Explicit_Problem




class MyProblem(Explicit_Problem):
    def __init__(self, y0,dataS, Jeval774):
        Explicit_Problem.__init__(self,y0=y0)
        self.dataS = dataS
        self.Jeval774 = Jeval774





    def jac(self,t,x):
        return self.Jeval774(t,x,self.dataS)


    #Define the rhs

    def rhs(self,t,x):

        # returns [ydot,flag,newdata,v]



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
        p53inac =xD[0];
        p53ac =xD[1];
        Mdm2 =xD[2];
        Wip1 =xD[3];
        ATMP =xD[4];
        ATRac =xD[5];
        Mdm2product1=xD[6];
        Mdm2product2=xD[7];
        Mdm2product3=xD[8];
        Mdm2product4=xD[10-1];
        Mdm2product5=xD[10];
        Mdm2product6=xD[11];
        Mdm2product7=xD[12];
        Mdm2product8=xD[13];
        Mdm2product9=xD[14];
        Mdm2pro =xD[15];
        Wip1product1=xD[16];
        Wip1product2=xD[17];
        Wip1product3=xD[18];
        Wip1product4=xD[20-1];
        Wip1product5=xD[20];
        Wip1product6=xD[21];
        Wip1product7=xD[22];
        Wip1product8=xD[23];
        Wip1product9=xD[24];
        Wip1pro =xD[25];
        BRCA2=xD[26];
        MSH6=xD[27];
        MGMT=xD[28];
        damageDSB=xD[30-1];
        damageSSB=xD[30];
        ppAKT_Mdm2=xD[31];
        pMdm2=xD[32];
        ARF=xD[33];
        MDM4=xD[34];
        p53ac_MDM4=xD[35];
        ATMinac=xD[36];
        ATRinac=xD[37];



        # ## xC **
        pRB=xC[0];
        pRBp=xC[1];
        pRBpp=xC[2];
        E2F=xC[3];
        Cd=xC[4];
        Mdi=xC[5];
        Md=xC[6];
        Mdp27=xC[7];
        Ce=xC[8];
        Mei=xC[10-1];
        Me=xC[10];
        Skp2=xC[11];
        Mep27=xC[12];
        Pe=xC[13];
        Pai=xC[14];
        Pei=xC[15];
        Pbi=xC[16];
        Ca=xC[17];
        Mai=xC[18];
        Ma=xC[20-1];
        Map27=xC[20];
        p27=xC[21];
        Cdh1i=xC[22];
        Cdh1a=xC[23];
        E2Fp=xC[24];
        p27p=xC[25];
        Pa=xC[26];
        Cb=xC[27];
        Mbi=xC[28];
        Mb=xC[30-1];
        Cdc20i=xC[30];
        Cdc20a=xC[31];
        Pb=xC[32];
        Wee1=xC[33];
        Wee1p=xC[34];
        Mbp27=xC[35];
        Chk1=xC[36];
        pRBc1=xC[37];
        pRBc2=xC[38];
        p21=xC[40-1];
        Mdp21=xC[40];
        Mep21=xC[41];
        Map21=xC[42];
        Mbp21=xC[43];



        # ## xA **
        L =xA[0];
        R =xA[1];
        L_R =xA[2];
        Ractive =xA[3];
        flip =xA[4];
        Ractive_flip =xA[5];
        pC8 =xA[6];
        Ractive_pC8 =xA[7];
        C8 =xA[8];
        Bar =xA[10-1];
        C8_Bar =xA[10];
        pC3 =xA[11];
        C8_pC3 =xA[12];
        C3 =xA[13];
        pC6 =xA[14];
        C3_pC6 =xA[15];
        C6 =xA[16];
        C6_C8 =xA[17];
        XIAP =xA[18];
        C3_XIAP =xA[20-1];
        PARP =xA[20];
        C3_PARP =xA[21];
        cPARP =xA[22];
        Bid =xA[23];
        C8_Bid =xA[24];
        tBid =xA[25];
        Bcl2c =xA[26];
        tBid_Bcl2c =xA[27];
        Bax =xA[28];
        tBid_Bax =xA[30-1];
        Baxactive =xA[30];
        Baxm =xA[31];
        Bcl2 =xA[32];
        Baxm_Bcl2 =xA[33];
        Bax2 =xA[34];
        Bax2_Bcl2 =xA[35];
        Bax4 =xA[36];
        Bax4_Bcl2 =xA[37];
        M =xA[38];
        Bax4_M =xA[40-1];
        Mactive =xA[40];
        CytoCm =xA[41];
        Mactive_CytoCm =xA[42];
        CytoCr =xA[43];
        Smacm =xA[44];
        Mactive_Smacm =xA[45];
        Smacr =xA[46];
        CytoC =xA[47];
        Apaf =xA[48];
        CytoC_Apaf =xA[50-1];
        Apafactive =xA[50];
        pC9 =xA[51];
        Apop =xA[52];
        Apop_C3 =xA[53];
        Smac =xA[54];
        Apop_XIAP =xA[55];
        Smac_XIAP =xA[56];
        C3_Ub =xA[57];
        BAD=xA[58];
        PUMA=xA[60-1];
        NOXA=xA[60];
        Bcl2c_BAD=xA[61];
        Bcl2c_PUMA=xA[62];
        Bcl2c_NOXA=xA[63];
        BIM=xA[64];
        BIM_Bax=xA[65];
        Bcl2c_BIM=xA[66];
        ppERK_BIM=xA[67];
        pBIM=xA[68];
        ppAKT_BAD=xA[70-1];
        pBAD=xA[70];
        ppERK_BAD=xA[71]


        ### xR **
        E=xR[0];
        H=xR[1];
        HGF=xR[2];
        P=xR[3];
        F=xR[4];
        I=xR[5];
        IN=xR[6];
        E1=xR[7];
        pE1=xR[8];
        E2=xR[10-1];
        pE2=xR[10];
        E3=xR[11];
        E4=xR[12];
        pE4=xR[13];
        Ev3=xR[14];
        Met=xR[15];
        Pr=xR[16];
        Fr=xR[17];
        Ir=xR[18];
        Isr =xR[20-1];
        E1E1=xR[20];
        E1E2=xR[21];
        E1E3=xR[22];
        E1E4=xR[23];
        E2E2=xR[24];
        E2E3=xR[25];
        E2E4=xR[26];
        E3E4=xR[27];
        E4E4=xR[28];
        Met_Met=xR[30-1];
        FrFr=xR[30];
        IrIr=xR[31];
        Isr_Isr=xR[32];
        EE1=xR[33];
        HE3=xR[34];
        HE4=xR[35];
        HGF_Met=xR[36];
        PPr=xR[37];
        FFr=xR[38];
        EE1E2=xR[40-1];
        EE1Ev3=xR[40];
        EE1E1=xR[41];
        EE1E3=xR[42];
        EE1E4=xR[43];
        E2HE3=xR[44];
        E1HE3=xR[45];
        HE3E3=xR[46];
        HE3Ev3=xR[47];
        HE3E4=xR[48];
        E2HE4=xR[50-1];
        HE4Ev3=xR[50];
        E1HE4=xR[51];
        E3HE4=xR[52];
        HE4E4=xR[53];
        HGF_Met_Met=xR[54];
        PPrPr=xR[55];
        FFrFr=xR[56];
        IIrIr=xR[57];
        IN_Isr_Isr=xR[58];
        EE1EE1=xR[60-1];
        EE1HE3=xR[60];
        EE1HE4=xR[61];
        HE3HE3=xR[62];
        HE3HE4=xR[63];
        HE4HE4=xR[64];
        HGF_Met_HGF_Met=xR[65];
        PPrPPr=xR[66];
        FFrFFr=xR[67];
        IIrIrI=xR[68];
        IN_Isr_Isr_IN=xR[70-1];
        E1_ppERK=xR[70];
        E2_ppERK=xR[71];
        E4_ppERK=xR[72];


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
        pIIrIr=xRP[25];
        pIN_Isr_Isr=xRP[26];
        pIIrIrI=xRP[27];
        pIN_Isr_Isr_IN=xRP[28];
        pIIrIr_IRS=xRP[30-1];
        pIN_Isr_Isr_IRS=xRP[30];
        pIIrIrI_IRS=xRP[31];
        pIN_Isr_Isr_IN_IRS=xRP[32];



        pIIrIr_int=xRP[116];
        pIN_Isr_Isr_int=xRP[117];
        pIIrIrI_int=xRP[118];
        pIN_Isr_Isr_IN_int=xRP[120-1];
        pIIrIr_int_IRS=xRP[120];
        pIN_Isr_Isr_int_IRS=xRP[121];
        pIIrIrI_int_IRS=xRP[122];
        pIN_Isr_Isr_IN_int_IRS=xRP[123];



        # ## xP **
        IRS=xP[0];
        Sp=xP[1];
        Cbl=xP[2];
        G2=xP[3];
        G2_SOS=xP[4];
        G2_pSOS=xP[5];
        PLCg=xP[6];
        PI3KC1=xP[7];
        PI3KR1=xP[8];
        PI3K1=xP[10-1];
        pPI3K1=xP[10];
        PI3K2=xP[11];
        mTORC1=xP[12];
        mTORC1active=xP[13];
        PIP=xP[14];




        PI3P=xP[15];
        DAG=xP[16];
        GRP=xP[17];
        DAG_GRP=xP[18];
        RasT=xP[20-1];
        RasD=xP[20];
        NF1=xP[21];
        pNF1=xP[22];
        pCRaf=xP[23];
        CRaf=xP[24];
        RasT_CRaf=xP[25];
        BRaf=xP[26];
        RasT_CRaf_BRaf=xP[27];
        MEK=xP[28];
        pMEK=xP[30-1];
        ppMEK=xP[30];
        MKP3=xP[31];
        ERKnuc=xP[32];
        ppERKnuc=xP[33];
        RSK=xP[34];
        pRSK=xP[35];
        pRSKnuc=xP[36];
        MKP1=xP[37];
        pMKP1=xP[38];
        cFos=xP[40-1];
        pcFos=xP[40];
        cJun=xP[41];
        pcFos_cJun=xP[42];
        cMyc=xP[43];
        bCATENINnuc=xP[44];
        bCATENIN=xP[45];
        pbCATENIN=xP[46];
        IP3=xP[47];
        PIP2=xP[48];
        PIP3=xP[50-1];
        PTEN=xP[50];
        PIP3_AKT=xP[51];
        AKT=xP[52];


        pAKT=xP[53];
        ppAKT=xP[54];
        PDK1=xP[55];
        PIP3_PDK1=xP[56];
        PIP3_pAKT=xP[57];
        Rictor=xP[58];
        mTOR=xP[60-1];
        mTORC2=xP[60];
        PIP3_ppAKT=xP[61];
        GSK3b=xP[62];
        pGSK3b=xP[63];
        TSC1=xP[64];
        TSC2=xP[65];
        pTSC2=xP[66];
        TSC=xP[67];
        PKC=xP[68];
        DAG_PKC=xP[70-1];
        pRKIP=xP[70];
        RKIP=xP[71];
        RKIP_CRaf=xP[72];
        ERK=xP[73];
        pERK=xP[74];
        ppERK=xP[75];
        FOXO=xP[76];
        pFOXO=xP[77];
        RhebD=xP[78];
        RhebT=xP[80-1];
        Raptor=xP[80];
        S6K=xP[81];
        pS6K=xP[82];
        EIF4EBP1=xP[83];
        pEIF4EBP1=xP[84];
        SOS=xP[85];
        G2_SOS_ppERK=xP[86];
        CRaf_ppERK=xP[87];
        RasD_DAG_GRP=xP[88];
        RasT_NF1=xP[90-1];
        NF1_ppERK=xP[90];
        MEK_RasT_CRaf_BRaf=xP[91];
        pMEK_RasT_CRaf_BRaf=xP[92];
        ERK_ppMEK=xP[93];
        pERK_ppMEK=xP[94];
        RSK_ppERK=xP[95];
        pRSKnuc_MKP1=xP[96];
        ppERKnuc_MKP1=xP[97];
        cFos_pRSKnuc=xP[98];
        cFos_ppERKnuc=xP[100-1];
        RKIP_DAG_PKC=xP[100];
        PIP3_PTEN=xP[101];
        PIP3_AKT_PIP3_PDK1=xP[102];
        PIP3_pAKT_mTORC2=xP[103];
        GSK3b_ppAKT=xP[104];
        bCATENIN_GSK3b=xP[105];
        TSC2_ppAKT=xP[106];
        TSC2_ppERK=xP[107];
        RhebT_TSC=xP[108];
        EIF4EBP1_mTORC1active=xP[110-1];
        S6K_mTORC1active=xP[110];
        FOXO_ppAKT=xP[111];
        PI3K1_mTORC1active=xP[112];
        pERK_MKP3=xP[113];
        ppERK_MKP3=xP[114];
        ppERKnuc_pMKP1=xP[115];
        RasT_BRaf=xP[116];
        RasT_BRaf_BRaf=xP[117];
        MEK_RasT_BRaf_BRaf=xP[118];
        pMEK_RasT_BRaf_BRaf=xP[120-1];
        EIF4E=xP[120];
        EIF4EBP1_EIF4E=xP[121];
        RasT_CRaf_CRaf=xP[122];
        MEK_RasT_CRaf_CRaf=xP[123];
        pMEK_RasT_CRaf_CRaf=xP[124];
        FOXOnuc=xP[125];

        MEKi=xP[126];
        MEKi_ppMEK=xP[127];
        AKTi=xP[128];
        AKTi_AKT=xP[130-1];



        # ###### RATE CONSTANTS ASSIGNMENT

        # ###DNA Damage Rate Constants
        bp=kD[0];
        ampi=kD[1];
        api=kD[2];
        bsp=kD[3];
        ns=kD[4];
        Ts=kD[5];
        ampa=kD[6];
        awpa=kD[7];
        bm=kD[8];
        bmi=kD[10-1];
        am=kD[10];
        asm=kD[11];
        bw=kD[12];
        aw=kD[13];
        asm2=kD[14];
        aws=kD[15];
        nw=kD[16];
        Tw=kD[17];



        as_=kD[18];
        # NOTE - had to change name of this variable because "as" is a reserved word in python


        bs=kD[20-1];
        bs2=kD[20];
        tau1=kD[21];
        tau2=kD[22];
        tau3=kD[23];
        tau4=kD[24];
        tau5=kD[25];
        tau6=kD[26];
        tau7=kD[27];
        tau8=kD[28];
        tau9=kD[30-1];
        tau10=kD[30];
        tau11=kD[31];
        tau12=kD[32];
        tau13=kD[33];
        tau14=kD[34];
        tau15=kD[35];
        tau16=kD[36];
        tau17=kD[37];
        tau18=kD[38];
        tau19=kD[40-1];
        tau20=kD[40];



        kD[41]=kD[41];
        kD[42]=kD[42];
        kD[43]=kD[43];
        kD[44]=kD[44];
        fixdsb1 =kD[45];
        fixmsh =kD[46];
        fixmgmt =kD[47];
        basalp53act=kD[48];
        kDDbasal=kD[50-1];
        kDDE=kD[50];
        kDEtop=kD[51];
        Etop=kD[52];
        kDnSP=kD[53];
        kDkmSP=kD[54];
        kDnSS=kD[55];
        kDnDS=kD[56];
        kDkmSS=kD[57];
        kDkmDS=kD[58];




        # ### Cell Cycle Rate Constants
        aa=kC[0];
        ab=kC[1];
        ae=kC[2];
        cdk1tot=kC[3];
        cdk2tot=kC[4];
        cdk4tot=kC[5];
        Chk1tot=kC[6];
        eps=kC[7];
        ib=kC[8];
        ib1=kC[10-1];
        ib2=kC[10];
        ib3=kC[11];
        K1=kC[12];
        K1a=kC[13];
        K1b=kC[14];
        K1cdh1=kC[15];
        K1chk=kC[16];
        K1d=kC[17];
        K1e=kC[18];
        K1e2f=kC[20-1];
        K1p27=kC[20];
        K2=kC[21];
        K2a=kC[22];
        K2b=kC[23];
        K2cdh1=kC[24];
        K2chk=kC[25];
        K2d=kC[26];
        K2e=kC[27];
        K2e2f=kC[28];
        K2p27=kC[30-1];
        K3=kC[30];
        K3b=kC[31];
        K4=kC[32];
        K4b=kC[33];
        K5a=kC[34];
        K5b=kC[35];
        K5e=kC[36];
        K6a=kC[37];
        K6b=kC[38];
        K6e=kC[40-1];
        K7b=kC[40];
        K8b=kC[41];
        Kacdc20=kC[42];
        kc1=kC[43];
        kc10=kC[44];
        kc11=kC[45];
        kc12=kC[46];
        kc13=kC[47];
        kc14=kC[48];
        kc15=kC[50-1];



        kc16=kC[50];
        kc2=kC[51];
        kc3=kC[52];
        kc4=kC[53];
        kc5=kC[54];
        kc6=kC[55];
        kc7=kC[56];
        kc8=kC[57];
        kc9=kC[58];
        kca=kC[60-1];
        kcd2=kC[60];
        Kcdh1=kC[61];
        kce=kC[62];
        kcom1=kC[63];
        kcom2=kC[64];
        kcom3=kC[65];
        kcom4=kC[66];
        Kda=kC[67];
        Kdb=kC[68];
        Kdbcdc20=kC[70-1];
        Kdbcdh1=kC[70];
        kdcdc20a=kC[71];
        kdcdc20i=kC[72];
        kdcdh1a=kC[73];
        kdcdh1i=kC[74];
        Kdceskp2=kC[75];
        Kdd=kC[76];
        kdda=kC[77];
        kddb=kC[78];
        kddd=kC[80-1];
        kdde=kC[80];
        kddp21=kC[81];
        kddp27=kC[82];
        kddp27p=kC[83];
        kddskp2=kC[84];
        Kde=kC[85];
        kde2f=kC[86];
        kde2fp=kC[87];
        kdecom1=kC[88];
        kdecom2=kC[90-1];
        kdecom3=kC[90];
        kdecom4=kC[91];
        Kdp27p=kC[92];
        Kdp27skp2=kC[93];
        kdpa=kC[94];
        kdpai=kC[95];
        kdpb=kC[96];
        kdpbi=kC[97];
        kdpe=kC[98];
        kdpei=kC[100-1];
        kdprb=kC[100];
        kdprbp=kC[101];
        kdprbpp=kC[102];
        Kdskp2=kC[103];
        kdWee1=kC[104];
        kdWee1p=kC[105];
        Ki10=kC[106];
        Ki11=kC[107];
        Ki12=kC[108];
        Ki13=kC[110-1];
        Ki14=kC[110];
        Ki7=kC[111];
        Ki8=kC[112];
        Ki9=kC[113];
        kpc1=kC[114];
        kpc2=kC[115];
        kpc3=kC[116];
        kpc4=kC[117];
        V1=kC[118];
        V1cdh1=kC[120-1];
        V1chk=kC[120];
        V1e2f=kC[121];
        V1p27=kC[122];
        V2=kC[123];
        V2cdh1=kC[124];
        V2chk=kC[125];
        V2e2f=kC[126];
        V2p27=kC[127];
        V3=kC[128];
        V4=kC[130-1];
        V6a=kC[130];
        V6b=kC[131];
        V6e=kC[132];
        vcb=kC[133];
        Vda=kC[134];
        Vdb=kC[135];
        Vdd=kC[136];
        Vde=kC[137];
        Vdp27p=kC[138];
        Vdskp2=kC[140-1];
        Vm1a=kC[140];
        Vm1b=kC[141];
        Vm1d=kC[142];
        Vm1e=kC[143];
        Vm2a=kC[144];
        Vm2b=kC[145];





        Vm2d=kC[146];
        Vm2e=kC[147];
        Vm3b=kC[148];
        Vm4b=kC[150-1];
        Vm5a=kC[150];
        Vm5b=kC[151];
        Vm5e=kC[152];
        Vm7b=kC[153];
        Vm8b=kC[154];
        vs1p27=kC[155];
        vs2p27=kC[156];
        vscdc20i=kC[157];
        vscdh1a=kC[158];
        vse2f=kC[160-1];
        vspai=kC[160];
        vspbi=kC[161];
        vspei=kC[162];
        vsprb=kC[163];
        vsskp2=kC[164];
        vswee1=kC[165];
        xa1=kC[166];
        xa2=kC[167];
        xb1=kC[168];
        xb2=kC[170-1];
        xe1=kC[170];
        xe2=kC[171];
        kcd1=kC[172];




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
        vTLCd[0]=kTLCd[0]*p53inac;
        vTLCd[1]=kTLCd[1]*Mdm2 ;
        vTLCd[2]=kTLCd[2]*Wip1 ;
        vTLCd[3]=kTLCd[3]*BRCA2;
        vTLCd[4]=kTLCd[4]*MSH6;
        vTLCd[5]=kTLCd[5]*MGMT;
        vTLCd[6]=kTLCd[6]*ARF;
        vTLCd[7]=kTLCd[7]*MDM4;
        vTLCd[8]=kTLCd[8]*ATMinac;
        vTLCd[10-1]=kTLCd[10-1]*ATRinac;
        vTLCd[10]=0;#kTLCd[10]*pRB;
        vTLCd[11]=0;#kTLCd[11]*E2F;
        vTLCd[12]=0;#kTLCd[12]*Cd;
        vTLCd[13]=0;#kTLCd[13]*Ce;
        vTLCd[14]=0;#kTLCd[14]*Skp2;
        vTLCd[15]=0;#kTLCd[15]*Pai;
        vTLCd[16]=0;#kTLCd[16]*Pei;
        vTLCd[17]=0;#kTLCd[17]*Pbi;
        vTLCd[18]=0;#kTLCd[18]*Ca;
        vTLCd[20-1]=0;#kTLCd[20-1]*p27;
        vTLCd[20]=0;#kTLCd[20]*Cdh1a;
        vTLCd[21]=0;#kTLCd[21]*Cb;
        vTLCd[22]=0;#kTLCd[22]*Cdc20i;
        vTLCd[23]=0;#kTLCd[23]*Wee1;
        vTLCd[24]=0;#kTLCd[24]*Chk1;
        vTLCd[25]=0;#kTLCd[25]*p21;
        vTLCd[26]=kTLCd[26]*L ;
        vTLCd[27]=kTLCd[27]*R ;
        vTLCd[28]=kTLCd[28]*flip ;
        vTLCd[30-1]=kTLCd[30-1]*pC8 ;
        vTLCd[30]=kTLCd[30]*Bar ;
        vTLCd[31]=kTLCd[31]*pC3 ;
        vTLCd[32]=kTLCd[32]*pC6 ;
        vTLCd[33]=kTLCd[33]*XIAP ;
        vTLCd[34]=kTLCd[34]*PARP ;
        vTLCd[35]=kTLCd[35]*Bid ;
        vTLCd[36]=kTLCd[36]*Bcl2c ;
        vTLCd[37]=kTLCd[37]*Bax ;
        vTLCd[38]=kTLCd[38]*CytoCm ;
        vTLCd[40-1]=kTLCd[40-1]*Smacm ;
        vTLCd[40]=kTLCd[40]*Apaf ;
        vTLCd[41]=kTLCd[41]*pC9 ;
        vTLCd[42]=kTLCd[42]*BAD;
        vTLCd[43]=kTLCd[43]*PUMA;
        vTLCd[44]=kTLCd[44]*NOXA;
        vTLCd[45]=kTLCd[45]*BIM;
        vTLCd[46]=kTLCd[46]*E;
        vTLCd[47]=kTLCd[47]*H;
        vTLCd[48]=kTLCd[48]*HGF;
        vTLCd[50-1]=kTLCd[50-1]*P;
        vTLCd[50]=kTLCd[50]*F;
        vTLCd[51]=kTLCd[51]*I;
        vTLCd[52]=kTLCd[52]*IN;
        vTLCd[53]=kTLCd[53]*E1;
        vTLCd[54]=kTLCd[54]*E2;
        vTLCd[55]=kTLCd[55]*E3;
        vTLCd[56]=kTLCd[56]*E4;
        vTLCd[57]=kTLCd[57]*Ev3;
        vTLCd[58]=kTLCd[58]*Met;
        vTLCd[60-1]=kTLCd[60-1]*Pr;
        vTLCd[60]=kTLCd[60]*Fr;
        vTLCd[61]=kTLCd[61]*Ir;
        vTLCd[62]=kTLCd[62]*Isr;
        vTLCd[63]=kTLCd[63]*IRS;
        vTLCd[64]=kTLCd[64]*Sp;
        vTLCd[65]=kTLCd[65]*Cbl;
        vTLCd[66]=kTLCd[66]*G2;
        vTLCd[67]=kTLCd[67]*PLCg;
        vTLCd[68]=kTLCd[68]*PI3KC1;
        vTLCd[70-1]=kTLCd[70-1]*PI3KR1;
        vTLCd[70]=kTLCd[70]*PI3K2;
        vTLCd[71]=kTLCd[71]*GRP;
        vTLCd[72]=kTLCd[72]*RasD;
        vTLCd[73]=kTLCd[73]*NF1;
        vTLCd[74]=kTLCd[74]*CRaf;
        vTLCd[75]=kTLCd[75]*BRaf;
        vTLCd[76]=kTLCd[76]*MEK;
        vTLCd[77]=kTLCd[77]*MKP3;
        vTLCd[78]=kTLCd[78]*RSK;
        vTLCd[80-1]=kTLCd[80-1]*MKP1;
        vTLCd[80]=kTLCd[80]*cFos;
        vTLCd[81]=kTLCd[81]*cJun;
        vTLCd[82]=kTLCd[82]*cMyc;
        vTLCd[83]=kTLCd[83]*bCATENIN;
        vTLCd[84]=kTLCd[84]*PTEN;
        vTLCd[85]=kTLCd[85]*AKT;
        vTLCd[86]=kTLCd[86]*PDK1;
        vTLCd[87]=kTLCd[87]*Rictor;
        vTLCd[88]=kTLCd[88]*mTOR;
        vTLCd[90-1]=kTLCd[90-1]*GSK3b;
        vTLCd[90]=kTLCd[90]*TSC1;
        vTLCd[91]=kTLCd[91]*TSC2;
        vTLCd[92]=kTLCd[92]*PKC;
        vTLCd[93]=kTLCd[93]*RKIP;
        vTLCd[94]=kTLCd[94]*ERK;
        vTLCd[95]=kTLCd[95]*FOXO;
        vTLCd[96]=kTLCd[96]*RhebD;
        vTLCd[97]=kTLCd[97]*Raptor;
        vTLCd[98]=kTLCd[98]*S6K;
        vTLCd[100-1]=kTLCd[100-1]*EIF4EBP1;
        vTLCd[100]=kTLCd[100]*SOS;
        vTLCd[101]=kTLCd[101]*EIF4E;




        # ## vD **
        # some of these were commented out in the original matlab file, so i kept them commented out
        vD = np.zeros(shape=(66))
        #vD[0]= bp;
        vD[1]= ampi*Mdm2*p53inac;
        vD[2]= basalp53act + bsp*p53inac*(ATMP**ns/(ATMP**ns+Ts**ns)+ATRac**ns/(ATRac**ns+Ts**ns));
        vD[3]= awpa*Wip1*p53ac;
        vD[4]= api*p53inac;
        vD[5]= ampa*Mdm2*p53ac;
        #vD[6]= bm*Mdm2pro;
        #vD[7]= bmi;
        vD[8]= asm*Mdm2*ATMP;
        vD[10-1]= asm2*Mdm2*ATRac;
        vD[10]= am*Mdm2;
        #vD[11]= bw*Wip1pro;
        vD[12]= aw*Wip1;


        vD[13]= bs*((damageDSB**kDnDS)/((kDkmDS**kDnDS)+(damageDSB**kDnDS)));
        vD[14]= aws*ATMP*Wip1**nw/(Wip1**nw+Tw**nw);
        vD[15]= as_*ATMP;
        vD[16]= bs2*((damageSSB**kDnSS)/((kDkmSS**kDnSS)+(damageSSB**kDnSS)));
        vD[17]= as_*ATRac;
        vD[18]= Mdm2product1/tau1;
        vD[20-1]= p53ac/tau1;
        vD[20]= Mdm2product2/tau2;
        vD[21]= Mdm2product1/tau2;
        vD[22]= Mdm2product3/tau3;
        vD[23]= Mdm2product2/tau3;
        vD[24]= Mdm2product4/tau4;
        vD[25]= Mdm2product3/tau4;
        vD[26]= Mdm2product5/tau5;
        vD[27]= Mdm2product4/tau5;
        vD[28]= Mdm2product6/tau6;
        vD[30-1]= Mdm2product5/tau6;
        vD[30]= Mdm2product7/tau7;
        vD[31]= Mdm2product6/tau7;
        vD[32]= Mdm2product8/tau8;
        vD[33]= Mdm2product7/tau8;
        vD[34]= Mdm2product9/tau9;
        vD[35]= Mdm2product8/tau9;
        vD[36]= Mdm2pro/tau10;
        vD[37]= Mdm2product9/tau10;
        vD[38]= Wip1product1/tau11;
        vD[40-1]= p53ac/tau11;
        vD[40]= Wip1product2/tau12;
        vD[41]= Wip1product1/tau12;
        vD[42]= Wip1product3/tau13;
        vD[43]= Wip1product2/tau13;
        vD[44]= Wip1product4/tau14;
        vD[45]= Wip1product3/tau14;
        vD[46]= Wip1product5/tau15;
        vD[47]= Wip1product4/tau15;
        vD[48]= Wip1product6/tau16;
        vD[50-1]= Wip1product5/tau16;
        vD[50]= Wip1product7/tau17;
        vD[51]= Wip1product6/tau17;
        vD[52]= Wip1product8/tau18;
        vD[53]= Wip1product7/tau18;
        vD[54]= Wip1product9/tau19;
        vD[55]= Wip1product8/tau19;
        vD[56]= Wip1pro/tau20;
        vD[57]= Wip1product9/tau20;
        vD[58]=kD[41]*ARF*Mdm2;
        vD[60-1]=kD[42]*ARF*pMdm2;
        vD[60]=kD[43]*MDM4*p53ac;
        vD[61]=kD[44]*p53ac_MDM4;
        vD[62]=fixdsb1*BRCA2*damageDSB;
        vD[63]=fixmsh*MSH6*damageSSB;
        vD[64]=fixmgmt*MGMT*damageSSB;
        vD[65]=(kDDbasal+kDDE*(Etop/(Etop+kDEtop)))*(((Ma+Me)**kDnSP)/(((Ma+Me)**kDnSP)+(kDkmSP**kDnSP)));




        # ## vC **
        vC = np.zeros(shape=(104))
        #vC[0]=vsprb; #pRb(Rb) synthesis
        vC[1]=kpc1*pRB*E2F; #pRb binding to E2F
        vC[2]=kpc2*pRBc1; #dissociation of that pRbE2F complex
        vC[3]=V1*(pRB/(K1+pRB))*(Md+Mdp27); #pRb phosphorylation
        vC[4]=V2*(pRBp/(K2+pRBp)); #pRb dephosphorylation
        vC[5]=kdprb*pRB; #pRb degradation
        vC[6]=V3*(pRBp/(K3+pRBp))*Me; #pRbp phosphorylating to pRbpp
        vC[7]=V4*(pRBpp/(K4+pRBpp)); #pRbpp dephosphorylation to pRbp
        vC[8]=kpc3*pRBp*E2F; #pRbp binding to E2F
        vC[10-1]=kpc4*pRBc2; #pRbp dissociation from E2F
        vC[10]=kdprbp*pRBp; #pRbp degradation
        vC[11]=kdprbpp*pRBpp; #pRbpp degradation
        #vC[12]=vse2f; #E2F synthesis
        vC[13]=V1e2f*Ma*(E2F/(E2F+K1e2f)); #E2F phosphorylation by active CYCACDK2
        vC[14]=V2e2f*(E2Fp/(E2Fp+K2e2f)); #pE2F dephosphorylation to E2F
        vC[15]=kde2f*E2F; #E2F degradation
        vC[16]=kde2fp*E2Fp; #pE2F degradation
        #vC[17]=kcd1+kcd2*E2F*(Ki7/(Ki7+pRB))*(Ki8/(Ki8+pRBp)); #cycd synthesis due to E2f inhibited by pRb and pRbp
        vC[18]=kcom1*Cd*(cdk4tot-(Mdi+Md+Mdp27+Mdp21)); #cycd binding to cdk4/6
        vC[20-1]=kdecom1*Mdi; #dissociation of CYCD from CYCDCDK4/6(i) complex
        vC[20]=Vdd*(Cd/(Kdd+Cd)); #maximum cycd degradation
        vC[21]=kddd*Cd; #non specific cycd degradation
        vC[22]=Vm2d*(Md/(K2d+Md)); #inactivation of CYCDCK4/6(a) or Md
        vC[23]=Vm1d*(Mdi/(K1d+Mdi)); #activation of CYCDCDK4/6(i) or Mdi
        vC[24]=kc1*Md*p27; #CYCDCDK4/6(a) or Md binding to p27
        vC[25]=kc2*Mdp27; #dissociation of CYCDCDK4/6p27 coplex or Mdp27 to Md
        #vC[26]=kce*E2F*(Ki9/(Ki9+pRB))*(Ki10/(Ki10+pRBp)); #CYCE synthesis ##Keep like this for now.
        vC[27]=kcom2*Ce*(cdk2tot-(Mei+Me+Mep27+Mep21+Mai+Ma+Map27+Map21)); #CYCE going into complex with cdk2
        vC[28]=kdecom2*Mei; #dissociation of complex CYCECDK2(i)
        vC[30-1]=Vde*(Skp2/(Kdceskp2+Skp2))*(Ce/(Kde+Ce)); #CYCE degradation
        vC[30]=Vm2e*(Wee1+ib2)*(Me/(K2e+Me)); #inactivation of CYCECDK2
        vC[31]=Vm1e*Pe*(Mei/(K1e+Mei)); #activation of CYCECDK2
        vC[32]=kc3*Me*p27; #CYCECDK2 binding to p27
        vC[33]=kc4*Mep27; #dissociation of CYCECDK2p27
        #vC[34]=vsskp2; #synthesis of SKP2
        vC[35]=Vdskp2*(Skp2/(Kdskp2+Skp2))*(Cdh1a/(Kcdh1+Cdh1a)); #max SKP2 degradation
        vC[36]=kddskp2*Skp2; #non-specific SKP2 degradation
        #vC[37]=vspei; #synthesis of inactivated CDC25(i) or pei
        vC[38]=V6e*(xe1+xe2*Chk1)*(Pe/(K6e+Pe)); #Pei inactivation
        vC[40-1]=Vm5e*(Me+ae)*(Pei/(K5e+Pei)); #Pei activation
        vC[40]=kdpei*Pei; #Pei degradation
        vC[41]=kdpe*Pe; #Pe degradation
        #vC[42]=kca*E2F*(Ki11/(Ki11+pRB))*(Ki12/(Ki12+pRBp)); #CYCA synthesis induced by E2F inhibited by pRb and pRbp ##Keep like this for now.
        vC[43]=kcom3*Ca*(cdk2tot-(Mei+Me+Mep27+Mep21+Mai+Ma+Map27+Map21)); #CYCA binding to CDK2 making CYCACDK2(i) Mai
        vC[44]=kdecom3*Mai; #dissociation of Mai complex
        vC[45]=Vda*(Ca/(Kda+Ca))*(Cdc20a/(Kacdc20+Cdc20a)); #CYCA degradation induced by Cdc20(a)
        vC[46]=kdda*Ca; #non specific CYCA degradation
        vC[47]=Vm2a*(Wee1+ib3)*(Ma/(K2a+Ma)); #inactivation of CYCACDK2(a) or Ma complex
        vC[48]=Vm1a*Pa*(Mai/(K1a+Mai)); #activation of CYCACDK2(i) or Mai complex
        vC[50-1]=kc5*Ma*p27; #Ma binding to P27 making CYCACDK2p27
        vC[50]=kc6*Map27; #dissociation of Map27 to Map and p27
        vC[51]=V1p27*Me*(p27/(p27+K1p27)); #inactivation of p27 by CYCECDK2(a)
        vC[52]=V2p27*(p27p/(p27p+K2p27)); #activation of p27
        vC[53]=Vdp27p*(Skp2/(Skp2+Kdp27skp2))*(p27p/(p27p+Kdp27p)); #max p27p degradation
        vC[54]=kddp27p*p27p; #non specific p27p degradation
        vC[55]=V2cdh1*(Cdh1a/(K2cdh1+Cdh1a))*(Ma+Mb); #inactivation of Cdh1(a)
        vC[56]=V1cdh1*(Cdh1i/(K1cdh1+Cdh1i)); #activation of Cdh1(1)
        vC[57]=kdcdh1i*Cdh1i; #inactive Cdh1(i) degradation
        #vC[58]=vscdh1a; #synthesis of Cdh1(a)
        vC[60-1]=kdcdh1a*Cdh1a; #Cdh1(a) degradation
        #vC[60]=vspai; #CDC25(i) Pai synthesis
        vC[61]=V6a*(xa1+xa2*Chk1)*(Pa/(K6a+Pa)); #Pa Cdc25(a) inactivation to Pai
        vC[62]=Vm5a*(Ma+aa)*(Pai/(K5a+Pai)); #Pai activation to Pa
        vC[63]=kdpai*Pai; #Pai degradation
        vC[64]=kdpa*Pa; #Pa degradation
        #vC[65]=vcb; #CYCB synthesis
        vC[66]=kcom4*Cb*(cdk1tot-(Mbi+Mb+Mbp27+Mbp21)); #CYCB forming CYCBCDK1(i) complex
        vC[67]=kdecom4*Mbi; #dissociation of CYCBCDK1(i) complex
        vC[68]=Vdb*(Cb/(Kdb+Cb))*((Cdc20a/(Kdbcdc20+Cdc20a))+(Cdh1a/(Kdbcdh1+Cdh1a))); #max CYCB degradation induced by Cdc20(a)
        vC[70-1]=kddb*Cb; #non specific CYCB degradation
        vC[70]=Vm2b*(Wee1+ib1)*(Mb/(K2b+Mb)); #Mb inactivation to Mbi
        vC[71]=Vm1b*Pb*(Mbi/(K1b+Mbi)); #Mbi becoming active
        vC[72]=kc7*Mb*p27; #Mb (active CYCBCDK1) binding to p27
        vC[73]=kc8*Mbp27; #dissociation of Mb and p27
        #vC[74]=vscdc20i; #cdc20(i) synthesis
        vC[75]=Vm3b*Mb*(Cdc20i/(K3b+Cdc20i)); #activation of cdc20(i) through phosphorylation by CYCBCDK1
        vC[76]=Vm4b*(Cdc20a/(K4b+Cdc20a)); #cdc20(a) inactivation to cdc20(i)
        vC[77]=kdcdc20i*Cdc20i; #cdc20i degradation
        vC[78]=kdcdc20a*Cdc20a; #degradation of cdc20a
        #vC[80-1]=vspbi; #synthesis of inactive CDC25 Pbi
        vC[80]=V6b*(xb1+xb2*Chk1)*(Pb/(K6b+Pb)); #inactivation of CDC25 (Pb)
        vC[81]=Vm5b*(Mb+ab)*(Pbi/(K5b+Pbi)); #activation of CDC25(i) (Pbi)
        vC[82]=kdpbi*Pbi; #degradation of inactive CDC25 (Pbi)
        vC[83]=kdpb*Pb; #degradation of active CDC25 (Pb)
        #vC[84]=vswee1; #Wee1 synthesis
        vC[85]=Vm7b*(Mb+ib)*(Wee1/(K7b+Wee1)); #wee1 inactivation through phosphorylation due to CYCBCDK1
        vC[86]=Vm8b*(Wee1p/(K8b+Wee1p)); #wee1p(wee1(i)) activation through dephosphorylation
        vC[87]=kdWee1*Wee1; #wee1 degradation
        vC[88]=kdWee1p*Wee1p; #wee1p degradation
        vC[90-1]=V1chk*ATRac*((Chk1tot-Chk1)/(K1chk+(Chk1tot-Chk1))); #activation of Chk1 through phosphorylation by kinase ATR
        vC[90]=V2chk*(Chk1/(K2chk+Chk1)); #Chk1 inactivation through dephosphorylation
        vC[91]=kdde*Ce;#non-specific cycE degradation
        #vC[92]=vs1p27; #+ basal p27 synthesis
        #vC[93]=vs2p27*E2F*(Ki13/(Ki13+pRB))*(Ki14/(Ki14+pRBp)); #+ synthesis of p27 induced by E2F, inhibited by pRB and pRBp ##Keep like this for now.
        vC[94]=kddp27*p27; #- non-specific p27 degradation.
        vC[95]=kc9*Md*p21; #CYCDCDK4/6(a) or Md binding to p21
        vC[96]=kc10*Mdp21; #dissociation of CYCDCDK4/6p21 coplex or Mdp21 to Md
        vC[97]=kc11*Me*p21; #CYCECDK2 binding to p21
        vC[98]=kc12*Mep21; #dissociation of CYCECDK2p21
        vC[100-1]=kc13*Ma*p21; #Ma binding to P21 making CYCACDK2p21
        vC[100]=kc14*Map21; #dissociation of Map21 to Map and p21
        vC[101]=kc15*Mb*p21; #Mb (active CYCBCDK1) binding to p21
        vC[102]=kc16*Mbp21; #dissociation of Mb and p21


        vC[103]=kddp21*p21; #-non-specific p21 degradation
        vC[0:104]=vC[0:104]*eps;






        # ## vA **
        vA = np.zeros(shape=(87))
        vA[0]=kA[0]*L*R *Vc/Ve;
        vA[1]=kA[1]*L_R;
        vA[2]=kA[2]*L_R;
        vA[3]=kA[3]*Ractive*flip;
        vA[4]=kA[4]*Ractive_flip;
        vA[5]=kA[5]*Ractive*pC8;
        vA[6]=kA[6]*Ractive_pC8;
        vA[7]=kA[7]*Ractive_pC8;
        vA[8]=kA[8]*C8*Bar;
        vA[10-1]=kA[10-1]*C8_Bar;
        vA[10]=kA[10]*C8*pC3;
        vA[11]=kA[11]*C8_pC3;
        vA[12]=kA[12]*C8_pC3;
        vA[13]=kA[13]*C3*pC6;
        vA[14]=kA[14]*C3_pC6;
        vA[15]=kA[15]*C3_pC6;
        vA[16]=kA[16]*pC8*C6;
        vA[17]=kA[17]*C6_C8;
        vA[18]=kA[18]*C6_C8;
        vA[20-1]=kA[20-1]*C3*XIAP;
        vA[20]=kA[20]*C3_XIAP;
        vA[21]=kA[21]*C3_XIAP;
        vA[22]=kA[22]*C3*PARP;
        vA[23]=kA[23]*C3_PARP;
        vA[24]=kA[24]*C3_PARP;
        vA[25]=kA[25]*C8*Bid;
        vA[26]=kA[26]*C8_Bid;
        vA[27]=kA[27]*C8_Bid;
        vA[28]=kA[28]*tBid*Bcl2c;
        vA[30-1]=kA[30-1]*tBid_Bcl2c;
        vA[30]=kA[30]*tBid*Bax;
        vA[31]=kA[31]*tBid_Bax;
        vA[32]=kA[32]*tBid_Bax;
        vA[33]=kA[33]*Baxactive;
        vA[34]=kA[34]*Baxm;
        vA[35]=kA[35]*Baxm*Bcl2;
        vA[36]=kA[36]*Baxm_Bcl2;
        vA[37]=kA[37]*Baxm**2;
        vA[38]=kA[38]*Bax2;
        vA[40-1]=kA[40-1]*Bcl2*Bax2;
        vA[40]=kA[40]*Bax2_Bcl2;
        vA[41]=kA[41]*Bax2**2;
        vA[42]=kA[42]*Bax4;
        vA[43]=kA[43]*Bcl2*Bax4;
        vA[44]=kA[44]*Bax4_Bcl2;
        vA[45]=kA[45]*M*Bax4;
        vA[46]=kA[46]*Bax4_M;
        vA[47]=kA[47]*Bax4_M;
        vA[48]=kA[48]*Mactive*CytoCm;
        vA[50-1]=kA[50-1]*Mactive_CytoCm;
        vA[50]=kA[50]*Mactive_CytoCm;
        vA[51]=kA[51]*Mactive*Smacm;
        vA[52]=kA[52]*Mactive_Smacm;
        vA[53]=kA[53]*Mactive_Smacm;
        vA[54]=kA[54]*CytoCr;
        vA[55]=kA[55]*CytoC;
        vA[56]=kA[56]*CytoC*Apaf;
        vA[57]=kA[57]*CytoC_Apaf;
        vA[58]=kA[58]*CytoC_Apaf;
        vA[60-1]=kA[60-1]*Apafactive*pC9;
        vA[60]=kA[60]*Apop;
        vA[61]=kA[61]*pC3*Apop;
        vA[62]=kA[62]*Apop_C3;
        vA[63]=kA[63]*Apop_C3;
        vA[64]=kA[64]*Smacr;
        vA[65]=kA[65]*Smac;
        vA[66]=kA[66]*XIAP*Apop;
        vA[67]=kA[67]*Apop_XIAP;
        vA[68]=kA[68]*XIAP*Smac;
        vA[70-1]=kA[70-1]*Smac_XIAP;
        vA[70]=kA[70]*Bcl2c*BAD;
        vA[71]=kA[71]*Bcl2c_BAD;
        vA[72]=kA[72]*Bcl2c*PUMA;
        vA[73]=kA[73]*Bcl2c_PUMA;
        vA[74]=kA[74]*Bcl2c*NOXA;
        vA[75]=kA[75]*Bcl2c_NOXA;


        vA[76]=kA[76]*BIM*Bax;

        vA[77]=kA[77]*BIM_Bax;
        vA[78]=kA[78]*BIM_Bax;
        vA[80-1]=kA[80-1]*Bcl2c*BIM;
        vA[80]=kA[80]*Bcl2c_BIM;
        vA[81]=kA[81]*Mactive;
        vA[82]=kA[82]*Smacr;
        vA[83]=kA[83]*CytoCr;
        vA[84]=kA[84]*Bcl2c;
        vA[85]=kA[85]*Bcl2;
        vA[86]=kA[86]*pC8;



        # ## vR **
        vR = np.zeros(shape=(158))
        vR[0]=kR[0]*E1*E *Vc/Ve;
        vR[1]=kR[1]*EE1 ;
        vR[2]=kR[2]*EE1*E2 ;
        vR[3]=kR[3]*EE1E2 ;
        vR[4]=kR[4]*EE1*E1 ;
        vR[5]=kR[5]*EE1E1 ;
        vR[6]=kR[6]*EE1E1*E *Vc/Ve;
        vR[7]=2*kR[7]*EE1EE1 ;
        vR[8]=kR[8]*EE1EE1 ;
        vR[10-1]=kR[10-1]*EE1*EE1 ;
        vR[10]=kR[10]*EE1*E3 ;
        vR[11]=kR[11]*EE1E3 ;
        vR[12]=kR[12]*EE1E3*H *Vc/Ve;
        vR[13]=kR[13]*EE1HE3 ;
        vR[14]=kR[14]*EE1HE3 ;
        vR[15]=kR[15]*EE1*HE3 ;
        vR[16]=kR[16]*EE1*Ev3 ;
        vR[17]=kR[17]*EE1Ev3 ;
        vR[18]=kR[18]*EE1*E4 ;
        vR[20-1]=kR[20-1]*EE1E4 ;
        vR[20]=kR[20]*EE1E4*H *Vc/Ve;
        vR[21]=kR[21]*EE1HE4 ;
        vR[22]=kR[22]*EE1HE4 ;
        vR[23]=kR[23]*EE1*HE4 ;
        vR[24]=kR[24]*H*E3 *Vc/Ve;
        vR[25]=kR[25]*HE3 ;
        vR[26]=kR[26]*HE3*E2 ;
        vR[27]=kR[27]*E2HE3 ;
        vR[28]=kR[28]*HE3*E1 ;
        vR[30-1]=kR[30-1]*E1HE3 ;
        vR[30]=kR[30]*E1HE3*E *Vc/Ve;
        vR[31]=kR[31]*EE1HE3 ;
        vR[32]=kR[32]*HE3*E3 ;
        vR[33]=kR[33]*HE3E3 ;
        vR[34]=kR[34]*HE3E3*H *Vc/Ve;
        vR[35]=2*kR[35]*HE3HE3 ;
        vR[36]=kR[36]*HE3HE3 ;
        vR[37]=kR[37]*HE3*HE3 ;
        vR[38]=kR[38]*HE3*Ev3 ;
        vR[40-1]=kR[40-1]*HE3Ev3 ;
        vR[40]=kR[40]*HE3*E4 ;
        vR[41]=kR[41]*HE3E4 ;
        vR[42]=kR[42]*HE3E4*H *Vc/Ve;
        vR[43]=kR[43]*HE3HE4 ;
        vR[44]=kR[44]*HE3HE4 ;
        vR[45]=kR[45]*HE3*HE4 ;
        vR[46]=kR[46]*H*E4 *Vc/Ve;
        vR[47]=kR[47]*HE4 ;
        vR[48]=kR[48]*HE4*E2 ;
        vR[50-1]=kR[50-1]*E2HE4 ;
        vR[50]=kR[50]*HE4*E1 ;
        vR[51]=kR[51]*E1HE4 ;
        vR[52]=kR[52]*E1HE4*E *Vc/Ve;
        vR[53]=kR[53]*EE1HE4 ;
        vR[54]=kR[54]*HE4*E3 ;
        vR[55]=kR[55]*E3HE4 ;
        vR[56]=kR[56]*E3HE4*H *Vc/Ve;
        vR[57]=kR[57]*HE3HE4 ;
        vR[58]=kR[58]*HE4*Ev3 ;
        vR[60-1]=kR[60-1]*HE4Ev3 ;
        vR[60]=kR[60]*HE4*E4 ;
        vR[61]=kR[61]*HE4E4 ;
        vR[62]=kR[62]*HE4E4*H *Vc/Ve;
        vR[63]=2*kR[63]*HE4HE4 ;
        vR[64]=kR[64]*HE4HE4 ;
        vR[65]=kR[65]*HE4*HE4 ;
        vR[66]=kR[66]*E1*ppERK ;
        vR[67]=kR[67]*pE1 ;
        vR[68]=kR[68]*E2*ppERK ;
        vR[70-1]=kR[70-1]*pE2 ;
        vR[70]=kR[70]*E4*ppERK ;
        vR[71]=kR[71]*pE4 ;
        vR[72]=kR[72]*Met*HGF *Vc/Ve;
        vR[73]=kR[73]*HGF_Met ;
        vR[74]=kR[74]*HGF_Met*Met ;
        vR[75]=kR[75]*HGF_Met_Met ;
        vR[76]=kR[76]*HGF_Met_Met*HGF *Vc/Ve;
        vR[77]=2*kR[77]*HGF_Met_HGF_Met ;
        vR[78]=kR[78]*HGF_Met_HGF_Met ;
        vR[80-1]=kR[80-1]*HGF_Met*HGF_Met ;
        vR[80]=kR[80]*Pr*P *Vc/Ve;
        vR[81]=kR[81]*PPr ;
        vR[82]=kR[82]*PPr*PPr ;
        vR[83]=kR[83]*PPrPPr ;
        vR[84]=2*kR[84]*PPrPPr ;
        vR[85]=kR[85]*PPrPr ;
        vR[86]=kR[86]*Fr*F *Vc/Ve;
        vR[87]=kR[87]*FFr;
        vR[88]=kR[88]*FFr*FFr;
        vR[90-1]=kR[90-1]*FFrFFr;
        vR[90]=2*kR[90]*FFrFFr;
        vR[91]=kR[91]*F*FFrFr *Vc/Ve;
        vR[92]=kR[92]*FFrFr;
        vR[93]=kR[93]*Fr*FFr;
        vR[94]=kR[94]*Ir*Ir;
        vR[95]=kR[95]*IrIr;
        vR[96]=kR[96]*Isr*Isr;
        vR[97]=kR[97]*Isr_Isr;
        vR[98]=kR[98]*E1_ppERK;
        vR[100-1]=kR[100-1]*E1_ppERK;
        vR[100]=kR[100]*E2_ppERK;
        vR[101]=kR[101]*E2_ppERK;
        vR[102]=kR[102]*E4_ppERK;
        vR[103]=kR[103]*E4_ppERK;
        vR[104]=kR[104]*E1*E1;
        vR[105]=kR[105]*E1E1;
        vR[106]=kR[106]*E1*E2;
        vR[107]=kR[107]*E1E2;
        vR[108]=kR[108]*E1*E3;
        vR[110-1]=kR[110-1]*E1E3;
        vR[110]=kR[110]*E1*E4;
        vR[111]=kR[111]*E1E4;
        vR[112]=kR[112]*E2*E2;
        vR[113]=kR[113]*E2E2;
        vR[114]=kR[114]*E2*E3;
        vR[115]=kR[115]*E2E3;
        vR[116]=kR[116]*E2*E4;
        vR[117]=kR[117]*E2E4;
        vR[118]=kR[118]*E3*E4;
        vR[120-1]=kR[120-1]*E3E4;
        vR[120]=kR[120]*E4*E4;
        vR[121]=kR[121]*E4E4;
        vR[122]=2*kR[122]*E*E1E1 *Vc/Ve;
        vR[123]=kR[123]*EE1E1;
        vR[124]=kR[124]*E*E1E2 *Vc/Ve;
        vR[125]=kR[125]*EE1E2;
        vR[126]=kR[126]*E*E1E3 *Vc/Ve;
        vR[127]=kR[127]*EE1E3;
        vR[128]=kR[128]*H*E1E3 *Vc/Ve;
        vR[130-1]=kR[130-1]*E1HE3;
        vR[130]=kR[130]*E*E1E4 *Vc/Ve;
        vR[131]=kR[131]*EE1E4;
        vR[132]=kR[132]*H*E1E4 *Vc/Ve;
        vR[133]=kR[133]*E1HE4;
        vR[134]=kR[134]*H*E2E3 *Vc/Ve;
        vR[135]=kR[135]*E2HE3;
        vR[136]=kR[136]*H*E2E4 *Vc/Ve;
        vR[137]=kR[137]*E2HE4;
        vR[138]=2*kR[138]*H*E3E4 *Vc/Ve;
        vR[140-1]=kR[140-1]*E3HE4;
        vR[140]=2*kR[140]*H*E4E4 *Vc/Ve;
        vR[141]=kR[141]*HE4E4;
        vR[142]=kR[142]*Met*Met;
        vR[143]=kR[143]*Met_Met;
        vR[144]=2*kR[144]*HGF*Met_Met;
        vR[145]=kR[145]*HGF_Met_Met;
        vR[146]=kR[146]*Fr*Fr;
        vR[147]=kR[147]*FrFr;
        vR[148]=2*kR[148]*F*FrFr;
        vR[150-1]=kR[150-1]*FFrFr;
        vR[150]=kR[150]*IrIr*I *Vc/Ve;
        vR[151]=kR[151]*IIrIr;
        vR[152]=kR[152]*IIrIr*I *Vc/Ve;
        vR[153]=kR[153]*IIrIrI;
        vR[154]=kR[154]*Isr_Isr*IN *Vc/Ve;
        vR[155]=kR[155]*IN_Isr_Isr;
        vR[156]=kR[156]*IN_Isr_Isr*IN *Vc/Ve;
        vR[157]=kR[157]*IN_Isr_Isr_IN;


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
        vP[0]=kP[0]*RasT*CRaf;
        vP[1]=kP[1]*RasT_CRaf;
        vP[2]=kP[2]*RasT*BRaf;
        vP[3]=kP[3]*RasT_BRaf;
        vP[4]=kP[4]*RasT_CRaf*RasT_CRaf;
        vP[5]=kP[5]*RasT_CRaf_CRaf;
        vP[6]=kP[6]*RasT_BRaf*RasT_BRaf;
        vP[7]=kP[7]*RasT_BRaf_BRaf;
        vP[8]=kP[8]*RasT_CRaf*RasT_BRaf;
        vP[10-1]=kP[10-1]*RasT_CRaf_BRaf;
        vP[10]=0;#kP[10]*RasT_BRaf*CRaf;
        vP[11]=0;#kP[11]*RasT_CRaf_BRaf;
        vP[12]=kP[12]*MEK*RasT_CRaf_CRaf;
        vP[13]=kP[13]*MEK_RasT_CRaf_CRaf;
        vP[14]=kP[14]*MEK_RasT_CRaf_CRaf;
        vP[15]=kP[15]*pMEK*RasT_CRaf_CRaf;
        vP[16]=kP[16]*pMEK_RasT_CRaf_CRaf;
        vP[17]=kP[17]*pMEK_RasT_CRaf_CRaf;
        vP[18]=kP[18]*MEK*RasT_BRaf_BRaf;
        vP[20-1]=kP[20-1]*MEK_RasT_BRaf_BRaf;
        vP[20]=kP[20]*MEK_RasT_BRaf_BRaf;
        vP[21]=kP[21]*pMEK*RasT_BRaf_BRaf;
        vP[22]=kP[22]*pMEK_RasT_BRaf_BRaf;
        vP[23]=kP[23]*pMEK_RasT_BRaf_BRaf;
        vP[24]=kP[24]*MEK*RasT_CRaf_BRaf;
        vP[25]=kP[25]*MEK_RasT_CRaf_BRaf;
        vP[26]=kP[26]*MEK_RasT_CRaf_BRaf;
        vP[27]=kP[27]*pMEK*RasT_CRaf_BRaf;
        vP[28]=kP[28]*pMEK_RasT_CRaf_BRaf;
        vP[30-1]=kP[30-1]*pMEK_RasT_CRaf_BRaf;
        vP[30]=kP[30]*pMEK;
        vP[31]=kP[31]*ppMEK;
        vP[32]=kP[32]*ERK*ppMEK;
        vP[33]=kP[33]*ERK_ppMEK;
        vP[34]=kP[34]*ERK_ppMEK;
        vP[35]=kP[35]*pERK*ppMEK;
        vP[36]=kP[36]*pERK_ppMEK;
        vP[37]=kP[37]*pERK_ppMEK;
        vP[38]=kP[38]*ppERKnuc*MKP1;
        vP[40-1]=kP[40-1]*ppERKnuc_MKP1;
        vP[40]=kP[40]*ppERKnuc_MKP1;
        vP[41]=kP[41]*pMKP1;
        vP[42]=kP[42]*pcFos;
        vP[43]=kP[43]*pTSC2;
        vP[44]=kP[44]*pRSKnuc;
        vP[45]=kP[45]*G2_SOS*ppERK;
        vP[46]=kP[46]*G2_SOS_ppERK;
        vP[47]=kP[47]*G2_SOS_ppERK;
        vP[48]=kP[48]*G2_pSOS;
        vP[50-1]=kP[50-1]*CRaf*ppERK;
        vP[50]=kP[50]*CRaf_ppERK;
        vP[51]=kP[51]*CRaf_ppERK;
        vP[52]=kP[52]*pCRaf;
        vP[53]=kP[53]*RasD*DAG_GRP;
        vP[54]=kP[54]*RasD_DAG_GRP;
        vP[55]=kP[55]*RasD_DAG_GRP;
        vP[56]=kP[56]*RasT*NF1;
        vP[57]=kP[57]*RasT_NF1;
        vP[58]=kP[58]*RasT_NF1;
        vP[60-1]=kP[60-1]*NF1*ppERK;
        vP[60]=kP[60]*NF1_ppERK;
        vP[61]=kP[61]*NF1_ppERK;
        vP[62]=kP[62]*pNF1;
        vP[63]=kP[63]*pERK*MKP3;
        vP[64]=kP[64]*pERK_MKP3;
        vP[65]=kP[65]*pERK_MKP3;
        vP[66]=kP[66]*ppERK*MKP3;
        vP[67]=kP[67]*ppERK_MKP3;
        vP[68]=kP[68]*ppERK_MKP3;
        vP[70-1]=kP[70-1]*RSK*ppERK;
        vP[70]=kP[70]*RSK_ppERK;
        vP[71]=kP[71]*RSK_ppERK;
        vP[72]=kP[72]*pRSK;
        vP[73]=kP[73]*ppERK;
        vP[74]=kP[74]*ERKnuc;
        vP[75]=kP[75]*ppERKnuc*pMKP1;
        vP[76]=kP[76]*ppERKnuc_pMKP1 ;
        vP[77]=kP[77]*ppERKnuc_pMKP1 ;
        vP[78]=kP[78]*ERKnuc;
        vP[80-1]=kP[80-1]*pRSK;
        vP[80]=kP[80]*MKP1*pRSKnuc;
        vP[81]=kP[81]*pRSKnuc_MKP1;
        vP[82]=kP[82]*pRSKnuc_MKP1;
        vP[83]=kP[83]*MKP1*ppERKnuc;
        vP[84]=kP[84]*ppERKnuc_MKP1;
        vP[85]=kP[85]*ppERKnuc_MKP1;
        vP[86]=kP[86]*cFos*pRSKnuc;
        vP[87]=kP[87]*cFos_pRSKnuc;
        vP[88]=kP[88]*cFos_pRSKnuc;
        vP[90-1]=kP[90-1]*cFos*ppERKnuc;
        vP[90]=kP[90]*cFos_ppERKnuc;
        vP[91]=kP[91]*cFos_ppERKnuc;
        vP[92]=kP[92]*pcFos*cJun;
        vP[93]=kP[93]*pcFos_cJun;
        vP[94]=kP[94]*GRP*DAG;
        vP[95]=kP[95]*DAG_GRP;
        vP[96]=kP[96]*DAG*PKC;
        vP[97]=kP[97]*DAG_PKC;
        vP[98]=kP[98]*RKIP*DAG_PKC;
        vP[100-1]=kP[100-1]*RKIP_DAG_PKC;
        vP[100]=kP[100]*RKIP_DAG_PKC;
        vP[101]=kP[101]*pRKIP;
        vP[102]=kP[102]*RKIP*CRaf;
        vP[103]=kP[103]*RKIP_CRaf;
        vP[104]=kP[104]*PIP3*PTEN;
        vP[105]=kP[105]*PIP3_PTEN;
        vP[106]=kP[106]*PIP3_PTEN;
        vP[107]=kP[107]*PIP3*AKT;
        vP[108]=kP[108]*PIP3_AKT;
        vP[110-1]=kP[110-1]*PIP3*PDK1;
        vP[110]=kP[110]*PIP3_PDK1;
        vP[111]=kP[111]*Rictor*mTOR;
        vP[112]=kP[112]*mTORC2;
        vP[113]=kP[113]*PIP3_AKT*PIP3_PDK1;
        vP[114]=kP[114]*PIP3_AKT_PIP3_PDK1;
        vP[115]=kP[115]*PIP3_AKT_PIP3_PDK1;
        vP[116]=kP[116]*PIP3_pAKT;
        vP[117]=kP[117]*PIP3_pAKT*mTORC2;
        vP[118]=kP[118]*PIP3_pAKT_mTORC2;
        vP[120-1]=kP[120-1]*PIP3_pAKT_mTORC2;
        vP[120]=kP[120]*PIP3_ppAKT;
        vP[121]=kP[121]*PIP3_ppAKT;
        vP[122]=kP[122]*PIP3*ppAKT;
        vP[123]=kP[123]*GSK3b*ppAKT;
        vP[124]=kP[124]*GSK3b_ppAKT;
        vP[125]=kP[125]*GSK3b_ppAKT;
        vP[126]=kP[126]*pGSK3b;


        vP[127]=(kP[127]*bCATENIN*GSK3b**4)/(200**4+GSK3b**4);

        vP[130]=kP[130]*pbCATENIN;
        vP[131]=kP[131]*bCATENIN;
        vP[132]=kP[132]*bCATENINnuc;
        vP[133]=kP[133]*TSC2*ppAKT;
        vP[134]=kP[134]*TSC2_ppAKT;
        vP[135]=kP[135]*TSC2_ppAKT;
        vP[136]=kP[136]*TSC2*ppERK;
        vP[137]=kP[137]*TSC2_ppERK;
        vP[138]=kP[138]*TSC2_ppERK;
        vP[140-1]=kP[140-1]*TSC1*TSC2;
        vP[140]=kP[140]*TSC;
        vP[141]=0;
        vP[142]=0;
        vP[143]=0;
        vP[144]=0;
        vP[145]=kP[145]*mTORC1;

        vP[146]=(kP[146]*mTORC1active*TSC**4)/(.1+TSC**4);

        vP[147]=kP[147]*Raptor*mTOR;
        vP[148]=kP[148]*mTORC1;
        vP[150-1]=kP[150-1]*EIF4EBP1*mTORC1active;
        vP[150]=kP[150]*EIF4EBP1_mTORC1active;
        vP[151]=kP[151]*EIF4EBP1_mTORC1active;
        vP[152]=kP[152]*pEIF4EBP1;
        vP[153]=kP[153]*S6K*mTORC1active;
        vP[154]=kP[154]*S6K_mTORC1active;
        vP[155]=kP[155]*S6K_mTORC1active;
        vP[156]=kP[156]*pS6K;
        vP[157]=kP[157]*FOXO*ppAKT;
        vP[158]=kP[158]*FOXO_ppAKT;
        vP[160-1]=kP[160-1]*FOXO_ppAKT;
        vP[160]=kP[160]*pFOXO;
        vP[161]=kP[161]*PI3K1*mTORC1active;
        vP[162]=kP[162]*PI3K1_mTORC1active;
        vP[163]=kP[163]*PI3K1_mTORC1active;
        vP[164]=kP[164]*pPI3K1;
        vP[165]=kP[165]*PI3KC1*PI3KR1;
        vP[166]=kP[166]*PI3K1;
        vP[167]=kP[167]*PI3P;
        vP[168]=kP[168]*SOS*G2;
        vP[170-1]=kP[170-1]*G2_SOS;
        vP[170]=kP[170]*EIF4E*EIF4EBP1;
        vP[171]=kP[171]*EIF4EBP1_EIF4E;
        vP[172]=kP[172];
        vP[173]=kP[173]*pbCATENIN*TSC;
        vP[174]=kP[174]*pERK;
        vP[175]=kP[175]*ppERK;
        vP[176]=kP[176]*ppERKnuc;
        vP[177]=kP[177]*ppAKT;
        vP[178]=kP[178]*pAKT;
        vP[180-1]=kP[180-1]*RhebT;
        vP[180]=kP[180]*FOXO;
        vP[181]=kP[181]*FOXOnuc;
        vP[182]=kP[182]*PIP2;
        vP[183]=kP[183]*PIP3;
        vP[184]=kP[184]*RasD;
        vP[185]=kP[185]*RasT;
        vP[186]=kP[186]*MEKi*ppMEK;
        vP[187]=kP[187]*MEKi_ppMEK;
        vP[188]=kP[188]*AKTi*AKT;
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
        vPA[0]=kPA[0]*ppERK*BIM;
        vPA[1]=kPA[1]*ppERK_BIM;
        vPA[2]=kPA[2]*ppERK_BIM;
        vPA[3]=kPA[3]*pBIM;
        vPA[4]=kPA[4]*ppAKT*BAD;
        vPA[5]=kPA[5]*ppAKT_BAD;
        vPA[6]=kPA[6]*ppAKT_BAD;
        vPA[7]=kPA[7]*ppERK*BAD;
        vPA[8]=kPA[8]*ppERK_BAD;
        vPA[10-1]=kPA[10-1]*ppERK_BAD;
        vPA[10]=kPA[10]*pBAD;



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



        # return ydot[0:774,0]

        to_return = []
        for i in range(0,774):
            to_return.append(ydot[i,0])




        return to_return
