# Funciones 
import numpy as np 

def F1HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*(np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + np.sin(q5i)*np.cos(q1i)) + np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q5d)*np.cos(q5i)

    return x


def F2HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*(np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + np.sin(q5i)*np.cos(q1i)) + np.sin(q5d)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q5i)

    return x

def F3HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = -(np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i))*np.sin(q2d + q3d + q4d)*np.cos(q1d) - (np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + np.sin(q5i)*np.cos(q1i))*np.sin(q1d)*np.sin(q2d + q3d + q4d) + np.sin(q2i + q3i + q4i)*np.cos(q5i)*np.cos(q2d + q3d + q4d)

    return x


def F4HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.cos(q5i) + np.sin(q5i)*np.cos(q1i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*(-np.sin(q1i)*np.sin(q5i)*np.cos(q2i + q3i + q4i) + np.cos(q1i)*np.cos(q5i)) - np.sin(q5i)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q5d)

    return x


def F5HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*(np.sin(q1i)*np.cos(q5i) + np.sin(q5i)*np.cos(q1i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*(-np.sin(q1i)*np.sin(q5i)*np.cos(q2i + q3i + q4i) + np.cos(q1i)*np.cos(q5i)) - np.sin(q5d)*np.sin(q5i)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)

    return x

def F6HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = -(np.sin(q1i)*np.cos(q5i) + np.sin(q5i)*np.cos(q1i)*np.cos(q2i + q3i + q4i))*np.sin(q2d + q3d + q4d)*np.cos(q1d) - (-np.sin(q1i)*np.sin(q5i)*np.cos(q2i + q3i + q4i) + np.cos(q1i)*np.cos(q5i))*np.sin(q1d)*np.sin(q2d + q3d + q4d) - np.sin(q5i)*np.sin(q2i + q3i + q4i)*np.cos(q2d + q3d + q4d)

    return x

def F7HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*np.sin(q2i + q3i + q4i)*np.cos(q1i) - (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*np.sin(q1i)*np.sin(q2i + q3i + q4i) + np.sin(q2d + q3d + q4d)*np.cos(q5d)*np.cos(q2i + q3i + q4i)

    return x

def F8HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    x = (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*np.sin(q2i + q3i + q4i)*np.cos(q1i) - (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*np.sin(q1i)*np.sin(q2i + q3i + q4i) + np.sin(q5d)*np.sin(q2d + q3d + q4d)*np.cos(q2i + q3i + q4i)

    return x

def F9HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    return  np.sin(q1d)*np.sin(q1i)*np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i) - np.sin(q2d + q3d + q4d)*np.sin(q2i + q3i + q4i)*np.cos(q1d)*np.cos(q1i) + np.cos(q2d + q3d + q4d)*np.cos(q2i + q3i + q4i)


def F10HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    x = L1*(np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d)) - L2*(np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d)) + L7 + (-np.sin(q1d)*np.sin(q5d) + np.cos(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d))*(-L2 - L3*np.cos(q1i) - L4*np.cos(q1i)*np.cos(q2i + np.pi/6) - L5*np.sin(q2i + q3i + np.pi/3)*np.cos(q1i) - L6*np.cos(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.sin(q5i) - L7*np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.cos(q5d)*np.cos(q2d + q3d + q4d) + np.sin(q5d)*np.cos(q1d))*(L1 + L3*np.sin(q1i) + L4*np.sin(q1i)*np.cos(q2i + np.pi/6) + L5*np.sin(q1i)*np.sin(q2i + q3i + np.pi/3) + L6*np.sin(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q5i)*np.cos(q1i)) + (L3*np.cos(q2d + q3d + q4d) + L4*np.cos(q3d + q4d + np.pi/6) + L5*np.sin(q4d + np.pi/3) + L6)*np.cos(q5d) + (L4*np.sin(q2i + np.pi/6) - L5*np.cos(q2i + q3i + np.pi/3) + L6*np.sin(q2i + q3i + q4i) + L7*np.sin(q2i + q3i + q4i)*np.cos(q5i))*np.sin(q2d + q3d + q4d)*np.cos(q5d)

    return x

def F11HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    x = L1*(np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d)) + L2*(np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d)) + (np.sin(q1d)*np.cos(q5d) + np.sin(q5d)*np.cos(q1d)*np.cos(q2d + q3d + q4d))*(-L2 - L3*np.cos(q1i) - L4*np.cos(q1i)*np.cos(q2i + np.pi/6) - L5*np.sin(q2i + q3i + np.pi/3)*np.cos(q1i) - L6*np.cos(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.sin(q5i) - L7*np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i)) + (np.sin(q1d)*np.sin(q5d)*np.cos(q2d + q3d + q4d) - np.cos(q1d)*np.cos(q5d))*(L1 + L3*np.sin(q1i) + L4*np.sin(q1i)*np.cos(q2i + np.pi/6) + L5*np.sin(q1i)*np.sin(q2i + q3i + np.pi/3) + L6*np.sin(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q5i)*np.cos(q1i)) + (L3*np.cos(q2d + q3d + q4d) + L4*np.cos(q3d + q4d + np.pi/6) + L5*np.sin(q4d + np.pi/3) + L6)*np.sin(q5d) + (L4*np.sin(q2i + np.pi/6) - L5*np.cos(q2i + q3i + np.pi/3) + L6*np.sin(q2i + q3i + q4i) + L7*np.sin(q2i + q3i + q4i)*np.cos(q5i))*np.sin(q5d)*np.sin(q2d + q3d + q4d)

    return x


def F12HPAPF(q5d, q4d, q3d, q2d, q1d, q1i, q2i, q3i, q4i, q5i):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    x = -L1*np.sin(q1d)*np.sin(q2d + q3d + q4d) - L2*np.sin(q2d + q3d + q4d)*np.cos(q1d) - L3*np.sin(q2d + q3d + q4d) - L4*np.sin(q3d + q4d + np.pi/6) + L5*np.cos(q4d + np.pi/3) + (L4*np.sin(q2i + np.pi/6) - L5*np.cos(q2i + q3i + np.pi/3) + L6*np.sin(q2i + q3i + q4i) + L7*np.sin(q2i + q3i + q4i)*np.cos(q5i))*np.cos(q2d + q3d + q4d) - (L1 + L3*np.sin(q1i) + L4*np.sin(q1i)*np.cos(q2i + np.pi/6) + L5*np.sin(q1i)*np.sin(q2i + q3i + np.pi/3) + L6*np.sin(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q5i)*np.cos(q1i))*np.sin(q1d)*np.sin(q2d + q3d + q4d) - (-L2 - L3*np.cos(q1i) - L4*np.cos(q1i)*np.cos(q2i + np.pi/6) - L5*np.sin(q2i + q3i + np.pi/3)*np.cos(q1i) - L6*np.cos(q1i)*np.cos(q2i + q3i + q4i) + L7*np.sin(q1i)*np.sin(q5i) - L7*np.cos(q1i)*np.cos(q5i)*np.cos(q2i + q3i + q4i))*np.sin(q2d + q3d + q4d)*np.cos(q1d)
    return x