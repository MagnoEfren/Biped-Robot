

import numpy as np
from functions.FxHPFC import * 


def InversekinematicBiped_1(P):
    # valores Iniciales de la Longitud (mm):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46
    # Valores Iniciales de las articulaciones.
    q1i=0;
    q2i=0;
    q3i=0;
    q4i=0;
    q5i=0;

    dx = 0.0001  # Variación para el cálculo de la derivada discreta

    for n in range(1000):  # Número de iteraciones
        # Funciones F_HPFC
        F = np.array([
            np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i) + np.cos(q1i)*np.cos(q2i)*np.cos(q5i)*np.sin(q3i)*np.sin(q4i) + np.cos(q1i)*np.cos(q3i)*np.cos(q5i)*np.sin(q2i)*np.sin(q4i) + np.cos(q1i)*np.cos(q4i)*np.cos(q5i)*np.sin(q2i)*np.sin(q3i),
            np.sin(q2i + q3i + q4i + q5i)/2 + np.sin(q2i + q3i + q4i - q5i)/2,
            np.cos(q1i)*np.sin(q5i) + np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i)*np.sin(q1i) - np.cos(q2i)*np.cos(q5i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i) - np.cos(q3i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i) - np.cos(q4i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i),
            np.cos(q5i)*np.sin(q1i) + np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.sin(q5i) - np.cos(q1i)*np.cos(q2i)*np.sin(q3i)*np.sin(q4i)*np.sin(q5i) - np.cos(q1i)*np.cos(q3i)*np.sin(q2i)*np.sin(q4i)*np.sin(q5i) - np.cos(q1i)*np.cos(q4i)*np.sin(q2i)*np.sin(q3i)*np.sin(q5i),
            np.cos(q2i + q3i + q4i + q5i)/2 - np.cos(q2i + q3i + q4i - q5i)/2,
            np.cos(q1i)*np.cos(q5i) - np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.sin(q1i)*np.sin(q5i) + np.cos(q2i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i)*np.sin(q5i) + np.cos(q3i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i)*np.sin(q5i) + np.cos(q4i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i)*np.sin(q5i),
            np.sin(q1i + q2i + q3i + q4i)/2 - np.sin(q1i - q2i - q3i - q4i)/2,
            np.cos(q2i + q3i + q4i),
            np.cos(q1i + q2i + q3i + q4i)/2 - np.cos(q1i - q2i - q3i - q4i)/2,
            (L4*np.cos(q1i)*np.sin(q2i))/2 - L3*np.cos(q1i) - L2 + L7*np.sin(q1i)*np.sin(q5i) - (L5*np.cos(q1i)*np.cos(q2i)*np.sin(q3i))/2 - (L5*np.cos(q1i)*np.cos(q3i)*np.sin(q2i))/2 - (np.sqrt(3)*L4*np.cos(q1i)*np.cos(q2i))/2 + L6*np.cos(q1i)*np.cos(q2i)*np.sin(q3i)*np.sin(q4i) + L6*np.cos(q1i)*np.cos(q3i)*np.sin(q2i)*np.sin(q4i) + L6*np.cos(q1i)*np.cos(q4i)*np.sin(q2i)*np.sin(q3i) - (np.sqrt(3)*L5*np.cos(q1i)*np.cos(q2i)*np.cos(q3i))/2 + (np.sqrt(3)*L5*np.cos(q1i)*np.sin(q2i)*np.sin(q3i))/2 - L6*np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i) - L7*np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i) + L7*np.cos(q1i)*np.cos(q2i)*np.cos(q5i)*np.sin(q3i)*np.sin(q4i) + L7*np.cos(q1i)*np.cos(q3i)*np.cos(q5i)*np.sin(q2i)*np.sin(q4i) + L7*np.cos(q1i)*np.cos(q4i)*np.cos(q5i)*np.sin(q2i)*np.sin(q3i),
            (L7*np.sin(q2i + q3i + q4i + q5i))/2 - (L5*np.cos(q2i + q3i))/2 + (L4*np.cos(q2i))/2 + (L7*np.sin(q2i + q3i + q4i - q5i))/2 + L6*np.sin(q2i + q3i + q4i) + (np.sqrt(3)*L5*np.sin(q2i + q3i))/2 + (np.sqrt(3)*L4*np.sin(q2i))/2,
            L1 + L3*np.sin(q1i) + L7*np.cos(q1i)*np.sin(q5i) - (L4*np.sin(q1i)*np.sin(q2i))/2 + (L5*np.cos(q2i)*np.sin(q1i)*np.sin(q3i))/2 + (L5*np.cos(q3i)*np.sin(q1i)*np.sin(q2i))/2 + (np.sqrt(3)*L4*np.cos(q2i)*np.sin(q1i))/2 + L6*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.sin(q1i) - L6*np.cos(q2i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i) - L6*np.cos(q3i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i) - L6*np.cos(q4i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i) + (np.sqrt(3)*L5*np.cos(q2i)*np.cos(q3i)*np.sin(q1i))/2 - (np.sqrt(3)*L5*np.sin(q1i)*np.sin(q2i)*np.sin(q3i))/2 - L7*np.cos(q2i)*np.cos(q5i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i) - L7*np.cos(q3i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i) - L7*np.cos(q4i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i) + L7*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i)*np.sin(q1i)
            ])

        # F set Point. Posicionamiento de la cadera a la que se moverá.
        Fsp = np.array([
            -1, 0, 0, 0, 0, 1, 0, 1, 0, P[0], P[1], P[2]
        ])

        # Error
        error = Fsp - F
        s = 0
        for i in range(12):
            s = np.sum(np.abs(error[i]))
        if s < 0.0001:
            break

        # Cálculo de las derivadas
        dp1=q1i+dx
        dp2=q2i+dx
        dp3=q3i+dx
        dp4=q4i+dx
        dp5=q5i+dx

        # Matriz Jacobiana
        J = np.zeros((12, 5))
        J[0,0] = (F1HPFC(dp1,q2i,q3i,q4i,q5i) - F1HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[0,1] = (F1HPFC(q1i,dp2,q3i,q4i,q5i) - F1HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[0,2] = (F1HPFC(q1i,q2i,dp3,q4i,q5i) - F1HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[0,3] = (F1HPFC(q1i,q2i,q3i,dp4,q5i) - F1HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[0,4] = (F1HPFC(q1i,q2i,q3i,q4i,dp5) - F1HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[1,0] = (F2HPFC(dp1,q2i,q3i,q4i,q5i) - F2HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[1,1] = (F2HPFC(q1i,dp2,q3i,q4i,q5i) - F2HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[1,2] = (F2HPFC(q1i,q2i,dp3,q4i,q5i) - F2HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[1,3] = (F2HPFC(q1i,q2i,q3i,dp4,q5i) - F2HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[1,4] = (F2HPFC(q1i,q2i,q3i,q4i,dp5) - F2HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[2,0] = (F3HPFC(dp1,q2i,q3i,q4i,q5i) - F3HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[2,1] = (F3HPFC(q1i,dp2,q3i,q4i,q5i) - F3HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[2,2] = (F3HPFC(q1i,q2i,dp3,q4i,q5i) - F3HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[2,3] = (F3HPFC(q1i,q2i,q3i,dp4,q5i) - F3HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[2,4] = (F3HPFC(q1i,q2i,q3i,q4i,dp5) - F3HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[3,0] = (F4HPFC(dp1,q2i,q3i,q4i,q5i) - F4HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[3,1] = (F4HPFC(q1i,dp2,q3i,q4i,q5i) - F4HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[3,2] = (F4HPFC(q1i,q2i,dp3,q4i,q5i) - F4HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[3,3] = (F4HPFC(q1i,q2i,q3i,dp4,q5i) - F4HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[3,4] = (F4HPFC(q1i,q2i,q3i,q4i,dp5) - F4HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[4,0] = (F5HPFC(dp1,q2i,q3i,q4i,q5i) - F5HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[4,1] = (F5HPFC(q1i,dp2,q3i,q4i,q5i) - F5HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[4,2] = (F5HPFC(q1i,q2i,dp3,q4i,q5i) - F5HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[4,3] = (F5HPFC(q1i,q2i,q3i,dp4,q5i) - F5HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[4,4] = (F5HPFC(q1i,q2i,q3i,q4i,dp5) - F5HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[5,0] = (F6HPFC(dp1,q2i,q3i,q4i,q5i) - F6HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[5,1] = (F6HPFC(q1i,dp2,q3i,q4i,q5i) - F6HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[5,2] = (F6HPFC(q1i,q2i,dp3,q4i,q5i) - F6HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[5,3] = (F6HPFC(q1i,q2i,q3i,dp4,q5i) - F6HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[5,4] = (F6HPFC(q1i,q2i,q3i,q4i,dp5) - F6HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[6,0] = (F7HPFC(dp1,q2i,q3i,q4i,q5i) - F7HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[6,1] = (F7HPFC(q1i,dp2,q3i,q4i,q5i) - F7HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[6,2] = (F7HPFC(q1i,q2i,dp3,q4i,q5i) - F7HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[6,3] = (F7HPFC(q1i,q2i,q3i,dp4,q5i) - F7HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[6,4] = (F7HPFC(q1i,q2i,q3i,q4i,dp5) - F7HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[7,0] = (F8HPFC(dp1,q2i,q3i,q4i,q5i) - F8HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[7,1] = (F8HPFC(q1i,dp2,q3i,q4i,q5i) - F8HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[7,2] = (F8HPFC(q1i,q2i,dp3,q4i,q5i) - F8HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[7,3] = (F8HPFC(q1i,q2i,q3i,dp4,q5i) - F8HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[7,4] = (F8HPFC(q1i,q2i,q3i,q4i,dp5) - F8HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[8,0] = (F9HPFC(dp1,q2i,q3i,q4i,q5i) - F9HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[8,1] = (F9HPFC(q1i,dp2,q3i,q4i,q5i) - F9HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[8,2] = (F9HPFC(q1i,q2i,dp3,q4i,q5i) - F9HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[8,3] = (F9HPFC(q1i,q2i,q3i,dp4,q5i) - F9HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[8,4] = (F9HPFC(q1i,q2i,q3i,q4i,dp5) - F9HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[9,0] = (F10HPFC(dp1,q2i,q3i,q4i,q5i) - F10HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[9,1] = (F10HPFC(q1i,dp2,q3i,q4i,q5i) - F10HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[9,2] = (F10HPFC(q1i,q2i,dp3,q4i,q5i) - F10HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[9,3] = (F10HPFC(q1i,q2i,q3i,dp4,q5i) - F10HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[9,4] = (F10HPFC(q1i,q2i,q3i,q4i,dp5) - F10HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[10,0] = (F11HPFC(dp1,q2i,q3i,q4i,q5i) - F11HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[10,1] = (F11HPFC(q1i,dp2,q3i,q4i,q5i) - F11HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[10,2] = (F11HPFC(q1i,q2i,dp3,q4i,q5i) - F11HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[10,3] = (F11HPFC(q1i,q2i,q3i,dp4,q5i) - F11HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[10,4] = (F11HPFC(q1i,q2i,q3i,q4i,dp5) - F11HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        J[11,0] = (F12HPFC(dp1,q2i,q3i,q4i,q5i) - F12HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[11,1] = (F12HPFC(q1i,dp2,q3i,q4i,q5i) - F12HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[11,2] = (F12HPFC(q1i,q2i,dp3,q4i,q5i) - F12HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[11,3] = (F12HPFC(q1i,q2i,q3i,dp4,q5i) - F12HPFC(q1i,q2i,q3i,q4i,q5i))/dx
        J[11,4] = (F12HPFC(q1i,q2i,q3i,q4i,dp5) - F12HPFC(q1i,q2i,q3i,q4i,q5i))/dx

        # Matriz Pseudoinversa por el Teorema de Moore - Penrose
        # landa = 1
        # dtheta = np.linalg.inv(J.T @ J + np.eye(5) * landa) @ J.T @ error
        # Método Levenberg-Marquardt

        landa = 1
        dtheta = np.linalg.inv(J.T @ J + np.eye(5) * landa) @ J.T @ error

        q1i += dtheta[0]
        q2i += dtheta[1]
        q3i += dtheta[2]
        q4i += dtheta[3]
        q5i += dtheta[4]

    # Estanderizacion de los angulos
    q11i = q1i - np.round(q1i / (2 * np.pi)) * 2 * np.pi
    q11is = q11i * 180 / np.pi
    q22i = q2i - np.round(q2i / (2 * np.pi)) * 2 * np.pi
    q22is = q22i * 180 / np.pi
    q33i = q3i - np.round(q3i / (2 * np.pi)) * 2 * np.pi
    q33is = q33i * 180 / np.pi
    q44i = q4i - np.round(q4i / (2 * np.pi)) * 2 * np.pi
    q44is = q44i * 180 / np.pi
    q55i = q5i - np.round(q5i / (2 * np.pi)) * 2 * np.pi
    q55is = q55i * 180 / np.pi

    Q = np.array([q11i, q22i, q33i, q44i, q55i])
    Q1 = np.array([q1i, q2i, q3i, q4i, q5i])
    Q2 = np.array([q11is, q22is, q33is, q44is, q55is])  # en Sexagesimal

    return Q