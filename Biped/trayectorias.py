import numpy as np
#import matplotlib.pyplot as plt
#from numba import jit


from InversekinematicBiped_0 import InversekinematicBiped_0
from directkinematicBiped_0 import directkinematicBiped_0

from InversekinematicBiped_1 import InversekinematicBiped_1
from directkinematicBiped_1 import directkinematicBiped_1

from InversekinematicBiped_2 import InversekinematicBiped_2
from directkinematicBiped_2 import directkinematicBiped_2


# Se considera Curva Spline Cúbica.
# Las Medidas están metros.
# Datos del Robot Bípedo
# hc = elevacion de la cadera
Lp = 0.020  # Lp = Longitud de paso
h = 0.23678  # h = altura de la cadera
hp = 0.010  # hp = elevacion de la pierna flotante.
hc = 0.005  # hc = elevacion de la cadera
Tp = 1  # Tp = tiempo empleado para cado paso

# ----------------------------------------------------------------
# CADERA.
# ----------------------------------------------------------------
# Eje "Z".
z0 = -Lp / 2
z1 = Lp / 2
v0 = 0
v1 = 0
Ti = Tp
t = np.linspace(0, Tp, 101) # np.arange(0, 1.01, 0.01) 
zc_PS = z0 + v0 * t + ((3 * (z1 - z0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t ** 2 + (
            (2 * (z0 - z1) + Ti * (v0 + v1)) / Ti ** 3) * t ** 3

# ----------------------------------------------------------------
# Eje "X":
# i)
x0 = h
x1 = h + hc
v0 = 0
v1 = 0
Ti = Tp / 2
t1 = np.linspace(0, Tp / 2, 51)
xc1_PS = x0 + v0 * t1 + ((3 * (x1 - x0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t1 ** 2 + (
            (2 * (x0 - x1) + Ti * (v0 + v1)) / Ti ** 3) * t1 ** 3
# ii)
x0 = h + hc
x1 = h
v0 = 0
v1 = 0
t2 = np.linspace(0, Tp / 2, 51)
xc2_PS = x0 + v0 * t2 + ((3 * (x1 - x0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t2 ** 2 + (
            (2 * (x0 - x1) + Ti * (v0 + v1)) / Ti ** 3) * t2 ** 3
xc_ps = np.concatenate((xc1_PS, xc2_PS[1:]))

# ----------------------------------------------------------------
# Eje "Y":
# PLANO FRONTAL
lc = 0.0452  # longitud del centro a unos de los extremos de la cadera.
dc = -0.035  # Sobre paso del punto central de la cadera sobre el eje "Y".
dp = 0.080  # distancia entre los pies.
vyc = 0  # Velocidad de la cadera al Inicio y final del Intervalo.
# i)
y0 = -lc
y1 = dc
v0 = vyc
v1 = 0
Ti = Tp / 2
t1 = np.linspace(0, Tp / 2, 51)
yc1_PF = y0 + v0 * t1 + ((3 * (y1 - y0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t1 ** 2 + (
            (2 * (y0 - y1) + Ti * (v0 + v1)) / Ti ** 3) * t1 ** 3

# ii)
y0 = dc
y1 = -lc
v0 = 0
v1 = -vyc
yc2_PF = y0 + v0 * t2 + ((3 * (y1 - y0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t2 ** 2 + (
            (2 * (y0 - y1) + Ti * (v0 + v1)) / Ti ** 3) * t2 ** 3
yc_pf = np.concatenate((yc1_PF, yc2_PF[1:]))

# ----------------------------------------------------------------
# PIERNA FLOTANTE.
# ----------------------------------------------------------------
# doble soporte.
# En el EJE "Z"
Tds = 0.3 * Tp
Tss = 0.7 * Tp
z0 = -Lp
z1 = Lp
v0 = 0
v1 = 0
Ti = Tss
t5 = np.linspace(0, Tss, 71)
zpf_Ps = z0 + v0 * t5 + ((3 * (z1 - z0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t5 ** 2 + (
            (2 * (z0 - z1) + Ti * (v0 + v1)) / Ti ** 3) * t5 ** 3

zpf_ps = np.zeros(101)
zpf_ps[:16] = -Lp
zpf_ps[16:87] = zpf_Ps
zpf_ps[87:] = Lp

# En el Eje "X"
x0 = 0
x1 = hp
v0 = 0
v1 = 0
Ti = Tss / 2
xpf_Ps = x0 + v0 * t1 + ((3 * (x1 - x0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t1 ** 2 + (
        (2 * (x0 - x1) + Ti * (v0 + v1)) / Ti ** 3) * t1 ** 3
x0 = hp
x1 = 0
xpf_Ps1 = x0 + v0 * t1 + ((3 * (x1 - x0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t1 ** 2 + (
        (2 * (x0 - x1) + Ti * (v0 + v1)) / Ti ** 3) * t1 ** 3

#print(xpf_Ps1)
xpf_ps = np.zeros(101)
# Asignar valores según las condiciones
for i in range(101):
    if i < 15:
        xpf_ps[i] = 0
    elif 15 <= i < 51:
        xpf_ps[i] = xpf_Ps[i - 15]
    elif 51 <= i < 86:
        xpf_ps[i] = xpf_Ps1[i - 51]
    else:
        xpf_ps[i] = 0



# En el Eje "Y"
y0 = -2 * lc
y1 = -dp
v0 = 0
v1 = 0
ypf1_PF = y0 + v0 * t1 + ((3 * (y1 - y0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t1 ** 2 + (
            (2 * (y0 - y1) + Ti * (v0 + v1)) / Ti ** 3) * t1 ** 3
y0 = -dp
y1 = -2 * lc
ypf2_PF = y0 + v0 * t1 + ((3 * (y1 - y0) - Ti * (2 * v0 + v1)) / Ti ** 2) * t1 ** 2 + (
            (2 * (y0 - y1) + Ti * (v0 + v1)) / Ti ** 3) * t1 ** 3

ypf_pf = np.zeros(101)
for i in range(101):
    if i < 16:
        ypf_pf[i] = -2 * lc
    elif 16 <= i < 51:
        ypf_pf[i] = ypf1_PF[i - 16]
    elif 51 <= i < 86:
        ypf_pf[i] = ypf2_PF[i - 51]
    else:
        ypf_pf[i] = -2 * lc



# Inicio de marcha
zc_start = 0 + v0 * t + ((3 * (Lp / 2 - 0) - Tp * (2 * v0 + v1)) / Tp ** 2) * t ** 2 + (
            (2 * (0 - Lp / 2) + Tp * (v0 + v1)) / Tp ** 3) * t ** 3

zpf_start = 0 + v0 * t + ((3 * (Lp - 0) - Tp * (2 * v0 + v1)) / Tp ** 2) * t ** 2 + (
            (2 * (0 - Lp) + Tp * (v0 + v1)) / Tp ** 3) * t ** 3

# Fin de marcha
zc_end = -Lp / 2 + v0 * t + ((3 * (0 - (-Lp / 2)) - Tp * (2 * v0 + v1)) / Tp ** 2) * t ** 2 + (
        (2 * ((-Lp / 2) - 0) + Tp * (v0 + v1)) / Tp ** 3) * t ** 3

zpf_end = -Lp + v0 * t + ((3 * (0 - (-Lp)) - Tp * (2 * v0 + v1)) / Tp ** 2) * t ** 2 + (
        (2 * ((-Lp) - 0) + Tp * (v0 + v1)) / Tp ** 3) * t ** 3

# Resumen planificación caminata
PosCadera = np.array([xpf_ps, ypf_pf, zc_start])
PosPieF = np.array([xpf_ps, ypf_pf, zpf_ps])

# Resumen inicio - fin de marcha
PosCadera_start = np.array([xpf_ps, ypf_pf, zc_start])
PosPieF_star = np.array([xpf_ps, ypf_pf, zpf_start])
PosCadera_end = np.array([xpf_ps, ypf_pf, zc_end])
PosPieF_end = np.array([xpf_ps, ypf_pf, zpf_end])


print(len(PosCadera_start[0]))
# Función para calcular los ángulos de la cadera respecto al pie de apoyo
#@jit
def calculate_qc(start_pos, end_pos, full_pos):
    qc_start = np.apply_along_axis(InversekinematicBiped_0, 1, 1000 * start_pos)
    qc_end = np.apply_along_axis(InversekinematicBiped_0, 1, 1000 * end_pos)
    qc = np.apply_along_axis(InversekinematicBiped_0, 1, 1000 * full_pos)

    return qc_start, qc_end, qc

# Función para calcular los ángulos del pie flotante respecto al pie de apoyo
#@jit

def calculate_qpf(start_pos, end_pos, full_pos):
    qpf_start = np.apply_along_axis(InversekinematicBiped_2, 1, 1000 * start_pos)
    qpf_end = np.apply_along_axis(InversekinematicBiped_2, 1, 1000 * end_pos)
    qpf = np.apply_along_axis(InversekinematicBiped_2, 1, 1000 * full_pos)

    return qpf_start, qpf_end, qpf


# Inicialización de variables
qc_start2, qc_end2, qcadera2 = calculate_qc(PosCadera_start, PosCadera_end, PosCadera)
qpf_start2, qpf_end2, qpf2 = calculate_qpf(PosPieF_star, PosPieF_end, PosPieF)

# Posiciones durante todo el ciclo
q5d = np.hstack((qc_start2[0, :], qcadera2[0, :], qc_end2[0, :]))
q4d = np.hstack((qc_start2[1, :], qcadera2[1, :], qc_end2[1, :]))
q3d = np.hstack((qc_start2[2, :], qcadera2[2, :], qc_end2[2, :]))
q2d = np.hstack((qc_start2[3, :], qcadera2[3, :], qc_end2[3, :]))
q1d = np.hstack((qc_start2[4, :], qcadera2[4, :], qc_end2[4, :]))

q1i = np.hstack((qpf_start2[0, :], qpf2[0, :], qpf_end2[0, :]))
q2i = np.hstack((qpf_start2[1, :], qpf2[1, :], qpf_end2[1, :]))
q3i = np.hstack((qpf_start2[2, :], qpf2[2, :], qpf_end2[2, :]))
q4i = np.hstack((qpf_start2[3, :], qpf2[3, :], qpf_end2[3, :]))
q5i = np.hstack((qpf_start2[4, :], qpf2[4, :], qpf_end2[4, :]))



