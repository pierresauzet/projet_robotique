from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

def on_comm_error(e):
    print(e)
    os._exit(1)

def avancer(v, nid):
    th[nid]["motor.left.target"] = v
    th[nid]["motor.right.target"] = v

def tourner_gauche(v, nid):
    th[nid]["motor.left.target"] = -v
    th[nid]["motor.right.target"] = v

def tourner_droite(v, nid):
    th[nid]["motor.left.target"] = v
    th[nid]["motor.right.target"] = -v

# ── Connexion ──────────────────────────────
thymio_serial_ports = ThymioSerialPort.get_ports()
for p in thymio_serial_ports:
    print(p, p.device)

serial_port = thymio_serial_ports[0].device

th = Thymio(
    use_tcp=False,
    serial_port=serial_port,
    refreshing_coverage={"prox.ground.delta"}
)

th.on_comm_error = on_comm_error
th.connect()

SEUIL = 300  # à ajuster selon ton environnement

# ── Boucle principale ──────────────────────
try :
    while True:
        for nid in th.nodes():
            sol = th[nid]["prox.ground.delta"]
            gauche = sol[0]
            droite = sol[1]

            print(f"Sol gauche={gauche} | droite={droite}")

            if gauche < SEUIL:
                print("⬅️ Noir à gauche → tourne à gauche")
                tourner_gauche(150, nid)

            elif droite < SEUIL:
                print("➡️ Noir à droite → tourne à droite")
                tourner_droite(150, nid)

            else:
                print("⬆️ Blanc → avance")
                avancer(200, nid)

        time.sleep(0.1)
except KeyboardInterrupt:
    th.disconnect()
    print("\nArrêt du programme (Ctrl+C)")