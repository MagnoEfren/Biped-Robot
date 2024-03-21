import numpy as np

def denavit(teta, d, a, alfa):
    ct = np.cos(teta)
    st = np.sin(teta)
    ca = np.cos(alfa)
    sa = np.sin(alfa)
    T = np.array([[ct, -st*ca, st*sa, a*ct],
                  [st, ct*ca, -ct*sa, a*st],
                  [0, sa, ca, d],
                  [0, 0, 0, 1]])
    return T
