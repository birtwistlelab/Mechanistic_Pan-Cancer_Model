# calc volume params


def CalcVolumeParams(VolumeofCell_IN):

    Vn=VolumeofCell_IN/4
    Vc=VolumeofCell_IN-Vn
    Vm=Vc*0.07

    mpc2nmcf_Vc=1E9/(Vc*6.023E+23)
    mpc2nmcf_Vn=1E9/(Vn*6.023E+23)
    mpc2nmcf_Vm=1E9/(Vm*6.023E+23)

    return(Vn,Vc,Vm,mpc2nmcf_Vc,mpc2nmcf_Vm,mpc2nmcf_Vn)
