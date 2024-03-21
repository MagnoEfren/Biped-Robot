
import numpy as np 

def F1HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.sin(q1i)*np.sin(q5i) - np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i) + np.cos(q1i)*np.cos(q2i)*np.cos(q5i)*np.sin(q3i)*np.sin(q4i) + np.cos(q1i)*np.cos(q3i)*np.cos(q5i)*np.sin(q2i)*np.sin(q4i) + np.cos(q1i)*np.cos(q4i)*np.cos(q5i)*np.sin(q2i)*np.sin(q3i)
    return result


def F2HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.sin(q2i + q3i + q4i + q5i)/2 + np.sin(q2i + q3i + q4i - q5i)/2
    return result

def F3HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.cos(q1i)*np.sin(q5i) + np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i)*np.sin(q1i) - np.cos(q2i)*np.cos(q5i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i) - np.cos(q3i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i) - np.cos(q4i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i)
    return result

def F4HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.cos(q5i)*np.sin(q1i) + np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.sin(q5i) - np.cos(q1i)*np.cos(q2i)*np.sin(q3i)*np.sin(q4i)*np.sin(q5i) - np.cos(q1i)*np.cos(q3i)*np.sin(q2i)*np.sin(q4i)*np.sin(q5i) - np.cos(q1i)*np.cos(q4i)*np.sin(q2i)*np.sin(q3i)*np.sin(q5i)
    return result


def F5HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.cos(q2i + q3i + q4i + q5i)/2 - np.cos(q2i + q3i + q4i - q5i)/2
    return result

def F6HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.cos(q1i)*np.cos(q5i) - np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.sin(q1i)*np.sin(q5i) + np.cos(q2i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i)*np.sin(q5i) + np.cos(q3i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i)*np.sin(q5i) + np.cos(q4i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i)*np.sin(q5i)
    return result

def F7HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.sin(q1i + q2i + q3i + q4i)/2 - np.sin(q1i - q2i - q3i - q4i)/2
    return result

def F8HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.cos(q2i + q3i + q4i)
    return result

def F9HPFC(q1i, q2i, q3i, q4i, q5i):
    result = np.cos(q1i + q2i + q3i + q4i)/2 - np.cos(q1i - q2i - q3i - q4i)/2
    return result

def F10HPFC(q1i, q2i, q3i, q4i, q5i):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46
    result = (L4*np.cos(q1i)*np.sin(q2i))/2 - L3*np.cos(q1i) - L2 + L7*np.sin(q1i)*np.sin(q5i) - (L5*np.cos(q1i)*np.cos(q2i)*np.sin(q3i))/2 - (L5*np.cos(q1i)*np.cos(q3i)*np.sin(q2i))/2 - (np.sqrt(3)*L4*np.cos(q1i)*np.cos(q2i))/2 + L6*np.cos(q1i)*np.cos(q2i)*np.sin(q3i)*np.sin(q4i) + L6*np.cos(q1i)*np.cos(q3i)*np.sin(q2i)*np.sin(q4i) + L6*np.cos(q1i)*np.cos(q4i)*np.sin(q2i)*np.sin(q3i) - (np.sqrt(3)*L5*np.cos(q1i)*np.cos(q2i)*np.cos(q3i))/2 + (np.sqrt(3)*L5*np.cos(q1i)*np.sin(q2i)*np.sin(q3i))/2 - L6*np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i) - L7*np.cos(q1i)*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i) + L7*np.cos(q1i)*np.cos(q2i)*np.cos(q5i)*np.sin(q3i)*np.sin(q4i) + L7*np.cos(q1i)*np.cos(q3i)*np.cos(q5i)*np.sin(q2i)*np.sin(q4i) + L7*np.cos(q1i)*np.cos(q4i)*np.cos(q5i)*np.sin(q2i)*np.sin(q3i)
    return result


def F11HPFC(q1i, q2i, q3i, q4i, q5i):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46
    result = (L7*np.sin(q2i + q3i + q4i + q5i))/2 - (L5*np.cos(q2i + q3i))/2 + (L4*np.cos(q2i))/2 + (L7*np.sin(q2i + q3i + q4i - q5i))/2 + L6*np.sin(q2i + q3i + q4i) + (np.sqrt(3)*L5*np.sin(q2i + q3i))/2 + (np.sqrt(3)*L4*np.sin(q2i))/2
    return result

def F12HPFC(q1i, q2i, q3i, q4i, q5i):
    L1 = 41.45
    L2 = 16.9
    L3 = 46.88
    L4 = 84.96
    L5 = 68.32
    L6 = 46.07
    L7 = 17.46
    result = L1 + L3*np.sin(q1i) + L7*np.cos(q1i)*np.sin(q5i) - (L4*np.sin(q1i)*np.sin(q2i))/2 + (L5*np.cos(q2i)*np.sin(q1i)*np.sin(q3i))/2 + (L5*np.cos(q3i)*np.sin(q1i)*np.sin(q2i))/2 + (np.sqrt(3)*L4*np.cos(q2i)*np.sin(q1i))/2 + L6*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.sin(q1i) - L6*np.cos(q2i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i) - L6*np.cos(q3i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i) - L6*np.cos(q4i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i) + (np.sqrt(3)*L5*np.cos(q2i)*np.cos(q3i)*np.sin(q1i))/2 - (np.sqrt(3)*L5*np.sin(q1i)*np.sin(q2i)*np.sin(q3i))/2 - L7*np.cos(q2i)*np.cos(q5i)*np.sin(q1i)*np.sin(q3i)*np.sin(q4i) - L7*np.cos(q3i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q4i) - L7*np.cos(q4i)*np.cos(q5i)*np.sin(q1i)*np.sin(q2i)*np.sin(q3i) + L7*np.cos(q2i)*np.cos(q3i)*np.cos(q4i)*np.cos(q5i)*np.sin(q1i)
    return result