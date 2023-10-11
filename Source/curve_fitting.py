from libraries import *

def growth_function(t, tau_STHSC, tau_MPP, tau_CLP, tau_CMP,
                    tau_GMP, tau_MEP, tau_ProB, tau_Bcell,
                    tau_DNT, tau_DPT, tau_CD4T, tau_CD8T):

    num_params = len(locals()) - 1

    def system_of_odes(F, t):
        STHSC, MPP, CLP, CMP, GMP, MEP, ProB, Bcell, DNT, DPT, CD4T, CD8T = F   # data at time t

        dSTHSC_dt = 1 / tau_STHSC * (1 - STHSC)     # LT-HSC --> ST-HSC
        dMPP_dt = 1 / tau_MPP * (STHSC - MPP)       # ST-HSC --> MPP
        dCLP_dt = 1 / tau_CLP * (MPP - CLP)         # MPP    --> CLP
        dCMP_dt = 1 / tau_CMP * (MPP - CMP)         # MPP    --> CMP
        dGMP_dt = 1 / tau_GMP * (CMP - GMP)         # CMP    --> GMP
        dMEP_dt = 1 / tau_MEP * (CMP - MEP)         # CMP    --> MEP
        dProB_dt = 1 / tau_ProB * (CLP - ProB)      # CLP    --> ProB
        dBcell_dt = 1 / tau_Bcell * (ProB - Bcell)  # ProB   --> B cells
        dDNT_dt = 1 / tau_DNT * (CLP - DNT)         # CLP    --> DNT
        dDPT_dt = 1 / tau_DPT * (DNT - DPT)         # DNT    --> DPT
        dCD4T_dt = 1 / tau_CD4T * (DPT - CD4T)      # DPT    --> CD4+T
        dCD8T_dt = 1 / tau_CD8T * (DPT - CD8T)      # DPT    --> CD8+T

        return [dSTHSC_dt, dMPP_dt, dCLP_dt, dCMP_dt,
                dGMP_dt, dMEP_dt, dProB_dt, dBcell_dt,
                dDNT_dt, dDPT_dt, dCD4T_dt, dCD8T_dt]   # numerical derivatives at time t

    F0 = [0] * num_params # f(0) = 0 for f in [STHSC, MPP, ... , CD8+T]
    F_sol = odeint(system_of_odes, F0, t)

    return F_sol.T.flatten()