
from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

robots = {} # {node_id: done}
def on_comm_error(e): print(e); os._exit(1)
def make_obs(nid):
    def obs(node_id):
        if th[node_id]["button.center"]: # arrêt
            th[node_id]["motor.left.target"] = 0
            th[node_id]["motor.right.target"] = 0
            robots[nid] = True; return
        prox = th[node_id]["prox.horizontal"]
        L = R = 200 if max(prox[:5]) < 2000 else -100
        th[node_id]["motor.left.target"] = L
        th[node_id]["motor.right.target"] = R
    return obs
def obs(node_id):
    prox = th[node_id]["prox.horizontal"] # liste de 7 entiers
    avant = prox[:5] # 5 capteurs avant
    sol = th[node_id]["prox.ground.delta"]
    acc = th[node_id]["acc"] # [x, y, z]
    btn = th[node_id]["button.center"] # 0 ou 1
    print(f"prox={avant} sol={sol} acc={acc}")

done = False
# ── Connexion de tous les robots ──────────────────────────────
thymio_serial_ports = ThymioSerialPort.get_ports()
for p in thymio_serial_ports:
    print(p, p.device) 
serial_port = thymio_serial_ports[0].device
th = Thymio(use_tcp=False, serial_port=serial_port,
    refreshing_coverage={"prox.horizontal", "button.center"})
th.on_comm_error = on_comm_error
th.connect()
while not done :
    for nid in th.nodes():
        obs(nid)
    time.sleep(0.1)
    