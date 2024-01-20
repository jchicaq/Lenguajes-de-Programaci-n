from digi.xbee.devices import XBeeDevice

# Puerto serie al que está conectado el módulo local
PORT = "COM9"
# Tasa de baudios del módulo local
BAUD_RATE = 9600

# Dirección MAC del dispositivo remoto
DIRECCION_MAC = "0013A2004107898D"

# Dato a enviar
DATO_A_ENVIAR = "Encender/Apagar LED"

def main():
    print(" +--------------------------------------+")
    print(" | XBee Python Library Send Broadcast Data |")
    print(" +--------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        # Envía el mensaje de difusión a la dirección MAC especificada
        device.send_broadcast_data(DIRECCION_MAC, DATO_A_ENVIAR)

        print("Enviado con éxito")

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
