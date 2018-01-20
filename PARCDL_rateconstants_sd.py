import math
import csv
import numpy as np
import sys



def PARCDL_rateconstants_sd(ke50,mExp_mpc,kTLnat,kTLd,EIF4Efree,S_TL,S_d):


    # returns kTLCd,kTL,kXd,xp_mpc

    data = []

    with open('observables_mat_18.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = ', '.join(row)
            x = x.split(',')
            data.append(x)

    data = data[1:]

    data2 = []
    for row in data:
        data2.append(row[2:103])


    ObsMat = np.matrix(data2)



    xpi = []
    for x in kTLnat:
        try:
            xpi.append(x * mExp_mpc / kTLd)
        except:
            xpi.append(0)



    # this is how you remove nans from matrix!!!!!! remember this syntax!!!
    for i in range(len(xpi)):
        xpi[i][np.isnan(xpi[i])] = 0
        xpi[i][np.isinf(xpi[i])] = 0


    # kTL **
    temp=1/((EIF4Efree/(ke50+EIF4Efree)));
    kTL = []
    for item in kTLnat:
        kTL.append(item*temp)


    xp_mpc = np.multiply(kTLnat,mExp_mpc)/kTLd


    xp_mpc[np.isnan(xp_mpc)] = 0
    xp_mpc[np.isinf(xp_mpc)] = 0



    # important - the setting dimension to 2 in matlab is the same as setting axis to 1 in numpy.... i think. sums by row instead of by column
    inds = np.nonzero(np.sum(S_TL,axis=1))[0]

    inds0 = np.matrix.transpose(inds)


    kTLCd = []


    for i in range(len(inds)):

        genes2include = np.nonzero(S_TL[inds0[i],:])

        genes2include = genes2include[1]

        kTLCd.append(sum(np.multiply(kTLd[genes2include],(xp_mpc[genes2include]/sum(xp_mpc[genes2include]))))) #Sum of the fraction of each gene


    kTLCd = np.matrix(kTLCd)

    kTLCd[np.isnan(kTLCd)]=0
    kTLCd = np.matrix.transpose(kTLCd)



    kXd = []

    for i in range(S_d.shape[1]):
        ProtInd = np.nonzero(S_d[:,i]==-1)

        tmp = []
        for j in range(ObsMat[ProtInd,:][0].shape[1]):
            tmp.append(int((ObsMat[ProtInd,:][0][0,j])))


        Obs2Include = np.nonzero(tmp)


        # this takes care of a weird off-by-1 error i was getting for all i>=37. no idea why there was an error, but this fixes it
        if i >= 37:
            Obs2Include = Obs2Include[0] + 1


        # starting at i = 37, Obs2Include is off by 1 beginning at that point

        if i < 37:
            if Obs2Include:
                # important syntax here! use for all matrix - array problems!!!
                try:
                    kXd.append(max(np.squeeze(np.asarray(kTLCd[Obs2Include]))))
                except:
                    try:
                        kXd.append(kTLCd[Obs2Include][0,0])
                    except:
                        kXd.append(0)
            else:
                kXd.append(0)


        else:
            if Obs2Include.any():
                try:
                    kXd.append(max(np.squeeze(np.asarray(kTLCd[Obs2Include]))))
                except Exception as exc:
                    try:
                        kXd.append(kTLCd[Obs2Include][0,0])
                    except:
                        kXd.append(0)
            else:
                kXd.append(0)




    # decrease all beginning indices by 1 because matlab
    # leave end indices because they're included in matlab but not in python
    a=0;
    kAd=kXd[a:a+47];a=a+47;
    kRd=kXd[a:a+56];a=a+56;
    kRPd1=kXd[a:a+33];a=a+33;
    kRPd2=kXd[a:a+29];a=a+29;
    kRPd3=kXd[a:a+29];a=a+29;
    kRPd4=kXd[a:a+33];a=a+33;
    kRPd5=kXd[a:a+29];a=a+29;
    kRPd6=kXd[a:a+29];a=a+29;
    kRPd7=kXd[a:a+29];a=a+29;
    kRPd8=kXd[a:a+29];a=a+29;
    kRPd9=kXd[a:a+29];a=a+29;
    kRPd10=kXd[a:a+29];a=a+29;
    kRPd11=kXd[a:a+29];a=a+29;
    kRPd12=kXd[a:a+29];a=a+29;
    kRPd13=kXd[a:a+29];a=a+29;
    kRPd14=kXd[a:a+29];a=a+29;


    kPd=kXd[a:a+89];






    # Rate constant modified for internalized receptors
    kRPd3 = np.array(kRPd3)
    kRPd3[2:4]=8.3711E-4;
    kRPd3[[0,1,4,5,6,7,10,15]]=2.1301E-4;
    kRPd3[[8,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28]]=8.7106E-5;

    kRPd4 = np.array(kRPd4)
    kRPd4[2:4]=8.3711E-4; kRPd4[[0,1,4,5,6,7,10,15]]=2.1301E-4; kRPd4[[8,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]]=8.7106E-5;

    kRPd6 = np.array(kRPd6)
    kRPd6[2:4]=8.3711E-4; kRPd6[[0,1,4,5,6,7,10,15]]=2.1301E-4; kRPd6[[8,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28]]=8.7106E-5;

    kRPd10 = np.array(kRPd10)
    kRPd10[2:4]=8.3711E-4; kRPd10[[0,1,4,5,6,7,10,15]]=2.1301E-4; kRPd10[[8,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28]]=8.7106E-5;


    kPd = np.array(kPd)


    # Rate constants modified for degradation of lipids
    kPd[6]=0.00001; #PIP
    kPd[7]=0.00001; #PI3P
    kPd[8]=0.00108*10; #DAG
    kPd[26]=0.081; #IP3
    kPd[27]=4.83E-5; #PIP2
    kPd[28]=4.83E-5; #PIP3


    # Other rate constant modifications
    kPd[21:24] = math.log(2)/4/3600; #pMPK1 (DUSP), pcFos, pcFos_cJun



    # kXd=[kAd';kRd';kRPd1';kRPd2';kRPd3';kRPd4';kRPd5';kRPd6';kRPd7';kRPd8';kRPd9';kRPd10';kRPd11';kRPd12';kRPd13';kRPd14';kPd'];
    to_transpose=[kAd,kRd,kRPd1,kRPd2,kRPd3,kRPd4,kRPd5,kRPd6,kRPd7,kRPd8,kRPd9,kRPd10,kRPd11,kRPd12,kRPd13,kRPd14,kPd];

    giant_array = np.array([])

    for item in to_transpose:
        giant_array = np.append(giant_array,item)


    kXd = np.matrix(giant_array)

    kXd = np.matrix.transpose(kXd)

    # need to cast some lists into arrays here before returning




    return np.array(kTLCd),np.array(kTL),kXd,xp_mpc
