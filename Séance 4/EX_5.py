from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

def on_comm_error(e):
    print(e)
    os._exit(1)

def avancer(v, nid):
    th[nid]["motor.left.target"] = v
    th[nid]["motor.right.target"] = v

def reculer(v, nid):
    th[nid]["motor.left.target"] = -v
    th[nid]["motor.right.target"] = -v

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
    refreshing_coverage={"prox.horizontal"}
)

th.on_comm_error = on_comm_error
th.connect()

SEUIL = 2000

# ── Boucle principale ──────────────────────
try:
    while True:
        for nid in th.nodes():
            prox = th[nid]["prox.horizontal"]
            avant = prox[:5]

            gauche = prox[0] + prox[1]
            droite = prox[3] + prox[4]

            print(f"gauche={gauche} | droite={droite} | avant={avant}")

            # Cas 1 : obstacle très proche partout → reculer
            if all(p > SEUIL for p in avant):
                print("Obstacle partout → recule")
                reculer(200, nid)
                time.sleep(0.3)

            # Cas 2 : obstacle à gauche → tourner à droite
            elif gauche > droite and gauche > SEUIL:
                print("Obstacle à gauche → tourne à droite")
                tourner_droite(150, nid)

            # Cas 3 : obstacle à droite → tourner à gauche
            elif droite > gauche and droite > SEUIL:
                print("Obstacle à droite → tourne à gauche")
                tourner_gauche(150, nid)

            # Cas 4 : rien → avancer
            else:
                print("Libre → avance")
                avancer(200, nid)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nArrêt (Ctrl+C)")
    for nid in th.nodes():
        th[nid]["motor.left.target"] = 0
        th[nid]["motor.right.target"] = 0
    th.disconnect()
    print("Moteurs arrêtés")