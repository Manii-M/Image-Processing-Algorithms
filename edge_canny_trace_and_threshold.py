import numpy as np

def trace_and_threshold(E_nms, E_bin, i, j, t_low):
    E_bin[i,j] = 255
    
    jL = np.max([j-1, 0])
    jR = np.min([j+1, E_bin.shape[1]])
    
    iT = np.max([i-1, 0])
    iB = np.min([i+1, E_bin.shape[0]])
    
    for ii in np.arange(iT, iB):
        for jj in np.arange(jL, jR):
            if E_nms[ii,jj] >= t_low and E_bin[ii,jj] == 0:
                trace_and_threshold(E_nms, E_bin, ii, jj, t_low)
                
    return