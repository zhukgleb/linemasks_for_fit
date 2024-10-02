import numpy as np


dech_lin_name = "rework_a_com.lin"
mask_name = "fe-lmask_VG.txt"
data_lin = np.genfromtxt(dech_lin_name, delimiter=[11], dtype=float)

double_hwhm = 0.4
left_wing = [data_lin[x] - double_hwhm for x in range(len(data_lin))]
right_wing = [data_lin[x] + double_hwhm for x in range(len(data_lin))]

np.savetxt(mask_name, np.column_stack((left_wing, data_lin, right_wing)))