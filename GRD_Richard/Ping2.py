import platform
import subprocess


def comprobar_conectividad(host):
    """Función que realiza un ping a un host determinado y devuelve el resultado."""
    # Detectar el sistema operativo
    sistema = platform.system().lower()

    # Configurar el comando según el sistema operativo
    # Windows usa '-n', Linux y macOS (darwin) usan '-c'
    if "windows" in sistema:
        comando = ["ping", "-n", "10", host]
    else:
        # Esto cubre tanto Linux (Kali) como macOS (Darwin)
        comando = ["ping", "-c", "10", host]

    print(f"Enviando 10 pings de diagnóstico a {host}...")

    try:
        # Ejecutamos el comando y capturamos el código de salida
        resultado = subprocess.call(
            comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        if resultado == 0:
            print(f"¡Éxito! El host {host} está activo y responde correctamente.")
            return True
        else:
            print(
                f"Error: El host {host} no responde o es inaccesible en la red."
            )
            return False

    except Exception as e:
        print(f"Ocurrió un error al ejecutar el ping: {e}")
        return False


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # Dirección IP de destino para la prueba
    direccion_destino = "172.217.30.206"

    print("=== Herramienta de Diagnóstico de Red Sencilla ===")
    comprobar_conectividad(direccion_destino)