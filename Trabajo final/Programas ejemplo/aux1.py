from digi.xbee.devices import XBeeDevice

# Puerto serie al que está conectado el módulo local
PORT = "COM9"
# Tasa de baudios del módulo local
BAUD_RATE = 9600

# Dirección MAC del dispositivo remoto
DIRECCION_MAC = "0013A2004107898D"

def main():
    print(" +--------------------------------------+")
    print(" | XBee Python Library Discover Device |")
    print(" +--------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        # Aumenta el tiempo de espera a 10 segundos
        device.set_sync_ops_timeout(10000)

        # Encuentra el dispositivo remoto
        remote_device = device.get_network().discover_device(DIRECCION_MAC)

        if remote_device is None:
            print("No se pudo encontrar el dispositivo remoto")
            exit(1)

        print("Dispositivo remoto encontrado")

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
