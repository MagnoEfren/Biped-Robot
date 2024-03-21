
import numpy as np
from functions.denavit import denavit



def directkinematicBiped_2(q):
    # CADERA RESPECTO AL PIE DE APOYO

    # Longitudes de los Eslabones en mm
    L1d = 41.45
    L2d = 16.9
    L3d = 46.88
    L4d = 84.96
    L5d = 68.32
    L6d = 46.07
    L7d = 17.46

    # Parámetros de D-H
    teta = [q[0]  ,q[1] - np.pi/6, q[2] + np.pi/3,  q[3] - np.pi/6, q[4] ]
    d = [0, 0, 0, 0, 0]
    a = [L6d, L5d, L4d, L3d, 0]
    alfa = [-np.pi/2, 0, 0, np.pi/2, 0]

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
    T5dC = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(T54d, T43d), T32d), T21d), T10d), T00d), T0Cd)

    # PIE FLOTANTE RESPECTO A LA CADERA (IZQUIERDA)
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    # Parámetros de Denavit - Hartemberg del robot.
    teta1 = [q[5], q[6] + np.pi/6, q[7] - np.pi/3, q[8] + np.pi/6, q[9]]
    d1 = [0, 0, 0, 0, 0]
    a1 = [L3, L4, L5, L6, L7]
    alfa1 = [np.pi/2, 0, 0, -np.pi/2, 0]

    # M.T.H entre sistemas de Coordenadas
    T01 = denavit(teta1[0], d1[0], a1[0], alfa1[0])
    T12 = denavit(teta1[1], d1[1], a1[1], alfa1[1])
    T23 = denavit(teta1[2], d1[2], a1[2], alfa1[2])
    T34 = denavit(teta1[3], d1[3], a1[3], alfa1[3])
    T45 = denavit(teta1[4], d1[4], a1[4], alfa1[4])

    # Matriz de Tranformación de la Cadera.
    TC0 = np.array([[-1, 0, 0, -L2],
                    [0, 0, 1, 0],
                    [0, 1, 0, L1],
                    [0, 0, 0, 1]])

    # M.T.H pie flotante-cadera
    TC5i = np.dot(np.dot(np.dot(np.dot(np.dot(TC0, T01), T12), T23), T34), T45)

    # RELACIÓN DEL PIE FLOTANTE RESPECTO AL PIE DE APOYO.
    TT = np.dot(T5dC, TC5i)
    #TT = [TT[0, 3], TT[1, 3], TT[2, 3]]

    return TT