# Funciones de la cinematica directa de cadera respecto al pie de apoyo 
import numpy as np 
#from numba import jit
#@jit
def F1HCPA(q5d, q4d, q3d, q2d, q1d):
    result = np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d) - np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.cos(q5d)*np.sin(q3d)*np.sin(q4d) - np.cos(q1d)*np.cos(q3d)*np.cos(q5d)*np.sin(q2d)*np.sin(q4d) - np.cos(q1d)*np.cos(q4d)*np.cos(q5d)*np.sin(q2d)*np.sin(q3d)
    return result

def F2HCPA(q5d, q4d, q3d, q2d, q1d):
    result = np.cos(q5d)*np.sin(q1d) + np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q3d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q4d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d)
    return result



def F3HCPA(q5d, q4d, q3d, q2d, q1d):
    result = np.sin(q1d - q2d - q3d - q4d)/2 - np.sin(q1d + q2d + q3d + q4d)/2
    return result


def F4HCPA(q5d, q4d, q3d, q2d, q1d):
    result = np.sin(q2d + q3d + q4d + q5d)/2 + np.sin(q2d + q3d + q4d - q5d)/2
    return result


def F5HCPA(q5d, q4d, q3d, q2d, q1d):
    result = np.cos(q2d + q3d + q4d - q5d)/2 - np.cos(q2d + q3d + q4d + q5d)/2
    return result


def F6HCPA(q5d, q4d, q3d, q2d, q1d):
    result = np.cos(q2d + q3d + q4d)
    return result

def F7HCPA(q5d, q4d, q3d, q2d, q1d):
    result = (np.cos(q1d)*np.sin(q5d) + np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d)*np.sin(q1d)
              - np.cos(q2d)*np.cos(q5d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d)
              - np.cos(q3d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d)
              - np.cos(q4d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d))
    return result



def F8HCPA(q5d, q4d, q3d, q2d, q1d):
    result = (np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q1d)*np.sin(q5d)
              - np.cos(q1d)*np.cos(q5d)
              - np.cos(q2d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d)
              - np.cos(q3d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d)
              - np.cos(q4d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d))
    return result


def F9HCPA(q5d, q4d, q3d, q2d, q1d):
    result = (np.cos(q1d + q2d + q3d + q4d)/2
              - np.cos(q1d - q2d - q3d - q4d)/2)
    return result



def F10HCPA(q5d, q4d, q3d, q2d, q1d):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    result = (L7
              + (np.cos(q5d)*(2*L6 - L4*np.sin(q3d + q4d) + L5*np.sin(q4d) + 2*L3*np.cos(q2d + q3d + q4d) + np.sqrt(3)*L4*np.cos(q3d + q4d) + np.sqrt(3)*L5*np.cos(q4d)))/2
              - L2*(np.sin(q1d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d) + np.cos(q1d)*np.cos(q2d)*np.cos(q5d)*np.sin(q3d)*np.sin(q4d) + np.cos(q1d)*np.cos(q3d)*np.cos(q5d)*np.sin(q2d)*np.sin(q4d) + np.cos(q1d)*np.cos(q4d)*np.cos(q5d)*np.sin(q2d)*np.sin(q3d))
              - L1*(np.cos(q2d)*np.cos(q5d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d) - np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.cos(q5d)*np.sin(q1d) - np.cos(q1d)*np.sin(q5d) + np.cos(q3d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d) + np.cos(q4d)*np.cos(q5d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d)))

    return result


def F11HCPA(q5d, q4d, q3d, q2d, q1d):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46

    result = (np.sin(q5d)*(2*L6 - L4*np.sin(q3d + q4d) + L5*np.sin(q4d) + 2*L3*np.cos(q2d + q3d + q4d) + np.sqrt(3)*L4*np.cos(q3d + q4d) + np.sqrt(3)*L5*np.cos(q4d)))/2
    - L1*(np.cos(q1d)*np.cos(q5d) - np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q1d)*np.sin(q5d) + np.cos(q2d)*np.sin(q1d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) + np.cos(q3d)*np.sin(q1d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) + np.cos(q4d)*np.sin(q1d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d))
    - L2*(np.cos(q1d)*np.cos(q2d)*np.sin(q3d)*np.sin(q4d)*np.sin(q5d) - np.cos(q1d)*np.cos(q2d)*np.cos(q3d)*np.cos(q4d)*np.sin(q5d) - np.cos(q5d)*np.sin(q1d) + np.cos(q1d)*np.cos(q3d)*np.sin(q2d)*np.sin(q4d)*np.sin(q5d) + np.cos(q1d)*np.cos(q4d)*np.sin(q2d)*np.sin(q3d)*np.sin(q5d))

    return result

def F12HCPA(q5d, q4d, q3d, q2d, q1d):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46
    result = (L5*np.cos(q4d))/2 - (L4*np.cos(q3d + q4d))/2 - L2*(np.sin(q1d + q2d + q3d + q4d)/2 - np.sin(q1d - q2d - q3d - q4d)/2) - L3*np.sin(q2d + q3d + q4d) + L1*(np.cos(q1d + q2d + q3d + q4d)/2 - np.cos(q1d - q2d - q3d - q4d)/2) - (np.sqrt(3)*L4*np.sin(q3d + q4d))/2 - (np.sqrt(3)*L5*np.sin(q4d))/2
    return result
