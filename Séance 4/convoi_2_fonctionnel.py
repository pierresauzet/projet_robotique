from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

# =========================
# Variables globales
# =========================
done_1 = False
done_2 = False
done_3 = False

# =========================
# Gestion erreur
# =========================
def on_comm_error(error):
    print(error)
    os._exit(1)

# =========================
# OBS TIMIDE
# =========================
def obs_anxieux(nid):
    global done_1
    if not done_1:
        # Si le bouton est au centre, on termine l'action
        if th_1[nid]["button.center"] == 1:
            done_1 = True
            th_1[nid]["motor.left.target"]  = 0
            th_1[nid]["motor.right.target"] = 0
            return

        # Si le bouton de "forward" est appuyé, afficher un message
        if th_1[nid]["button.forward"] == 1:
            print("Je suis anxieux!")

        # Proximité de l'obstacle sur la gauche (on suppose que l'indice 'prox.horizontal' inclut des informations sur la gauche)
        prox = th_1[nid]["prox.horizontal"]

        if max(prox[0:2]) > 2000:
            # tourne à droite
            th_1[nid]["motor.left.target"]  = 200
            th_1[nid]["motor.right.target"] = 60

        # droite = capteurs 3,4
        elif max(prox[3:5]) > 2000:
            # tourne à gauche
            th_1[nid]["motor.left.target"]  = 60
            th_1[nid]["motor.right.target"] = 200

        else:

            th_1[nid]["motor.left.target"]  = 150
            th_1[nid]["motor.right.target"] = 150

# =========================
# OBS DIRIGE
# =========================
def obs_dirige1(nid):
    global done_2
    if not done_2:
        if th_2[nid]["button.center"] == 1:
            done_2 = True
            th_2[nid]["motor.left.target"]  = 0
            th_2[nid]["motor.right.target"] = 0
            return

        if th_2[nid]["button.forward"] == 1:
            print("Je suis dirigé!")

        prox = th_2[nid]["prox.horizontal"]

        # gauche = capteurs 0,1
        if max(prox[0:2]) > 2000:
            # tourne à gauche
            th_2[nid]["motor.left.target"]  = 60
            th_2[nid]["motor.right.target"] = 200

        # droite = capteurs 3,4
        elif max(prox[3:5]) > 2000:
            # tourne à droite
            th_2[nid]["motor.left.target"]  = 200
            th_2[nid]["motor.right.target"] = 60


        else:
            # avance (zigzag naturel via corrections)
            th_2[nid]["motor.left.target"]  = 200
            th_2[nid]["motor.right.target"] = 200


# =========================
# OBS ATTRACTION / REPULSION
# =========================
def obs_dirige2(nid):
    global done_3
    if not done_3:
        if th_3[nid]["button.center"] == 1:
            done_3 = True
            th_3[nid]["motor.left.target"]  = 0
            th_3[nid]["motor.right.target"] = 0
            return

        if th_3[nid]["button.forward"] == 1:
            print("Je suis dirigé!")

        prox = th_3[nid]["prox.horizontal"]

        # gauche = capteurs 0,1
        if max(prox[0:2]) > 2000:
            # tourne à gauche
            th_3[nid]["motor.left.target"]  = 60
            th_3[nid]["motor.right.target"] = 200

        # droite = capteurs 3,4
        elif max(prox[3:5]) > 2000:
            # tourne à droite
            th_3[nid]["motor.left.target"]  = 200
            th_3[nid]["motor.right.target"] = 60

        else:
            # avance (zigzag naturel via corrections)
            th_3[nid]["motor.left.target"]  = 200
            th_3[nid]["motor.right.target"] = 200


# =========================
# Connexion robots
# =========================
ports = ThymioSerialPort.get_ports()



th_1 = Thymio(serial_port=ports[0].device, refreshing_rate=0.1,
              refreshing_coverage={"prox.horizontal", "button.center","button.forward"})
th_2 = Thymio(serial_port=ports[1].device, refreshing_rate=0.1,
              refreshing_coverage={"prox.horizontal", "button.center","button.forward"})
th_3 = Thymio(serial_port=ports[2].device, refreshing_rate=0.1,
              refreshing_coverage={"prox.horizontal", "button.center","button.forward"})

th_1.on_comm_error = on_comm_error
th_2.on_comm_error = on_comm_error
th_3.on_comm_error = on_comm_error

th_1.connect()
th_2.connect()
th_3.connect()

id_1 = th_1.first_node()
id_2 = th_2.first_node()
id_3 = th_3.first_node()

th_1.set_variable_observer(id_1, obs_anxieux)
th_2.set_variable_observer(id_2, obs_dirige1)
th_3.set_variable_observer(id_3, obs_dirige2)

# =========================
# Boucle principale
# =========================
while not (done_1 and done_2 and done_3):
    time.sleep(0.05)
    print(done_1, done_2, done_3)

# =========================
# Déconnexion
# =========================
th_1.disconnect()
th_2.disconnect()
th_3.disconnect()