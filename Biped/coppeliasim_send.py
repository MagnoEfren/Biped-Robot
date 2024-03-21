import sim
import time
import numpy as np
import keyboard

class CoppeliaSimConnection:
    def __init__(self):
        self.client_id = -1
        self.joint_handles = []

    def connect(self):
        sim.simxFinish(-1)  # Cerrar cualquier conexión existente
        self.client_id = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Conectar a CoppeliaSim
        if self.client_id != -1:
            print("Conexión establecida con CoppeliaSim")
            joint_names = ["jointd1", "jointd2", "jointd3", "jointd4", "jointd5",
                           "jointi1", "jointi2", "jointi3", "jointi4", "jointi5"]
            self.joint_handles = [0] * 10
            for i in range(10):
                _, self.joint_handles[i] = sim.simxGetObjectHandle(self.client_id, joint_names[i], sim.simx_opmode_oneshot_wait)
        else:
            print("No se pudo conectar a CoppeliaSim")

    def disconnect(self):
        if self.client_id != -1:
            sim.simxFinish(self.client_id)
            print("Conexión con CoppeliaSim cerrada")

    def set_joint_positions(self, positions):
        if self.client_id != -1:
            for j in range(len(positions)):
                for i in range(len(positions[j])):
                    sim.simxSetJointTargetPosition(self.client_id, self.joint_handles[i], positions[j][i], sim.simx_opmode_oneshot)
                time.sleep(1)
        else:
            print("No se puede establecer la conexión con CoppeliaSim")




"""
import sim
import time
import numpy as np
import keyboard

def main():
    sim.simxFinish(-1)  # Cerrar cualquier conexión existente
    client_id = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Conectar a CoppeliaSim

    if client_id != -1:
        print("Conexión establecida con CoppeliaSim")
        joint_names = ["jointd1", "jointd2", "jointd3", "jointd4", "jointd5","jointi1", "jointi2", "jointi3", "jointi4", "jointi5"]
        joint_handles = [0] * 10

        for i in range(10):
            _, joint_handles[i] = sim.simxGetObjectHandle(client_id, joint_names[i], sim.simx_opmode_oneshot_wait)

        while True:
            if keyboard.is_pressed('q'):
                print("\n Programa finalizado.")
                break

            # Posiciones
            pos0 = [np.radians(0) , np.radians(0), np.radians(-25),np.radians(25) , np.radians(0),
             np.radians(0),np.radians(0) , np.radians(-25), np.radians(25), np.radians(0)]

            pos1 = [np.radians(0), np.radians(0), np.radians(-25), np.radians(25), np.radians(0), 
            np.radians(0), np.radians(0), np.radians(-25), np.radians(25), np.radians(45)]

            pos2 = [np.radians(30), np.radians(0), np.radians(-350), np.radians(40), np.radians(30), 
            np.radians(40), np.radians(40), np.radians(30), np.radians(-40), np.radians(30)]

            pos3 = [np.radians(60), np.radians(0), np.radians(-290), np.radians(0), np.radians(90), 
            np.radians(0), np.radians(90), np.radians(0), np.radians(90), np.radians(0)]

            pos4 = [np.radians(30), np.radians(0), np.radians(-250), np.radians(40), np.radians(60), 
            np.radians(40), np.radians(40), np.radians(30), np.radians(-40), np.radians(30)]

            positions =[pos0, pos1]


            for j in range(2):  #cantidad de posiciones 
                for i in range(10): #cantidad de articulaciones 
                    sim.simxSetJointTargetPosition(client_id, joint_handles[i], positions[j][i], sim.simx_opmode_oneshot)
                time.sleep(1)
            #print("11")

    else:
        print("No se pudo conectar a CoppeliaSim")

if __name__ == "__main__":
    main()

"""