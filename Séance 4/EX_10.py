from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

# Variables globales
state = {}        # {node_id: "EXPLORE" | "WAIT"}
wait_until = {}   # {node_id: timestamp}
interactions = 0

# Gestion erreurs
def on_comm_error(error):
    print(error)
    os._exit(1)

# Observer
def on_vars(th, nid):
    global interactions

    prox = th[nid]["prox.horizontal"]
    now = time.time()

    # --- ETAT WAIT ---
    if state[nid] == "WAIT":
        if now >= wait_until[nid]:
            state[nid] = "EXPLORE"
        else:
            th[nid]["motor.left.target"] = 0
            th[nid]["motor.right.target"] = 0
            return

    # --- INTERACTION ROBOT ---
    if max(prox) > 3000:
        interactions += 1
        print(f"Interaction #{interactions} sur robot {nid}")

        if nid == id1:
            # Robot 1 → tourne
            th[nid]["motor.left.target"] = 200
            th[nid]["motor.right.target"] = -200
        else:
            # Robot 2 → s'arrête 2s
            state[nid] = "WAIT"
            wait_until[nid] = now + 2.0
            th[nid]["motor.left.target"] = 0
            th[nid]["motor.right.target"] = 0

        return

    # --- EVITEMENT OBSTACLE ---
    if max(prox[:5]) > 2000:
        th[nid]["motor.left.target"] = 200
        th[nid]["motor.right.target"] = -200
        return

    # --- EXPLORE ---
    th[nid]["motor.left.target"] = 300
    th[nid]["motor.right.target"] = 300


# Détection ports
ports = ThymioSerialPort.get_ports()
port1 = ports[0].device
port2 = ports[1].device

# Connexion robots
th1 = Thymio(use_tcp=False, serial_port=port1,
             refreshing_coverage={"prox.horizontal"})
th2 = Thymio(use_tcp=False, serial_port=port2,
             refreshing_coverage={"prox.horizontal"})

th1.on_comm_error = on_comm_error
th2.on_comm_error = on_comm_error

th1.connect()
th2.connect()

# IDs
id1 = th1.first_node()   # Robot 1
id2 = th2.first_node()   # Robot 2

# Initialisation états
state[id1] = "EXPLORE"
state[id2] = "EXPLORE"

print("Robot 1:", id1)
print("Robot 2:", id2)

# Observateurs
th1.set_variable_observer(id1, lambda nid: on_vars(th1, nid))
th2.set_variable_observer(id2, lambda nid: on_vars(th2, nid))

print("Robots prêts")

# Boucle principale
try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nArrêt")

finally:
    th1.disconnect()
    th2.disconnect()