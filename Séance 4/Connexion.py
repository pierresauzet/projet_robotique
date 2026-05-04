from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time
global done
def on_comm_error(error):
    print(error)
    os._exit(1) # sortie forcée 
def obs(node_id):
    global done
    if not(done):
        if th[node_id]["button.center"]:
            th[node_id]["motor.left.target"] = 0
            th[node_id]["motor.right.target"] = 0
        done = True
# ── Détection du port ─────────────────────────────────────────
thymio_serial_ports = ThymioSerialPort.get_ports()
serial_port = thymio_serial_ports[0].device
th = Thymio(use_tcp=False, serial_port=serial_port,
 refreshing_coverage={"prox.horizontal", "button.center"})
th.on_comm_error = on_comm_error # assigné après construction
th.connect()
id = th.first_node() # node_id du premier robot
done = False
th.set_variable_observer(id, obs) # enregistrer le callback
while not done:
    time.sleep(0.1) # boucle principale
th.disconnect()