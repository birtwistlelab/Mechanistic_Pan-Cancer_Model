
import numpy as np
import sys


def PARCDL_compartments(flagOUT,Vc,Ve,Vm,Vn,S_d):

    # returns [Vx,Vv,VxTL]

    numberofgenes=141;


    if flagOUT[2]:
    # VxTL
        VxTL = np.zeros(shape=(numberofgenes))
        VxTL[0:numberofgenes]=Vc;
        VxTL[0:30]=Vn;
        VxTL[47:49]=Vm;
        VxTL[96:100]=Vn;
        VxTL[136:139]=Vn;

    if flagOUT[0]:
    # VxRibosome
        VxRibosome=Vc;



        # VxD
        VxD = np.zeros(shape=(38))
        VxD[0:38]=Vn;



        # VxC
        VxC = np.zeros(shape=(44))
        VxC[0:44]=Vn;


        VxA = np.zeros(shape=(72))
        # VxA

        # reason indices are written weird is cuz i did a search and replace to add -1 to all of them (cuz of weird matlab 1 base indexing)
        VxA[1-1]=Ve;#L
        VxA[2-1]=Vc;#R
        VxA[3-1]=Vc;#L_R
        VxA[4-1]=Vc;#Ractive
        VxA[5-1]=Vc;#flip
        VxA[6-1]=Vc;#Ractive_flip
        VxA[7-1]=Vc;#pC8
        VxA[8-1]=Vc;#Ractive_pC8
        VxA[9-1]=Vc;#C8
        VxA[10-1]=Vc;#Bar
        VxA[11-1]=Vc;#C8_Bar
        VxA[12-1]=Vc;#pC3
        VxA[13-1]=Vc;#C8_pC3
        VxA[14-1]=Vc;#C3
        VxA[15-1]=Vc;#pC6
        VxA[16-1]=Vc;#C3_pC6
        VxA[17-1]=Vc;#C6
        VxA[18-1]=Vc;#C6_C8
        VxA[19-1]=Vc;#XIAP
        VxA[20-1]=Vc;#C3_XIAP
        VxA[21-1]=Vc;#PARP
        VxA[22-1]=Vc;#C3_PARP
        VxA[23-1]=Vc;#cPARP
        VxA[24-1]=Vc;#Bid
        VxA[25-1]=Vc;#C8_Bid
        VxA[26-1]=Vc;#tBid
        VxA[27-1]=Vc;#Bcl2c
        VxA[28-1]=Vc;#tBid_Bcl2c
        VxA[29-1]=Vc;#Bax
        VxA[30-1]=Vc;#tBid_Bax
        VxA[31-1]=Vc;#Baxactive
        VxA[32-1]=Vm;#Baxm
        VxA[33-1]=Vm;#Bcl2
        VxA[34-1]=Vm;#Baxm_Bcl2
        VxA[35-1]=Vm;#Bax2
        VxA[36-1]=Vm;#Bax2_Bcl2
        VxA[37-1]=Vm;#Bax4
        VxA[38-1]=Vm;#Bax4_Bcl2
        VxA[39-1]=Vm;#M
        VxA[40-1]=Vm;#Bax4_M
        VxA[41-1]=Vm;#Mactive
        VxA[42-1]=Vm;#CytoCm
        VxA[43-1]=Vm;#Mactive_CytoCm
        VxA[44-1]=Vm;#CytoCr
        VxA[45-1]=Vm;#Smacm
        VxA[46-1]=Vm;#Mactive_Smacm
        VxA[47-1]=Vm;#Smacr
        VxA[48-1]=Vc;#CytoC
        VxA[49-1]=Vc;#Apaf
        VxA[50-1]=Vc;#CytoC_Apaf
        VxA[51-1]=Vc;#Apafactive
        VxA[52-1]=Vc;#pC9
        VxA[53-1]=Vc;#Apop
        VxA[54-1]=Vc;#Apop_C3
        VxA[55-1]=Vc;#Smac
        VxA[56-1]=Vc;#Apop_XIAP
        VxA[57-1]=Vc;#Smac_XIAP
        VxA[58-1]=Vc;#C3_Ub
        VxA[59-1]=Vc;#BAD
        VxA[60-1]=Vc;#PUMA
        VxA[61-1]=Vc;#NOXA
        VxA[62-1]=Vc;#Bcl2c_BAD
        VxA[63-1]=Vc;#Bcl2c_PUMA
        VxA[64-1]=Vc;#Bcl2c_NOXA
        VxA[65-1]=Vc;#BIM
        VxA[66-1]=Vc;#BIM_Bax
        VxA[67-1]=Vc;#Bcl2_BIM
        VxA[68-1]=Vc;#ppERK_BIM
        VxA[69-1]=Vc;#pBIM
        VxA[70-1]=Vc;#ppAKT_BAD
        VxA[71-1]=Vc;#pBAD
        VxA[72-1]=Vc;#ppERK_BAD


        # VxR
        VxR = np.zeros(shape=(73))

        VxR[0:73]=Vc;
        VxR[0:7]=Ve; #ligands

        # VxRP
        VxRP = np.zeros(shape=(414))
        VxRP[0:414]=Vc;





        # VxP
        VxP = np.zeros(shape=(130))

        VxP[1-1]=Vc;#IRS
        VxP[2-1]=Vc;#Sp
        VxP[3-1]=Vc;#Cbl
        VxP[4-1]=Vc;#G2
        VxP[5-1]=Vc;#G2_SOS
        VxP[6-1]=Vc;#G2_pSOS
        VxP[7-1]=Vc;#PLCg
        VxP[8-1]=Vc;#PI3KC1
        VxP[9-1]=Vc;#PI3KR1
        VxP[10-1]=Vc;#PI3K1
        VxP[11-1]=Vc;#pPI3K1
        VxP[12-1]=Vc;#PI3K2
        VxP[13-1]=Vc;#mTORC1
        VxP[14-1]=Vc;#mTORC1active
        VxP[15-1]=Vc;#PIP
        VxP[16-1]=Vc;#PI3P
        VxP[17-1]=Vc;#DAG
        VxP[18-1]=Vc;#GRP
        VxP[19-1]=Vc;#DAG_GRP
        VxP[20-1]=Vc;#RasT
        VxP[21-1]=Vc;#RasD
        VxP[22-1]=Vc;#NF1
        VxP[23-1]=Vc;#pNF1
        VxP[24-1]=Vc;#pCRaf
        VxP[25-1]=Vc;#CRaf
        VxP[26-1]=Vc;#RasT_CRaf
        VxP[27-1]=Vc;#BRaf
        VxP[28-1]=Vc;#RasT_CRaf_BRaf
        VxP[29-1]=Vc;#MEK
        VxP[30-1]=Vc;#pMEK
        VxP[31-1]=Vc;#ppMEK
        VxP[32-1]=Vc;#MKP3
        VxP[33-1]=Vn;#ERKnuc
        VxP[34-1]=Vn;#ppERKnuc
        VxP[35-1]=Vc;#RSK
        VxP[36-1]=Vc;#pRSK
        VxP[37-1]=Vn;#pRSKnuc
        VxP[38-1]=Vn;#MKP1
        VxP[39-1]=Vn;#pMKP1
        VxP[40-1]=Vn;#cFos
        VxP[41-1]=Vn;#pcFos
        VxP[42-1]=Vn;#cJun
        VxP[43-1]=Vn;#pcFos_cJun
        VxP[44-1]=Vn;#cMyc
        VxP[45-1]=Vn;#bCATENINnuc
        VxP[46-1]=Vc;#bCATENIN
        VxP[47-1]=Vc;#pbCATENIN
        VxP[48-1]=Vc;#IP3
        VxP[49-1]=Vc;#PIP2
        VxP[50-1]=Vc;#PIP3
        VxP[51-1]=Vc;#PTEN
        VxP[52-1]=Vc;#PIP3_AKT
        VxP[53-1]=Vc;#AKT
        VxP[54-1]=Vc;#pAKT
        VxP[55-1]=Vc;#ppAKT
        VxP[56-1]=Vc;#PDK1
        VxP[57-1]=Vc;#PIP3_PDK1
        VxP[58-1]=Vc;#PIP3_pAKT
        VxP[59-1]=Vc;#Rictor
        VxP[60-1]=Vc;#mTOR
        VxP[61-1]=Vc;#mTORC2
        VxP[62-1]=Vc;#PIP3_ppAKT
        VxP[63-1]=Vc;#GSK3b
        VxP[64-1]=Vc;#pGSK3b
        VxP[65-1]=Vc;#TSC1
        VxP[66-1]=Vc;#TSC2
        VxP[67-1]=Vc;#pTSC2
        VxP[68-1]=Vc;#TSC
        VxP[69-1]=Vc;#PKC
        VxP[70-1]=Vc;#DAG_PKC
        VxP[71-1]=Vc;#pRKIP
        VxP[72-1]=Vc;#RKIP
        VxP[73-1]=Vc;#RKIP_CRaf
        VxP[74-1]=Vc;#ERK
        VxP[75-1]=Vc;#pERK
        VxP[76-1]=Vc;#ppERK
        VxP[77-1]=Vc;#FOXO
        VxP[78-1]=Vc;#pFOXO
        VxP[79-1]=Vc;#RhebD
        VxP[80-1]=Vc;#RhebT
        VxP[81-1]=Vc;#Raptor
        VxP[82-1]=Vc;#S6K
        VxP[83-1]=Vc;#pS6K
        VxP[84-1]=Vc;#EIF4EBP1
        VxP[85-1]=Vc;#pEIF4EBP1
        VxP[86-1]=Vc;#SOS
        VxP[87-1]=Vc;#G2_SOS_ppERK
        VxP[88-1]=Vc;#CRaf_ppERK
        VxP[89-1]=Vc;#RasD_DAG_GRP
        VxP[90-1]=Vc;#RasT_NF1
        VxP[91-1]=Vc;#NF1_ppERK
        VxP[92-1]=Vc;#MEK_RasT_CRaf_BRaf
        VxP[93-1]=Vc;#pMEK_RasT_CRaf_BRaf
        VxP[94-1]=Vc;#ERK_ppMEK
        VxP[95-1]=Vc;#pERK_ppMEK
        VxP[96-1]=Vc;#RSK_ppERK
        VxP[97-1]=Vn;#pRSKnuc_MPK1
        VxP[98-1]=Vn;#ppERKnuc_MPK1
        VxP[99-1]=Vn;#cFos_pRSKnuc
        VxP[100-1]=Vn;#cFos_ppERKnuc
        VxP[101-1]=Vc;#RKIP_DAG_PKC
        VxP[102-1]=Vc;#PIP3_PTEN
        VxP[103-1]=Vc;#PIP3_AKT_PIP3_PDK1
        VxP[104-1]=Vc;#PIP3_pAKT_mTORC2
        VxP[105-1]=Vc;#GSK3b_ppAKT
        VxP[106-1]=Vc;#bCATENIN_GSK3b
        VxP[107-1]=Vc;#TSC2_ppAKT
        VxP[108-1]=Vc;#TSC2_ppERK
        VxP[109-1]=Vc;#RhebT_TSC
        VxP[110-1]=Vc;#EIF4EBP1_mTORC1active
        VxP[111-1]=Vc;#S6K_mTORC1active
        VxP[112-1]=Vc;#FOXO_ppAKT
        VxP[113-1]=Vc;#PI3K1_mTORC1active
        VxP[114-1]=Vc;#pERK_MKP3
        VxP[115-1]=Vc;#ppERK_MKP3
        VxP[116-1]=Vc;#ppERKnuc_pMKP1
        VxP[117-1]=Vc;#RasT_BRaf
        VxP[118-1]=Vc;#RasT_BRaf_BRaf
        VxP[119-1]=Vc;# MEK_RasT_BRaf_BRaf
        VxP[120-1]=Vc;# pMEK_RasT_BRaf_BRaf
        VxP[121-1]=Vc;#EIF4E
        VxP[122-1]=Vc;#EIF4E_EIF4EBP1
        VxP[123-1]=Vc;
        VxP[124-1]=Vc;
        VxP[125-1]=Vc;
        VxP[126-1]=Vn;#FOXOnuc
        VxP[127-1:130]=Vc;




        # %% VxE
        VxE = np.zeros(shape=(2))
        VxE[0]=Vc;
        VxE[1]=Vc;



        # Vx
        # Vx=[VxRibosome;VxD';VxC';VxA';VxR';VxRP';VxP';VxE'];

        to_transpose = [VxD,VxC,VxA,VxR,VxRP,VxP,VxE]


        Vx = np.array([])

        Vx = np.append(Vx,VxRibosome)

        for item in to_transpose:
            Vx = np.append(Vx,item)

        Vx = np.matrix(Vx)

        Vx = np.matrix.transpose(Vx)






    if flagOUT[1]:
    # VvR
        VvbR=Vc;
        VvdR=Vc;

    # VvTL
        VvTL = np.zeros(shape=(numberofgenes))
        VvTL[0:numberofgenes]=Vc;


    # VvTLCd
        VvTLCd = np.zeros(shape=(102))
        VvTLCd[0:102]=Vc;
        VvTLCd[0:26]=Vn;
        VvTLCd[[38,39]]=Vm;
        VvTLCd[77:81]=Vn;


    # VvE
        VvE = np.zeros(shape=(5))
        VvE[0:5]=Vc;


    # VvD **
        VvD = np.zeros(shape=(66))

        VvD[1-1]=Vn;
        VvD[2-1]=Vn;
        VvD[3-1]=Vn;
        VvD[4-1]=Vn;
        VvD[5-1]=Vn;
        VvD[6-1]=Vn;
        VvD[7-1]=Vn;
        VvD[8-1]=Vn;
        VvD[9-1]=Vn;
        VvD[10-1]=Vn;
        VvD[11-1]=Vn;
        VvD[12-1]=Vn;
        VvD[13-1]=Vn;
        VvD[14-1]=Vn;
        VvD[15-1]=Vn;
        VvD[16-1]=Vn;
        VvD[17-1]=Vn;
        VvD[18-1]=Vn;
        VvD[19-1]=Vn;
        VvD[20-1]=Vn;
        VvD[21-1]=Vn;
        VvD[22-1]=Vn;
        VvD[23-1]=Vn;
        VvD[24-1]=Vn;
        VvD[25-1]=Vn;
        VvD[26-1]=Vn;
        VvD[27-1]=Vn;
        VvD[28-1]=Vn;
        VvD[29-1]=Vn;
        VvD[30-1]=Vn;
        VvD[31-1]=Vn;
        VvD[32-1]=Vn;
        VvD[33-1]=Vn;
        VvD[34-1]=Vn;
        VvD[35-1]=Vn;
        VvD[36-1]=Vn;
        VvD[37-1]=Vn;
        VvD[38-1]=Vn;
        VvD[39-1]=Vn;
        VvD[40-1]=Vn;
        VvD[41-1]=Vn;
        VvD[42-1]=Vn;
        VvD[43-1]=Vn;
        VvD[44-1]=Vn;
        VvD[45-1]=Vn;
        VvD[46-1]=Vn;
        VvD[47-1]=Vn;
        VvD[48-1]=Vn;
        VvD[49-1]=Vn;
        VvD[50-1]=Vn;
        VvD[51-1]=Vn;
        VvD[52-1]=Vn;
        VvD[53-1]=Vn;
        VvD[54-1]=Vn;
        VvD[55-1]=Vn;
        VvD[56-1]=Vn;
        VvD[57-1]=Vn;
        VvD[58-1]=Vn;
        VvD[59-1]=Vn;
        VvD[60-1]=Vn;
        VvD[61-1]=Vn;
        VvD[62-1]=Vn;
        VvD[63-1]=Vn;
        VvD[64-1]=Vn;
        VvD[65-1]=Vn;
        VvD[66-1]=Vn;



    # VvC **
        VvC = np.zeros(shape=(104))
        VvC[1-1]=Vn;
        VvC[2-1]=Vn;
        VvC[3-1]=Vn;
        VvC[4-1]=Vn;
        VvC[5-1]=Vn;
        VvC[6-1]=Vn;
        VvC[7-1]=Vn;
        VvC[8-1]=Vn;
        VvC[9-1]=Vn;
        VvC[10-1]=Vn;
        VvC[11-1]=Vn;
        VvC[12-1]=Vn;
        VvC[13-1]=Vn;
        VvC[14-1]=Vn;
        VvC[15-1]=Vn;
        VvC[16-1]=Vn;
        VvC[17-1]=Vn;
        VvC[18-1]=Vn;
        VvC[19-1]=Vn;
        VvC[20-1]=Vn;
        VvC[21-1]=Vn;
        VvC[22-1]=Vn;
        VvC[23-1]=Vn;
        VvC[24-1]=Vn;
        VvC[25-1]=Vn;
        VvC[26-1]=Vn;
        VvC[27-1]=Vn;
        VvC[28-1]=Vn;
        VvC[29-1]=Vn;
        VvC[30-1]=Vn;
        VvC[31-1]=Vn;
        VvC[32-1]=Vn;
        VvC[33-1]=Vn;
        VvC[34-1]=Vn;
        VvC[35-1]=Vn;
        VvC[36-1]=Vn;
        VvC[37-1]=Vn;
        VvC[38-1]=Vn;
        VvC[39-1]=Vn;
        VvC[40-1]=Vn;
        VvC[41-1]=Vn;
        VvC[42-1]=Vn;
        VvC[43-1]=Vn;
        VvC[44-1]=Vn;
        VvC[45-1]=Vn;
        VvC[46-1]=Vn;
        VvC[47-1]=Vn;
        VvC[48-1]=Vn;
        VvC[49-1]=Vn;
        VvC[50-1]=Vn;
        VvC[51-1]=Vn;
        VvC[52-1]=Vn;
        VvC[53-1]=Vn;
        VvC[54-1]=Vn;
        VvC[55-1]=Vn;
        VvC[56-1]=Vn;
        VvC[57-1]=Vn;
        VvC[58-1]=Vn;
        VvC[59-1]=Vn;
        VvC[60-1]=Vn;
        VvC[61-1]=Vn;
        VvC[62-1]=Vn;
        VvC[63-1]=Vn;
        VvC[64-1]=Vn;
        VvC[65-1]=Vn;
        VvC[66-1]=Vn;
        VvC[67-1]=Vn;
        VvC[68-1]=Vn;
        VvC[69-1]=Vn;
        VvC[70-1]=Vn;
        VvC[71-1]=Vn;
        VvC[72-1]=Vn;
        VvC[73-1]=Vn;
        VvC[74-1]=Vn;
        VvC[75-1]=Vn;
        VvC[76-1]=Vn;
        VvC[77-1]=Vn;
        VvC[78-1]=Vn;
        VvC[79-1]=Vn;
        VvC[80-1]=Vn;
        VvC[81-1]=Vn;
        VvC[82-1]=Vn;
        VvC[83-1]=Vn;
        VvC[84-1]=Vn;
        VvC[85-1]=Vn;
        VvC[86-1]=Vn;
        VvC[87-1]=Vn;
        VvC[88-1]=Vn;
        VvC[89-1]=Vn;
        VvC[90-1]=Vn;
        VvC[91-1]=Vn;
        VvC[92-1]=Vn;
        VvC[93-1]=Vn;
        VvC[94-1]=Vn;
        VvC[95-1]=Vn;
        VvC[96-1]=Vn;
        VvC[97-1]=Vn;
        VvC[98-1]=Vn;
        VvC[99-1]=Vn;
        VvC[100-1]=Vn;
        VvC[101-1]=Vn;
        VvC[102-1]=Vn;
        VvC[103-1]=Vn;
        VvC[104-1]=Vn;

    # VvA **
        VvA = np.zeros(shape=(87))

        VvA[1-1]=Ve;
        VvA[2-1]=Vc;
        VvA[3-1]=Vc;
        VvA[4-1]=Vc;
        VvA[5-1]=Vc;
        VvA[6-1]=Vc;
        VvA[7-1]=Vc;
        VvA[8-1]=Vc;
        VvA[9-1]=Vc;
        VvA[10-1]=Vc;
        VvA[11-1]=Vc;
        VvA[12-1]=Vc;
        VvA[13-1]=Vc;
        VvA[14-1]=Vc;
        VvA[15-1]=Vc;
        VvA[16-1]=Vc;
        VvA[17-1]=Vc;
        VvA[18-1]=Vc;
        VvA[19-1]=Vc;
        VvA[20-1]=Vc;
        VvA[21-1]=Vc;
        VvA[22-1]=Vc;
        VvA[23-1]=Vc;
        VvA[24-1]=Vc;
        VvA[25-1]=Vc;
        VvA[26-1]=Vc;
        VvA[27-1]=Vc;
        VvA[28-1]=Vc;
        VvA[29-1]=Vc;
        VvA[30-1]=Vc;
        VvA[31-1]=Vc;
        VvA[32-1]=Vc;
        VvA[33-1]=Vc;
        VvA[34-1]=Vc;
        VvA[35-1]=Vm;
        VvA[36-1]=Vm;
        VvA[37-1]=Vm;
        VvA[38-1]=Vm;
        VvA[39-1]=Vm;
        VvA[40-1]=Vm;
        VvA[41-1]=Vm;
        VvA[42-1]=Vm;
        VvA[43-1]=Vm;
        VvA[44-1]=Vm;
        VvA[45-1]=Vm;
        VvA[46-1]=Vm;
        VvA[47-1]=Vm;
        VvA[48-1]=Vm;
        VvA[49-1]=Vm;
        VvA[50-1]=Vm;
        VvA[51-1]=Vm;
        VvA[52-1]=Vm;
        VvA[53-1]=Vm;
        VvA[54-1]=Vm;
        VvA[55-1]=Vm;
        VvA[56-1]=Vc;
        VvA[57-1]=Vc;
        VvA[58-1]=Vc;
        VvA[59-1]=Vc;
        VvA[60-1]=Vc;
        VvA[61-1]=Vc;
        VvA[62-1]=Vc;
        VvA[63-1]=Vc;
        VvA[64-1]=Vc;
        VvA[65-1]=Vm;
        VvA[66-1]=Vc;
        VvA[67-1]=Vc;
        VvA[68-1]=Vc;
        VvA[69-1]=Vc;
        VvA[70-1]=Vc;
        VvA[71-1]=Vc;
        VvA[72-1]=Vc;
        VvA[73-1]=Vc;
        VvA[74-1]=Vc;
        VvA[75-1]=Vc;
        VvA[76-1]=Vc;
        VvA[77-1]=Vc;
        VvA[78-1]=Vc;
        VvA[79-1]=Vc;
        VvA[80-1]=Vc;
        VvA[81-1]=Vc;
        VvA[82-1]=Vm;
        VvA[83-1]=Vm;
        VvA[84-1]=Vm;
        VvA[85-1]=Vc;
        VvA[86-1]=Vm;
        VvA[87-1]=Vc;

    # VvR **
        VvR = np.zeros(shape=(158))




        VvR[0:158]=Vc;
        VvR[[1-1,7-1,13-1,21-1,25-1,31-1,35-1,43-1,47-1,53-1,57-1,63-1,73-1,77-1,81-1,87-1,92-1,123-1,125-1,127-1,129-1,131-1,133-1,135-1,137-1,139-1,141-1,151-1,153-1,155-1,157-1]]=Ve;
        # looks weird because used search and replace to subtract 1 to fix matlab indices



    # VvRP **
        td=29

        VvRP1 = np.zeros(shape=(td))
        VvRP1[0:td]=Vc;

        VvRP2 = np.zeros(shape=(td))
        VvRP2[0:td]=Vc;

        VvRP3 = np.zeros(shape=(td))
        VvRP3[0:td]=Vc;

        VvRP4 = np.zeros(shape=(td))
        VvRP4[0:td]=Vc;

        VvRP5 = np.zeros(shape=(td))
        VvRP5[0:td]=Vc;

        VvRP6 = np.zeros(shape=(td))
        VvRP6[0:td]=Vc;

        VvRP7 = np.zeros(shape=(td))
        VvRP7[0:td]=Vc;

        VvRP8 = np.zeros(shape=(td))
        VvRP8[0:td]=Vc;

        VvRP9 = np.zeros(shape=(td))
        VvRP9[0:td]=Vc;

        VvRP10 = np.zeros(shape=(td))
        VvRP10[0:td]=Vc;

        VvRP11 = np.zeros(shape=(td))
        VvRP11[0:td]=Vc;

        VvRP12 = np.zeros(shape=(td))
        VvRP12[0:td]=Vc;

        VvRP13 = np.zeros(shape=(td))
        VvRP13[0:td]=Vc;

        VvRP14 = np.zeros(shape=(td))
        VvRP14[0:td]=Vc;

        VvRP15 = np.zeros(shape=(td))
        VvRP15[0:td]=Vc;

        VvRP16 = np.zeros(shape=(td))
        VvRP16[0:td]=Vc;

        VvRP17 = np.zeros(shape=(td))
        VvRP17[0:td]=Vc;

        VvRP18 = np.zeros(shape=(td))
        VvRP18[0:td]=Vc;

        VvRP19 = np.zeros(shape=(td))
        VvRP19[0:td]=Vc;

        VvRP20 = np.zeros(shape=(td))
        VvRP20[0:td]=Vc;

        VvRP21 = np.zeros(shape=(td))
        VvRP21[0:td]=Vc;

        VvRP22 = np.zeros(shape=(td))
        VvRP22[0:td]=Vc;

        VvRP23 = np.zeros(shape=(td))
        VvRP23[0:td]=Vc;

        VvRP24 = np.zeros(shape=(td))
        VvRP24[0:td]=Vc;

        VvRP25 = np.zeros(shape=(td))
        VvRP25[0:td]=Vc;

        VvRP26 = np.zeros(shape=(td))
        VvRP26[0:td]=Vc;

        VvRP27 = np.zeros(shape=(td))
        VvRP27[0:td]=Vc;

        VvRP28 = np.zeros(shape=(td))
        VvRP28[0:td]=Vc;

        VvRP29 = np.zeros(shape=(td))
        VvRP29[0:td]=Vc;

        VvRP30 = np.zeros(shape=(td))
        VvRP30[0:td]=Vc;

        VvRP31 = np.zeros(shape=(td))
        VvRP31[0:td]=Vc;

        VvRP32 = np.zeros(shape=(td))
        VvRP32[0:td]=Vc;

        VvRP33 = np.zeros(shape=(td))
        VvRP33[0:td]=Vc;

        VvRP34 = np.zeros(shape=(16))
        VvRP34[0:16]=Vc;



    # VvP **
        VvP = np.zeros(shape=(190))

        VvP[1-1]=Vc;
        VvP[2-1]=Vc;
        VvP[3-1]=Vc;
        VvP[4-1]=Vc;
        VvP[5-1]=Vc;
        VvP[6-1]=Vc;
        VvP[7-1]=Vc;
        VvP[8-1]=Vc;
        VvP[9-1]=Vc;
        VvP[10-1]=Vc;
        VvP[11-1]=Vc;
        VvP[12-1]=Vc;
        VvP[13-1]=Vc;
        VvP[14-1]=Vc;
        VvP[15-1]=Vc;
        VvP[16-1]=Vc;
        VvP[17-1]=Vc;
        VvP[18-1]=Vc;
        VvP[19-1]=Vc;
        VvP[20-1]=Vc;
        VvP[21-1]=Vc;
        VvP[22-1]=Vc;
        VvP[23-1]=Vc;
        VvP[24-1]=Vc;
        VvP[25-1]=Vc;
        VvP[26-1]=Vc;
        VvP[27-1]=Vc;
        VvP[28-1]=Vc;
        VvP[29-1]=Vc;
        VvP[30-1]=Vc;
        VvP[31-1]=Vc;
        VvP[32-1]=Vc;
        VvP[33-1]=Vc;
        VvP[34-1]=Vc;
        VvP[35-1]=Vc;
        VvP[36-1]=Vc;
        VvP[37-1]=Vc;
        VvP[38-1]=Vc;
        VvP[39-1]=Vn;
        VvP[40-1]=Vn;
        VvP[41-1]=Vn;
        VvP[42-1]=Vn;
        VvP[43-1]=Vn;
        VvP[44-1]=Vc;
        VvP[45-1]=Vn;
        VvP[46-1]=Vc;
        VvP[47-1]=Vc;
        VvP[48-1]=Vc;
        VvP[49-1]=Vc;
        VvP[50-1]=Vc;
        VvP[51-1]=Vc;
        VvP[52-1]=Vc;
        VvP[53-1]=Vc;
        VvP[54-1]=Vc;
        VvP[55-1]=Vc;
        VvP[56-1]=Vc;
        VvP[57-1]=Vc;
        VvP[58-1]=Vc;
        VvP[59-1]=Vc;
        VvP[60-1]=Vc;
        VvP[61-1]=Vc;
        VvP[62-1]=Vc;
        VvP[63-1]=Vc;
        VvP[64-1]=Vc;
        VvP[65-1]=Vc;
        VvP[66-1]=Vc;
        VvP[67-1]=Vc;
        VvP[68-1]=Vc;
        VvP[69-1]=Vc;
        VvP[70-1]=Vc;
        VvP[71-1]=Vc;
        VvP[72-1]=Vc;
        VvP[73-1]=Vc;
        VvP[74-1]=Vc;
        VvP[75-1]=Vn;
        VvP[76-1]=Vn;
        VvP[77-1]=Vn;
        VvP[78-1]=Vn;
        VvP[79-1]=Vn;
        VvP[80-1]=Vc;
        VvP[81-1]=Vn;
        VvP[82-1]=Vn;
        VvP[83-1]=Vn;
        VvP[84-1]=Vn;
        VvP[85-1]=Vn;
        VvP[86-1]=Vn;
        VvP[87-1]=Vn;
        VvP[88-1]=Vn;
        VvP[89-1]=Vn;
        VvP[90-1]=Vn;
        VvP[91-1]=Vn;
        VvP[92-1]=Vn;
        VvP[93-1]=Vn;
        VvP[94-1]=Vn;
        VvP[95-1]=Vc;
        VvP[96-1]=Vc;
        VvP[97-1]=Vc;
        VvP[98-1]=Vc;
        VvP[99-1]=Vc;
        VvP[100-1]=Vc;
        VvP[101-1]=Vc;
        VvP[102-1]=Vc;
        VvP[103-1]=Vc;
        VvP[104-1]=Vc;
        VvP[105-1]=Vc;
        VvP[106-1]=Vc;
        VvP[107-1]=Vc;
        VvP[108-1]=Vc;
        VvP[109-1]=Vc;
        VvP[110-1]=Vc;
        VvP[111-1]=Vc;
        VvP[112-1]=Vc;
        VvP[113-1]=Vc;
        VvP[114-1]=Vc;
        VvP[115-1]=Vc;
        VvP[116-1]=Vc;
        VvP[117-1]=Vc;
        VvP[118-1]=Vc;
        VvP[119-1]=Vc;
        VvP[120-1]=Vc;
        VvP[121-1]=Vc;
        VvP[122-1]=Vc;
        VvP[123-1]=Vc;
        VvP[124-1]=Vc;
        VvP[125-1]=Vc;
        VvP[126-1]=Vc;
        VvP[127-1]=Vc;
        VvP[128-1]=Vc;
        VvP[129-1]=Vc;
        VvP[130-1]=Vc;
        VvP[131-1]=Vc;
        VvP[132-1]=Vc;
        VvP[133-1]=Vn;
        VvP[134-1]=Vc;
        VvP[135-1]=Vc;
        VvP[136-1]=Vc;
        VvP[137-1]=Vc;
        VvP[138-1]=Vc;
        VvP[139-1]=Vc;
        VvP[140-1]=Vc;
        VvP[141-1]=Vc;
        VvP[142-1]=Vc;
        VvP[143-1]=Vc;
        VvP[144-1]=Vc;
        VvP[145-1]=Vc;
        VvP[146-1]=Vc;
        VvP[147-1]=Vc;
        VvP[148-1]=Vc;
        VvP[149-1]=Vc;
        VvP[150-1]=Vc;
        VvP[151-1]=Vc;
        VvP[152-1]=Vc;
        VvP[153-1]=Vc;
        VvP[154-1]=Vc;
        VvP[155-1]=Vc;
        VvP[156-1]=Vc;
        VvP[157-1]=Vc;
        VvP[158-1]=Vc;
        VvP[159-1]=Vc;
        VvP[160-1]=Vc;
        VvP[161-1]=Vc;
        VvP[162-1]=Vc;
        VvP[163-1]=Vc;
        VvP[164-1]=Vc;
        VvP[165-1]=Vc;
        VvP[166-1]=Vc;
        VvP[167-1]=Vc;
        VvP[168-1]=Vc;
        VvP[169-1]=Vc;
        VvP[170-1]=Vc;
        VvP[171-1]=Vc;
        VvP[172-1]=Vc;
        VvP[173-1]=Vc;
        VvP[174-1]=Vc;
        VvP[175-1]=Vc;
        VvP[176-1]=Vc;
        VvP[177-1]=Vn;
        VvP[178-1]=Vc;
        VvP[179-1]=Vc;
        VvP[180-1]=Vc;
        VvP[181-1]=Vc;
        VvP[182-1]=Vn;
        VvP[183-1]=Vc;
        VvP[184-1]=Vc;
        VvP[185-1]=Vc;
        VvP[186-1]=Vc;
        VvP[187-1:190]=Vc;


    # VvDA **
    # NONE as these are all transcriptional control mechanisms.
    # VvDP **
        VvDP = np.zeros(shape=(4))

        VvDP[0]=Vc;
        VvDP[1]=Vc;
        VvDP[2]=Vc;
        VvDP[3]=Vc;


    # VvPA **
        VvPA = np.zeros(shape=(11))

        VvPA[1-1]=Vc;
        VvPA[2-1]=Vc;
        VvPA[3-1]=Vc;
        VvPA[4-1]=Vc;
        VvPA[5-1]=Vc;
        VvPA[6-1]=Vc;
        VvPA[7-1]=Vc;
        VvPA[8-1]=Vc;
        VvPA[9-1]=Vc;
        VvPA[10-1]=Vc;
        VvPA[11-1]=Vc



    # VvPC **
    # NONE as these are all transcriptional control mechanisms.
    #
    # VvDC **
    # NONE as these are all transcriptional control mechanisms.





    # %%%%%%% DEGRADATION
    # still within if statement
        S_dtemp=S_d;


        S_dtemp[S_d==1] = 0
        S_dtemp = S_dtemp.astype(bool).astype(int)
        VvXd = np.matrix.transpose(S_dtemp)*Vx




        # Transpose and Concatenate
        VvRP=[VvRP1,VvRP2,VvRP3,VvRP4,VvRP5,VvRP6,VvRP7,VvRP8,VvRP9,VvRP10,VvRP11,VvRP12,VvRP13,VvRP14,VvRP15,VvRP16,VvRP17,VvRP18,VvRP19,VvRP20,VvRP21,VvRP22,VvRP23,VvRP24,VvRP25,VvRP26,VvRP27,VvRP28,VvRP29,VvRP30,VvRP31,VvRP32,VvRP33,VvRP34];

        # Vv=[VvbR;VvdR;VvTL';VvTLCd';VvE';VvD';VvC';VvA';VvR';VvRP';VvP';VvDP';VvPA';VvXd];

        Vv = np.array([])

        Vv = np.append(Vv,VvbR)
        Vv = np.append(Vv,VvdR)
        Vv = np.append(Vv,VvTL)
        Vv = np.append(Vv,VvTLCd)
        Vv = np.append(Vv,VvE)
        Vv = np.append(Vv,VvD)
        Vv = np.append(Vv,VvC)
        Vv = np.append(Vv,VvA)
        Vv = np.append(Vv,VvR)
        Vv = np.append(Vv,VvRP)
        Vv = np.append(Vv,VvP)
        Vv = np.append(Vv,VvDP)
        Vv = np.append(Vv,VvPA)
        Vv = np.append(Vv,np.matrix.transpose(VvXd))



        # to_measure = [VvbR,VvdR,VvTL,VvTLCd,VvE,VvD,VvC,VvA,VvR,VvRP1,VvRP2,VvRP3,VvRP4,VvRP5,VvRP6,VvRP7,VvRP8,VvRP9,VvRP10,VvRP11,VvRP12,VvRP13,VvRP14,VvRP15,VvRP16,VvRP17,VvRP18,VvRP19,VvRP20,VvRP21,VvRP22,VvRP23,VvRP24,VvRP25,VvRP26,VvRP27,VvRP28,VvRP29,VvRP30,VvRP31,VvRP32,VvRP33,VvRP34,VvP,VvDP,VvPA,VvXd]




        real_Vv = np.array([])
        for item in Vv:
            if type(item) == float:
                real_Vv = np.append(real_Vv,item)
            else:
                for element in item:
                    real_Vv = np.append(real_Vv,element)


        real_Vv = np.matrix(real_Vv)

        real_Vv = np.matrix.transpose(real_Vv)






    return [Vx,real_Vv,VxTL]
