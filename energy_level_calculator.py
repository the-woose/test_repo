import numpy as np
import scipy
from scipy import constants as spc
#-------------------------constants--------------------------------#
h = spc.h; L = 0.2e-9; e_mass = spc.electron_mass; n = 0
#-------------------------loop calculation-------------------------#
while True:
    En = (h**2)*(n**2)/(8*(e_mass**2)*(L**2))
    # ----str() converts numbers to string----#
    print("n = " + str(n) + " => Energy = " + str(En))
    n += 1  # ----if reaches target, break----#
    if En > 1e+15:
        break