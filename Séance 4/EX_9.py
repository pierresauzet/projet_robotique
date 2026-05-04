from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

# Variables globales
global done_leader, done_follower, leader_distance
done_leader = False
done_follower = False

# Fonction de gestion des erreurs de communication
def on_comm_error(error):
    print(error)
    os._exit(1)  # Quitte le programme en cas de problème de communication

# Observer pour le robot leader
def obs_leader(node_id):
    global done_leader, leader_distance
    if not(done_leader):
        # Lecture de la valeur des capteurs du leader
        value = th_leader[node_id]["prox.horizontal"][2]
        button_center = th_leader[node_id]["button.center"]

        # Conversion de la distance
        if value > 0:
            leader_distance = 14000 / value  # Calcul de la distance en cm
        else:
            leader_distance = float("inf")

        print(f"Leader distance: {leader_distance:.1f} cm")


        if leader_distance < 10:
            print("danger: objet à moins de 10 cm")
            th_leader[node_id]["motor.left.target"] = 0
            th_leader[node_id]["motor.right.target"] = 0
        # Faire avancer le leader si l'obstacle est à une distance acceptable
        
        if leader_distance > 10:
            th_leader[node_id]["motor.left.target"] = 400
            th_leader[node_id]["motor.right.target"] = 400

        # Arrêt du leader si le bouton est pressé
        if button_center:
            th_leader[node_id]["motor.left.target"] = 0
            th_leader[node_id]["motor.right.target"] = 0
            done_leader = True

# Observer pour le robot suiveur
def obs_follower(node_id):
    global done_follower, leader_distance
    if not(done_follower):
        # Lecture de la valeur des capteurs du suiveur
        value = th_follower[node_id]["prox.horizontal"][2]
        button_center = th_follower[node_id]["button.center"]

        # Conversion de la distance
        if value > 0:
            follower_distance = 14000 / value  # Calcul de la distance en cm
        else:
            follower_distance = float("inf")

        print(f"Follower distance: {follower_distance:.1f} cm")

        # Ajustement de la position du suiveur pour maintenir 15 cm derrière le leader
        if leader_distance > 15:  # Si trop loin du leader
            th_follower[node_id]["motor.left.target"] = 400
            th_follower[node_id]["motor.right.target"] = 400
        else:  # Si à 15 cm
            th_follower[node_id]["motor.left.target"] = 0
            th_follower[node_id]["motor.right.target"] = 0

        # Arrêt du suiveur si le bouton est pressé
        if button_center:
            th_follower[node_id]["motor.left.target"] = 0
            th_follower[node_id]["motor.right.target"] = 0
            done_follower = True

# Détection des ports
thymio_serial_ports = ThymioSerialPort.get_ports()
serial_port_leader = thymio_serial_ports[0].device
serial_port_follower = thymio_serial_ports[1].device
print(serial_port_leader)
print(serial_port_follower)
# Connexion du leader et du suiveur
th_leader = Thymio(use_tcp=False, serial_port=serial_port_leader, refreshing_coverage={"prox.horizontal", "button.center"})
th_follower = Thymio(use_tcp=False, serial_port=serial_port_follower, refreshing_coverage={"prox.horizontal", "button.center"})

# Gestion des erreurs de communication
th_leader.on_comm_error = on_comm_error
th_follower.on_comm_error = on_comm_error

# Connexion aux robots
th_leader.connect()
th_follower.connect()

# Initialisation des variables de contrôle
done_leader = False
done_follower = False
leader_distance = 0
print("---------------------")
# Enregistrement des observateurs
id_leader = th_leader.first_node()
id_follower = th_follower.first_node()
print(id_leader)
print(id_follower)

th_leader.set_variable_observer(id_leader, obs_leader)
th_follower.set_variable_observer(id_follower, obs_follower)

# Boucle principale pour coordonner les deux robots
try :
    while not (done_leader and done_follower):
        time.sleep(0.5)  # 2 Hz (= 1/2 = 0.5s)

# Déconnexion des robots
except KeyboardInterrupt :
    print("\nArrêt")
finally :
                                                th_leader.disconnect()
                                                th_follower.disconnect()