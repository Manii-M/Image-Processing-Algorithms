def is_local_max(E_mag, i, j, s_theta, t_low):
    mC = E_mag[i,j]
    if mC < t_low:
        return False
    else:
        mL = -1
        if s_theta == 0:
            mL = E_mag[i, j-1]
        elif s_theta == 1:
            mL = E_mag[i-1, j-1]
        elif s_theta == 2:
            mL = E_mag[i-1, j]
        elif s_theta == 3:
            mL = E_mag[i-1, j+1]        
        
        mR = -1
        if s_theta == 0:
            mL = E_mag[i, j+1]
        elif s_theta == 1:
            mL = E_mag[i+1, j+1]
        elif s_theta == 2:
            mL = E_mag[i+1, j]
        elif s_theta == 3:
            mL = E_mag[i+1, j-1]
        
    return mL <= mC and mC >= mR