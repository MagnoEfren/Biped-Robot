

import numpy as np
from functions.denavit import denavit


def directkinematicBiped_0(q):
    # Longitudes de los Eslabones en mm.
    L1d = 41.45
    L2d = 16.9
    L3d = 46.88
    L4d = 84.96
    L5d = 68.32
    L6d = 46.07
    L7d = 17.46
    # Parámetros de D-H
    teta = np.array([q[0], q[1]-np.pi/6, q[2]+np.pi/3, q[3]-np.pi/6, q[4]])
    d = np.array([0, 0, 0, 0, 0])
    a = np.array([L6d, L5d, L4d, L3d, 0])
    alfa = np.array([-np.pi/2, 0, 0, np.pi/2, 0])

    # M.T.H entre sistemas de Coordenadas
    T43d = denavit(teta[0], d[0], a[0], alfa[0])
    T32d = denavit(teta[1], d[1], a[1], alfa[1])
    T21d = denavit(teta[2], d[2], a[2], alfa[2])
    T10d = denavit(teta[3], d[3], a[3], alfa[3])
    T00d = denavit(teta[4], d[4], a[4], alfa[4])

    # Matriz Tranformación de la Base del Pie a la Articulación1
    T54d = np.array([[1, 0, 0, L7d],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

    # Matriz de Tranformación de la Cadera.
    T0Cd = np.array([[1, 0, 0, L2d],
                     [0, 0, -1, -L1d],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1]])

    # M.T.H cadera-pie de apoyo
    T5dc = np.dot(T54d, np.dot(T43d, np.dot(T32d, np.dot(T21d, np.dot(T10d, np.dot(T00d, T0Cd))))))

    return T5dc