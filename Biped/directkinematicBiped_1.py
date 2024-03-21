

import numpy as np
from functions.denavit import denavit


def directkinematicBiped_1(q):
    # Longitudes de los Eslabones en mm.
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    # Parámetros de Denavit - Hartemberg del robot.
    teta1 = np.array([q[0], q[1]+np.pi/6, q[2]-np.pi/3, q[3]+np.pi/6, q[4]])
    d1 = np.array([0, 0, 0, 0, 0])
    a1 = np.array([L3, L4, L5, L6, L7])
    alfa1 = np.array([np.pi/2, 0, 0, -np.pi/2, 0])

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
    TC5i = np.dot(TC0, np.dot(T01, np.dot(T12, np.dot(T23, np.dot(T34, T45)))))

    return TC5i