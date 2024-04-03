
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtCore import QThread, pyqtSignal, QObject

import numpy as np

from coppeliasim_send import CoppeliaSimConnection
from PyQt6.QtCore import QTimer
import requests
# df9b6a
#  849fa8 

from InversekinematicBiped_0 import InversekinematicBiped_0
from directkinematicBiped_0 import directkinematicBiped_0


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('C:\Programing\PyQt6\projects\Bipedo\design.ui', self)


        self.sim_connection = CoppeliaSimConnection()

        self.timer = QTimer()
        self.timer.timeout.connect(self.send_data)
        self.interval = 100  # Intervalo de tiempo en milisegundos
      
        self.checkBox_posicion.setChecked(True) #configuracion enviar posicion default
        self.checkBox_sliders.setChecked(False) #  Usando slidrs para enviar angulos a firebase

            

        self.q1d = np.deg2rad(0)
        self.q2d = np.deg2rad(0)
        self.q3d = np.deg2rad(-25)
        self.q4d = np.deg2rad(25)
        self.q5d = np.deg2rad(0)

        self.q1i = np.deg2rad(0)
        self.q2i = np.deg2rad(0)
        self.q3i = np.deg2rad(-25)
        self.q4i = np.deg2rad(25)
        self.q5i = np.deg2rad(0)


        self.bt_start.clicked.connect(self.start_simulation)
        self.bt_stop.clicked.connect(self.stop_simulation)    
        self.bt_pos_inicial.clicked.connect(self.posicion_inicial)    
        self.bt_cpa.clicked.connect(self.cadera_pie_apoyo)    

        self.bt_pfc.clicked.connect(self.pie_flotante_cadera)    
        self.bt_papf.clicked.connect(self.cadera_pie_apoyo_pie_flotante) 
        self.bt_enviar_fb.clicked.connect(self.send_values)     #reset_values                   
        self.bt_reset_fb.clicked.connect(self.reset_values)     #            


        self.slider_q1d.valueChanged['int'].connect(self.get_value_q1d)
        self.slider_q2d.valueChanged['int'].connect(self.get_value_q2d)
        self.slider_q3d.valueChanged['int'].connect(self.get_value_q3d)
        self.slider_q4d.valueChanged['int'].connect(self.get_value_q4d)
        self.slider_q5d.valueChanged['int'].connect(self.get_value_q5d)

        self.slider_q1i.valueChanged['int'].connect(self.get_value_q1i)
        self.slider_q2i.valueChanged['int'].connect(self.get_value_q2i)
        self.slider_q3i.valueChanged['int'].connect(self.get_value_q3i)
        self.slider_q4i.valueChanged['int'].connect(self.get_value_q4i)
        self.slider_q5i.valueChanged['int'].connect(self.get_value_q5i)



    def start_simulation(self):
        self.sim_connection.connect()
        self.timer.start(self.interval)


    def stop_simulation(self):
        self.sim_connection.disconnect()
        self.timer.stop()


    def send_data(self):
        pos0 = [np.radians(0), np.radians(0), np.radians(-25), np.radians(25), np.radians(0),
                np.radians(0), np.radians(0), np.radians(-25), np.radians(25), np.radians(0)]

        pos1 = [self.q1d, self.q2d, self.q3d, self.q4d, self.q5d,
                     self.q1i, self.q2i, self.q3i, self.q4i, self.q5i]


        print(pos1)
        # Crear una lista de posiciones
        positions = [pos1]

        self.sim_connection.set_joint_positions(positions)
        print("Enviando datos...")

    def posicion_inicial(self):
        pos0 = [np.radians(0), np.radians(0), np.radians(-25), np.radians(25), np.radians(0),
                np.radians(0), np.radians(0), np.radians(-25), np.radians(25), np.radians(0)]
        # Crear una lista de posiciones
        positions = [pos0]
        self.sim_connection.set_joint_positions(positions)
        self.slider_q1d.setValue(0)
        self.slider_q2d.setValue(0)
        self.slider_q3d.setValue(-25)
        self.slider_q4d.setValue(25)
        self.slider_q5d.setValue(0)

        self.slider_q1i.setValue(0)
        self.slider_q2i.setValue(0)
        self.slider_q3i.setValue(-25)
        self.slider_q4i.setValue(25)
        self.slider_q5i.setValue(0)

        print("Enviando posición inicial")

    def cadera_pie_apoyo(self):
        px = float(self.px_in.value())
        py = float(self.py_in.value())
        pz = float(self.pz_in.value())

        Pd = np.array([px, py, pz])
        Qd = InversekinematicBiped_0(Pd)
        pd = directkinematicBiped_0(Qd)
        print('Posiciones 0 : \n', pd[0,3], '\n',pd[1,3], '\n', pd[2,3])
        #print(pd)
        self.label_px.setText(f'Px: {(round(pd[0,3],3))}')
        self.label_py.setText(f'Py: {(round(pd[1,3],3))}')
        self.label_pz.setText(f'Pz: {(round(pd[2,3],3))}')

        self.value_r11.setText(f'{(round(pd[0,0],3))}')
        self.value_r21.setText(f'{(round(pd[1,0],3))}')
        self.value_r31.setText(f'{(round(pd[2,0],3))}')

        self.value_r12.setText(f'{(round(pd[0,1],3))}')
        self.value_r22.setText(f'{(round(pd[1,1],3))}')
        self.value_r32.setText(f'{(round(pd[2,1],3))}')

        self.value_r13.setText(f'{(round(pd[0,2],3))}')
        self.value_r23.setText(f'{(round(pd[1,2],3))}')
        self.value_r33.setText(f'{(round(pd[2,2],3))}')

        self.value_dx.setText(f'{(round(pd[0,3],3))}')
        self.value_dy.setText(f'{(round(pd[1,3],3))}')
        self.value_dz.setText(f'{(round(pd[2,3],3))}')




    def pie_flotante_cadera(self):
        px = float(self.px_in_2.value())
        py = float(self.py_in_2.value())
        pz = float(self.pz_in_2.value())

        Pi = np.array([px, py, pz])
        Qi = InversekinematicBiped_0(Pi)
        pi = directkinematicBiped_0(Qi)
        print('Posiciones 0 : \n', pi[0,3], '\n',pi[1,3], '\n', pi[2,3])
        self.label_px_2.setText(f'Px: {(round(pi[0,3],3))}')
        self.label_py_2.setText(f'Py: {(round(pi[1,3],3))}')
        self.label_pz_2.setText(f'Pz: {(round(pi[2,3],3))}')

        self.value_r11_2.setText(f'{(round(pi[0,0],3))}')
        self.value_r21_2.setText(f'{(round(pi[1,0],3))}')
        self.value_r31_2.setText(f'{(round(pi[2,0],3))}')

        self.value_r12_2.setText(f'{(round(pi[0,1],3))}')
        self.value_r22_2.setText(f'{(round(pi[1,1],3))}')
        self.value_r32_2.setText(f'{(round(pi[2,1],3))}')

        self.value_r13_2.setText(f'{(round(pi[0,2],3))}')
        self.value_r23_2.setText(f'{(round(pi[1,2],3))}')
        self.value_r33_2.setText(f'{(round(pi[2,2],3))}')

        self.value_dx_2.setText(f'{(round(pi[0,3],3))}')
        self.value_dy_2.setText(f'{(round(pi[1,3],3))}')
        self.value_dz_2.setText(f'{(round(pi[2,3],3))}')

    def cadera_pie_apoyo_pie_flotante(self):
        px = float(self.px_in_3.value())
        py = float(self.py_in_3.value())
        pz = float(self.pz_in_3.value())

        P = np.array([px, py, pz])
        Q = InversekinematicBiped_0(P)
        p1 = directkinematicBiped_0(Q)
        print('Posiciones 0 : \n', p1[0,3], '\n',p1[1,3], '\n', p1[2,3])
        self.label_px_3.setText(f'Px: {(round(p1[0,3],3))}')
        self.label_py_3.setText(f'Py: {(round(p1[1,3],3))}')
        self.label_pz_3.setText(f'Pz: {(round(p1[2,3],3))}')

        self.value_r11_3.setText(f'{(round(p1[0,0],3))}')
        self.value_r21_3.setText(f'{(round(p1[1,0],3))}')
        self.value_r31_3.setText(f'{(round(p1[2,0],3))}')

        self.value_r12_3.setText(f'{(round(p1[0,1],3))}')
        self.value_r22_3.setText(f'{(round(p1[1,1],3))}')
        self.value_r32_3.setText(f'{(round(p1[2,1],3))}')

        self.value_r13_3.setText(f'{(round(p1[0,2],3))}')
        self.value_r23_3.setText(f'{(round(p1[1,2],3))}')
        self.value_r33_3.setText(f'{(round(p1[2,2],3))}')

        self.value_dx_3.setText(f'{(round(p1[0,3],3))}')
        self.value_dy_3.setText(f'{(round(p1[1,3],3))}')
        self.value_dz_3.setText(f'{(round(p1[2,3],3))}')


        #.....................................

    def reset_values(self):
        firebase_url = 'https://realtime-smartlamp-default-rtdb.firebaseio.com/'
        CD_PieaPie = 'CinDirecta/CDPieaPie.json'

        data = {'q1': 0, 'q2': 0, 'q3': -25, 'q4': 25, 'q5': 0,
                'q6': 0, 'q7': 0, 'q8': -25, 'q9': 25, 'q10': 0}

        response = requests.patch(firebase_url + CD_PieaPie, json=data)

        if response.status_code == 200:
            print("Datos reseteados")
        else:
            print('No se pudo resetear')
        self.Qxd_label.setText(f'Q1d:     Q2d:  Q3d:   Q4d:    Q5d:  ')
        self.px_in_4.setValue(0.0)
        self.py_in_4.setValue(0.0)
        self.pz_in_4.setValue(0.0)




    def send_values(self):
        # Imprimir el valor de todos los sliders
        q1 = round(np.rad2deg(self.q1d),1) #self.sliders[0].slider.value()
        q2 = round(np.rad2deg(self.q2d),1)
        q3 = round(np.rad2deg(self.q3d),1)
        q4 = round(np.rad2deg(self.q4d),1)
        q5 = round(np.rad2deg(self.q5d),1)
        q6 = round(np.rad2deg(self.q1i),1)
        q7 = round(np.rad2deg(self.q2i),1)
        q8 = round(np.rad2deg(self.q3i),1)
        q9 = round(np.rad2deg(self.q4i),1)
        q10 = round(np.rad2deg(self.q5i),1)

        if self.checkBox_posicion.isChecked():  #open:
            px = float(self.px_in_4.value())
            py = float(self.py_in_4.value())
            pz = float(self.pz_in_4.value())

            Pd = np.array([px, py, pz])
            Qd = InversekinematicBiped_0(Pd)
            pd = directkinematicBiped_0(Qd)

            q1 = round(np.rad2deg(Qd[0]), 1)  #self.sliders[0].slider.value()
            q2 = round(np.rad2deg(Qd[1]), 1)
            q3 = round(np.rad2deg(Qd[2]), 1)
            q4 = round(np.rad2deg(Qd[3]), 1)
            q5 = round(np.rad2deg(Qd[4]), 1)
            print("Funcionando valores posicion")
 
 
        self.Qxd_label.setText(f'Q1d: {q1}    Q2d:  {q2}  Q3d: {q3}   Q4d:   {q4} Q5d: {q5} ')
        firebase_url = 'https://realtime-smartlamp-default-rtdb.firebaseio.com/'
        CD_PieaPie = 'CinDirecta/CDPieaPie.json'
        data = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5,
                'q6': q6, 'q7': q7, 'q8': q8, 'q9': q9, 'q10': q10}

        response = requests.patch(firebase_url + CD_PieaPie, json=data)
        if response.status_code == 200:
            print("Datos Enviados")
        else:
            print('No se pudo enviar los datos')
        print(self.q1d)


    def get_value_q1d(self, event):
        self.q1d = np.deg2rad(event)
        self.label_q1d.setText(f'{event}°')

    def get_value_q2d(self, event):
        self.q2d = np.deg2rad(event)
        self.label_q2d.setText(f'{event}°')


    def get_value_q3d(self, event):
        self.q3d = np.deg2rad(event)
        self.label_q3d.setText(f'{event} °')


    def get_value_q4d(self, event):
        self.q4d = np.deg2rad(event)
        self.label_q4d.setText(f'{event}°')
    def get_value_q5d(self, event):
        self.q5d = np.deg2rad(event)
        self.label_q5d.setText(f'{event}°')    

    def get_value_q1i(self, event):
        self.q1i = np.deg2rad(event)
        self.label_q1i.setText(f'{event}°')
    def get_value_q2i(self, event):
        self.q2i = np.deg2rad(event)
        self.label_q2i.setText(f'{event}°')
    def get_value_q3i(self, event):
        self.q3i = np.deg2rad(event)
        self.label_q3i.setText(f'{event} °')
    def get_value_q4i(self, event):
        self.q4i = np.deg2rad(event)
        self.label_q4i.setText(f'{event}°')
    def get_value_q5i(self, event):
        self.q5i = np.deg2rad(event)
        self.label_q5i.setText(f'{event}°')  




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())









