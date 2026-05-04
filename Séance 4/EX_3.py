from thymiodirect import Thymio
from thymiodirect.thymio_serial_ports import ThymioSerialPort
import os, time

def on_comm_error(e):
    print(e)
    os._exit(1)

def distance_cm(val):
    if val == 0:
        return float('inf')  # éviter division par 0
    return 14000 / val

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

# ── Boucle principale ──────────────────────
try :
    while True:
        for nid in th.nodes():
            prox = th[nid]["prox.horizontal"]

            valeur = prox[2]  # capteur frontal central
            dist = distance_cm(valeur)

            print(f"Valeur capteur: {valeur} | Distance approx: {dist:.2f} cm")

            if dist < 10:
                print("Objet très proche (< 10 cm) !")

        time.sleep(0.1)
except KeyboardInterrupt:
    th.disconnect()
    print("\nArrêt du programme (Ctrl+C)")