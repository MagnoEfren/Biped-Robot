
import numpy as np
#from numba import jit

from functions.FxHCPA import *


def InversekinematicBiped_0(P):
    # Valores iniciales de la longitud (mm)
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    # Valores iniciales de las articulaciones
    q5d = 0
    q4d = 0
    q3d = 0
    q2d = 0
    q1d = 0

    dx = 0.0001  # Variación para el cálculo de la derivada discreta

    for n in range(1000):  # Número de iteraciones
        # Funciones F_HCPA
        F = np.array([
            np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d) - np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.cos(q5d)*np.sin(q3d)*np.sin(q4d) - np.cos(q1d)*np.cos(q3d)*np.cos(q5d)*np.sin(q2d)*np.sin(q4d) - np.cos(q1d)*np.cos(q4d)*np.cos(q5d)*np.sin(q2d)*np.sin(q3d),
            np.cos(q5d)*np.sin(q1d) + np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q3d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q4d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d),
            np.sin(q1d - q2d - q3d - q4d)/2 - np.sin(q1d + q2d + q3d + q4d)/2,
            np.sin(q2d + q3d + q4d + q5d)/2 + np.sin(q2d + q3d + q4d - q5d)/2,
            np.cos(q2d + q3d + q4d - q5d)/2 - np.cos(q2d + q3d + q4d + q5d)/2,
            np.cos(q2d + q3d + q4d),
            np.cos(q1d)*np.sin(q5d) + np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d)*np.sin(q1d) - np.cos(q2d)*np.cos(q5d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d) - np.cos(q3d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d) - np.cos(q4d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d),
            np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q5d) - np.cos(q2d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) - np.cos(q3d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) - np.cos(q4d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d),
            np.cos(q1d + q2d + q3d + q4d)/2 - np.cos(q1d - q2d - q3d - q4d)/2,
            L7 + (np.cos(q5d)*(2*L6 - L4*np.sin(q3d + q4d) + L5*np.sin(q4d) + 2*L3*np.cos(q2d + q3d + q4d) + np.sqrt(3)*L4*np.cos(q3d + q4d) + np.sqrt(3)*L5*np.cos(q4d)))/2 - L2*(np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d) + np.cos(q1d)*np.cos(q2d)*np.cos(q5d)*np.sin(q3d)*np.sin(q4d) + np.cos(q1d)*np.cos(q3d)*np.cos(q5d)*np.sin(q2d)*np.sin(q4d) + np.cos(q1d)*np.cos(q4d)*np.cos(q5d)*np.sin(q2d)*np.sin(q3d)) - L1*(np.cos(q2d)*np.cos(q5d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d) - np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d)*np.sin(q1d) - np.cos(q1d)*np.sin(q5d) + np.cos(q3d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d) + np.cos(q4d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d)),
            (np.sin(q5d)*(2*L6 - L4*np.sin(q3d + q4d) + L5*np.sin(q4d) + 2*L3*np.cos(q2d + q3d + q4d) + np.sqrt(3)*L4*np.cos(q3d + q4d) + np.sqrt(3)*L5*np.cos(q4d)))/2 - L1*(np.cos(q1d)*np.cos(q5d) - np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q1d)*np.sin(q5d) + np.cos(q2d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) + np.cos(q3d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) + np.cos(q4d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d)) - L2*(np.cos(q1d)*np.cos(q2d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q5d) - np.cos(q5d)*np.sin(q1d) + np.cos(q1d)*np.cos(q3d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) + np.cos(q1d)*np.cos(q4d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d)),
            (L5*np.cos(q4d))/2 - (L4*np.cos(q3d + q4d))/2 - L2*(np.sin(q1d + q2d + q3d + q4d)/2 - np.sin(q1d - q2d - q3d - q4d)/2) - L3*np.sin(q2d + q3d + q4d) + L1*(np.cos(q1d + q2d + q3d + q4d)/2 - np.cos(q1d - q2d - q3d - q4d)/2) - (np.sqrt(3)*L4*np.sin(q3d + q4d))/2 - (np.sqrt(3)*L5*np.sin(q4d))/2 ])

        # F set Point. Posicionamiento de la cadera a la que se moverá.
        Fsp = np.array([1, 0, 0, 0, 0, -1, 0, 1, 0, P[0], P[1], P[2]])

        # Error
        error = Fsp - F
        s = 0
        for i in range(12):
            s = np.sum(np.abs(error[i]))
        if s < 0.0001:
            break

        # Cálculo de las derivadas
        dp5 = q5d + dx
        dp4 = q4d + dx
        dp3 = q3d + dx
        dp2 = q2d + dx
        dp1 = q1d + dx

        # Matriz Jacobiana
        J = np.zeros((12, 5))
        J[0,0] = (F1HCPA(dp5, q4d, q3d, q2d, q1d) - F1HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[0,1] = (F1HCPA(q5d, dp4, q3d, q2d, q1d) - F1HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[0,2] = (F1HCPA(q5d, q4d, dp3, q2d, q1d) - F1HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[0,3] = (F1HCPA(q5d, q4d, q3d, dp2, q1d) - F1HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[0,4] = (F1HCPA(q5d, q4d, q3d, q2d, dp1) - F1HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[1,0] = (F2HCPA(dp5, q4d, q3d, q2d, q1d) - F2HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[1,1] = (F2HCPA(q5d, dp4, q3d, q2d, q1d) - F2HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[1,2] = (F2HCPA(q5d, q4d, dp3, q2d, q1d) - F2HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[1,3] = (F2HCPA(q5d, q4d, q3d, dp2, q1d) - F2HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[1,4] = (F2HCPA(q5d, q4d, q3d, q2d, dp1) - F2HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[2,0] = (F3HCPA(dp5, q4d, q3d, q2d, q1d) - F3HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[2,1] = (F3HCPA(q5d, dp4, q3d, q2d, q1d) - F3HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[2,2] = (F3HCPA(q5d, q4d, dp3, q2d, q1d) - F3HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[2,3] = (F3HCPA(q5d, q4d, q3d, dp2, q1d) - F3HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[2,4] = (F3HCPA(q5d, q4d, q3d, q2d, dp1) - F3HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[3,0] = (F4HCPA(dp5, q4d, q3d, q2d, q1d) - F4HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[3,1] = (F4HCPA(q5d, dp4, q3d, q2d, q1d) - F4HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[3,2] = (F4HCPA(q5d, q4d, dp3, q2d, q1d) - F4HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[3,3] = (F4HCPA(q5d, q4d, q3d, dp2, q1d) - F4HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[3,4] = (F4HCPA(q5d, q4d, q3d, q2d, dp1) - F4HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[4,0] = (F5HCPA(dp5, q4d, q3d, q2d, q1d) - F5HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[4,1] = (F5HCPA(q5d, dp4, q3d, q2d, q1d) - F5HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[4,2] = (F5HCPA(q5d, q4d, dp3, q2d, q1d) - F5HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[4,3] = (F5HCPA(q5d, q4d, q3d, dp2, q1d) - F5HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[4,4] = (F5HCPA(q5d, q4d, q3d, q2d, dp1) - F5HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[5,0] = (F6HCPA(dp5, q4d, q3d, q2d, q1d) - F6HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[5,1] = (F6HCPA(q5d, dp4, q3d, q2d, q1d) - F6HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[5,2] = (F6HCPA(q5d, q4d, dp3, q2d, q1d) - F6HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[5,3] = (F6HCPA(q5d, q4d, q3d, dp2, q1d) - F6HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[5,4] = (F6HCPA(q5d, q4d, q3d, q2d, dp1) - F6HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[6,0] = (F7HCPA(dp5, q4d, q3d, q2d, q1d) - F7HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[6,1] = (F7HCPA(q5d, dp4, q3d, q2d, q1d) - F7HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[6,2] = (F7HCPA(q5d, q4d, dp3, q2d, q1d) - F7HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[6,3] = (F7HCPA(q5d, q4d, q3d, dp2, q1d) - F7HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[6,4] = (F7HCPA(q5d, q4d, q3d, q2d, dp1) - F7HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[7,0] = (F8HCPA(dp5, q4d, q3d, q2d, q1d) - F8HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[7,1] = (F8HCPA(q5d, dp4, q3d, q2d, q1d) - F8HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[7,2] = (F8HCPA(q5d, q4d, dp3, q2d, q1d) - F8HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[7,3] = (F8HCPA(q5d, q4d, q3d, dp2, q1d) - F8HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[7,4] = (F8HCPA(q5d, q4d, q3d, q2d, dp1) - F8HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[8,0] = (F9HCPA(dp5, q4d, q3d, q2d, q1d) - F9HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[8,1] = (F9HCPA(q5d, dp4, q3d, q2d, q1d) - F9HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[8,2] = (F9HCPA(q5d, q4d, dp3, q2d, q1d) - F9HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[8,3] = (F9HCPA(q5d, q4d, q3d, dp2, q1d) - F9HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[8,4] = (F9HCPA(q5d, q4d, q3d, q2d, dp1) - F9HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[9,0] = (F10HCPA(dp5, q4d, q3d, q2d, q1d) - F10HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[9,1] = (F10HCPA(q5d, dp4, q3d, q2d, q1d) - F10HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[9,2] = (F10HCPA(q5d, q4d, dp3, q2d, q1d) - F10HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[9,3] = (F10HCPA(q5d, q4d, q3d, dp2, q1d) - F10HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[9,4] = (F10HCPA(q5d, q4d, q3d, q2d, dp1) - F10HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[10,0] = (F11HCPA(dp5, q4d, q3d, q2d, q1d) - F11HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[10,1] = (F11HCPA(q5d, dp4, q3d, q2d, q1d) - F11HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[10,2] = (F11HCPA(q5d, q4d, dp3, q2d, q1d) - F11HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[10,3] = (F11HCPA(q5d, q4d, q3d, dp2, q1d) - F11HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[10,4] = (F11HCPA(q5d, q4d, q3d, q2d, dp1) - F11HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        J[11,0] = (F12HCPA(dp5, q4d, q3d, q2d, q1d) - F12HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[11,1] = (F12HCPA(q5d, dp4, q3d, q2d, q1d) - F12HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[11,2] = (F12HCPA(q5d, q4d, dp3, q2d, q1d) - F12HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[11,3] = (F12HCPA(q5d, q4d, q3d, dp2, q1d) - F12HCPA(q5d, q4d, q3d, q2d, q1d))/dx
        J[11,4] = (F12HCPA(q5d, q4d, q3d, q2d, dp1) - F12HCPA(q5d, q4d, q3d, q2d, q1d))/dx

        # Matriz Pseudoinversa por el Teorema de Moore - Penrose
        # landa = 1
        # dtheta = np.linalg.inv(J.T @ J + np.eye(5) * landa) @ J.T @ error
        # Método Levenberg-Marquardt

        landa = 1
        dtheta = np.linalg.inv(J.T @ J + np.eye(5) * landa) @ J.T @ error

        q5d += dtheta[0]
        q4d += dtheta[1]
        q3d += dtheta[2]
        q2d += dtheta[3]
        q1d += dtheta[4]

    # Estandarización de los ángulos
    q11d = q1d - np.round(q1d / (2 * np.pi)) * 2 * np.pi
    q11ds = np.degrees(q11d)
    q22d = q2d - np.round(q2d / (2 * np.pi)) * 2 * np.pi
    q22ds = np.degrees(q22d)
    q33d = q3d - np.round(q3d / (2 * np.pi)) * 2 * np.pi
    q33ds = np.degrees(q33d)
    q44d = q4d - np.round(q4d / (2 * np.pi)) * 2 * np.pi
    q44ds = np.degrees(q44d)
    q55d = q5d - np.round(q5d / (2 * np.pi)) * 2 * np.pi
    q55ds = np.degrees(q55d)

    Q = [q55d, q44d, q33d, q22d, q11d]
    Q1 = [q5d, q4d, q3d, q2d, q1d]
    Q2 = [q55ds, q44ds, q33ds, q22ds, q11ds]  # en Sexagesimal

    return Q
