
#   #494949   gris fundo 
#   #df9b6a    naranjado 
#   #849fa8    celeste  palido 
#   #caff31     verdeamarrillento 

import numpy as np 


from InversekinematicBiped_0 import InversekinematicBiped_0
from directkinematicBiped_0 import directkinematicBiped_0

from InversekinematicBiped_1 import InversekinematicBiped_1
from directkinematicBiped_1 import directkinematicBiped_1

from InversekinematicBiped_2 import InversekinematicBiped_2
from directkinematicBiped_2 import directkinematicBiped_2


Pd = np.array([1.3, 2.5, 3.7])
Qd = InversekinematicBiped_0(Pd)
pd = directkinematicBiped_0(Qd)
print('Posiciones 0 : \n', pd[0,3], '\n',pd[1,3], '\n', pd[2,3])


Pi = np.array([1.3, 2.5, 3.7])
Qi = InversekinematicBiped_1(Pi)
pi = directkinematicBiped_1(Qi)
print('Posiciones 1 : \n', pi[0,3], '\n',pi[1,3], '\n', pi[2,3])


P = np.array([30,14,17])
Q = InversekinematicBiped_2(P)
p1 = directkinematicBiped_2(Q)
print('Posiciones 2 : \n', p1[0,3], '\n',p1[1,3], '\n', p1[2,3])




    
"""class Worker(QObject):
    def __init__(self, positions, parent=None):
        super().__init__(parent)
        finished = pyqtSignal()
        # Resto del código...

    def do_work(self, data):
        # Realiza alguna tarea con los datos aquí
        print("Datos actualizados:", data)
        self.finished.emit()

class MyThread(QThread):
    def __init__(self, data):
        super().__init__()
        self.worker = Worker()
        self.data = data
        self._running = False

    def run(self):
        self._running = True
        while self._running:
            self.worker.do_work(self.data)  # Pasar los datos al worker
        self._running = False

    def stop(self):
        self._running = False

"""