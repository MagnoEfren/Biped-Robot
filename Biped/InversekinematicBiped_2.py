


import numpy as np
from functions.FxHPAPF import * 

def InversekinematicBiped_2(P):

    #valores Iniciales de la Longitud (mm):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46
    #angulos (rad)
    q1d=0; #-0.0134;
    q2d=0; #-0.4386;
    q3d=0; #1.4693;
    q4d=0; #-1.0090;
    q5d=0; #0.0013;
    # angulos (rad)
    q1i=0;
    q2i=0;
    q3i=0;
    q4i=0;
    q5i=0;
    dx=0.0001;

    for n in range(1000):  # Número de iteraciones
        # Funciones F_HPAPF
        F = np.array([
        (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*(np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + np.sin(q5i)*np.cos(q1i)) + np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q5d)*np.cos(q5i) ,
        (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*(np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + np.sin(q5i)*np.cos(q1i)) + np.sin(q5d)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q5i) ,
        -(np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i))*np.sin(q2d + q3d + q4d)*np.cos(q1d) - (np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + np.sin(q5i)*np.cos(q1i))*np.sin(q1d)*np.sin(q2d + q3d + q4d) + np.sin(q2i + q3i + q4i)*np.cos(q5i)*np.cos(q2d + q3d + q4d) ,
        (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.cos(q5i) + np.sin(q5i)*np.cos(q1i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*(-np.sin(q1i)*np.sin(q5i)*np.cos(q2i + q3i + q4i) + np.cos(q1i)*np.cos(q5i)) - np.sin(q5i)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q5d) ,
        (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.cos(q5i) + np.sin(q5i)*np.cos(q1i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*(-np.sin(q1i)*np.sin(q5i)*np.cos(q2i + q3i + q4i) + np.cos(q1i)*np.cos(q5i)) - np.sin(q5d)*np.sin(q5i)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i) ,
        -(np.sin(q1i)*np.cos(q5i) + np.sin(q5i)*np.cos(q1i)*np.cos(q2i + q3i + q4i))*np.sin(q2d + q3d + q4d)*np.cos(q1d) - (-np.sin(q1i)*np.sin(q5i)*np.cos(q2i + q3i + q4i) + np.cos(q1i)*np.cos(q5i))*np.sin(q1d)*np.sin(q2d + q3d + q4d) - np.sin(q5i)*np.sin(q2i + q3i + q4i)*np.cos(q2d + q3d + q4d) ,
        (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*np.sin(q2i + q3i + q4i)*np.cos(q1i) - (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*np.sin(q1i)*np.sin(q2i + q3i + q4i) + np.sin(q2d + q3d + q4d)*np.cos(q5d)*np.cos(q2i + q3i + q4i) ,
        (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*np.sin(q2i + q3i + q4i)*np.cos(q1i) - (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*np.sin(q1i)*np.sin(q2i + q3i + q4i) + np.sin(q5d)*np.sin(q2d + q3d + q4d)*np.cos(q2i + q3i + q4i) ,
        np.sin(q1d)*np.sin(q1i)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i) - np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q1d)*np.cos(q1i) + np.cos(q2d + q3d + q4d)*np.cos(q2i + q3i + q4i) ,
        L1*(np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d)) - L2*(np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d)) + L7 + (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*(-L2 - L3*np.cos(q1i) - L4*np.cos(q1i)*np.cos(q2i + np.pi/6) - L5*np.sin(q2i + q3i + np.pi/3)*np.cos(q1i) - L6*np.cos(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.sin(q5i) - L7*np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*(L1 + L3*np.sin(q1i) + L4*np.sin(q1i)*np.cos(q2i + np.pi/6) + L5*np.sin(q1i)*np.sin(q2i + q3i + np.pi/3) + L6*np.sin(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q5i)*np.cos(q1i)) + (L3*np.cos(q2d + q3d + q4d) + L4*np.cos(q3d + q4d + np.pi/6) + L5*np.sin(q4d + np.pi/3) + L6)*np.cos(q5d) + (L4*np.sin(q2i + np.pi/6) - L5*np.cos(q2i + q3i + np.pi/3) + L6*np.sin(q2i + q3i + q4i) + L7*np.sin(q2i + q3i + q4i)*np.cos(q5i))*np.sin(q2d + q3d + q4d)*np.cos(q5d) ,
        L1*(np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d)) + L2*(np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d)) + (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*(-L2 - L3*np.cos(q1i) - L4*np.cos(q1i)*np.cos(q2i + np.pi/6) - L5*np.sin(q2i + q3i + np.pi/3)*np.cos(q1i) - L6*np.cos(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.sin(q5i) - L7*np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*(L1 + L3*np.sin(q1i) + L4*np.sin(q1i)*np.cos(q2i + np.pi/6) + L5*np.sin(q1i)*np.sin(q2i + q3i + np.pi/3) + L6*np.sin(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q5i)*np.cos(q1i)) + (L3*np.cos(q2d + q3d + q4d) + L4*np.cos(q3d + q4d + np.pi/6) + L5*np.sin(q4d + np.pi/3) + L6)*np.sin(q5d) + (L4*np.sin(q2i + np.pi/6) - L5*np.cos(q2i + q3i + np.pi/3) + L6*np.sin(q2i + q3i + q4i) + L7*np.sin(q2i + q3i + q4i)*np.cos(q5i))*np.sin(q5d)*np.sin(q2d + q3d + q4d) ,
        -L1*np.sin(q1d)*np.sin(q2d + q3d + q4d) - L2*np.sin(q2d + q3d + q4d)*np.cos(q1d) - L3*np.sin(q2d + q3d + q4d) - L4*np.sin(q3d + q4d + np.pi/6) + L5*np.cos(q4d + np.pi/3) + (L4*np.sin(q2i + np.pi/6) - L5*np.cos(q2i + q3i + np.pi/3) + L6*np.sin(q2i + q3i + q4i) + L7*np.sin(q2i + q3i + q4i)*np.cos(q5i))*np.cos(q2d + q3d + q4d) - (L1 + L3*np.sin(q1i) + L4*np.sin(q1i)*np.cos(q2i + np.pi/6) + L5*np.sin(q1i)*np.sin(q2i + q3i + np.pi/3) + L6*np.sin(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q5i)*np.cos(q1i))*np.sin(q1d)*np.sin(q2d + q3d + q4d) - (-L2 - L3*np.cos(q1i) - L4*np.cos(q1i)*np.cos(q2i + np.pi/6) - L5*np.sin(q2i + q3i + np.pi/3)*np.cos(q1i) - L6*np.cos(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.sin(q5i) - L7*np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i))*np.sin(q2d + q3d + q4d)*np.cos(q1d) ,
        ])
        # F set Point. Posicionamiento de la cadera a la que se moverá.
        Fsp = np.array([
            -1, 0, 0, 0, -1, 0, 0, 0, 1, P[0], P[1], P[2]
        ])

        # Error
        error = Fsp - F
        s = 0
        for i in range(12):
            s = np.sum(np.abs(error[i]))
        if s < 0.0001:
            break

        # Cálculo de las derivadas
        dp1=q1i+dx;
        dp2=q2i+dx;
        dp3=q3i+dx;
        dp4=q4i+dx;
        dp5=q5i+dx;

        # Matriz Jacobiana
        J = np.zeros((12, 5))
        J[0,0] = (F1HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[0,1] = (F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[0,2] = (F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[0,3] = (F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[0,4] = (F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F1HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[1,0] = (F2HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[1,1] = (F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[1,2] = (F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[1,3] = (F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[1,4] = (F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F2HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[2,0] = (F3HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[2,1] = (F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[2,2] = (F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[2,3] = (F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[2,4] = (F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F3HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[3,0] = (F4HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[3,1] = (F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[3,2] = (F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[3,3] = (F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[3,4] = (F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F4HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[4,0] = (F5HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[4,1] = (F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[4,2] = (F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[4,3] = (F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[4,4] = (F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F5HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[5,0] = (F6HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[5,1] = (F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[5,2] = (F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[5,3] = (F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[5,4] = (F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F6HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[6,0] = (F7HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[6,1] = (F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[6,2] = (F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[6,3] = (F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[6,4] = (F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F7HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[7,0] = (F8HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[7,1] = (F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[7,2] = (F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[7,3] = (F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[7,4] = (F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F8HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[8,0] = (F9HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[8,1] = (F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[8,2] = (F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[8,3] = (F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[8,4] = (F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F9HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[9,0] = (F10HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[9,1] = (F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[9,2] = (F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[9,3] = (F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[9,4] = (F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F10HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[10,0] = (F11HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[10,1] = (F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[10,2] = (F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[10,3] = (F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[10,4] = (F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F11HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

        J[11,0] = (F12HPAPF(q5d,q4d,q3d,q2d,q1d,dp1,q2i,q3i,q4i,q5i) - F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[11,1] = (F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,dp2,q3i,q4i,q5i) - F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[11,2] = (F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,dp3,q4i,q5i) - F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[11,3] = (F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,dp4,q5i) - F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx
        J[11,4] = (F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,dp5) - F12HPAPF(q5d,q4d,q3d,q2d,q1d,q1i,q2i,q3i,q4i,q5i))/dx

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

    Q = np.array([q5d, q4d, q3d, q2d, q1d, q11i, q22i, q33i, q44i, q55i])
    Q1 = np.array([q5d, q4d, q3d, q2d, q1d])
    Q2 = np.array([q11is, q22is, q33is, q44is, q55is])  # en Sexagesimal
    return Q
