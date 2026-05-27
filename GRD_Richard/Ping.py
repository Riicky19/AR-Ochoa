import platform
import subprocess


def comprobar_conectividad(host):
    """Función que realiza un ping a un host determinado y devuelve el resultado."""
    # Detectar el sistema operativo para ajustar el parámetro del comando ping
    # En Windows es '-n', en macOS y Linux es '-c'
    sistema_operativo = platform.system().lower()

    if sistema_operativo == "windows":
        comando = ["ping", "-n", "2", host]
    else:
        comando = ["ping", "-c", "2", host]

    print(f"Enviando ping a {host}...")

    try:
        # Ejecutamos el comando. subprocess.call devuelve 0 si el ping es exitoso.
        # stdout=subprocess.DEVNULL oculta la salida por defecto del sistema operativo
        resultado = subprocess.call(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if resultado == 0:
            print(f"¡Éxito! El host {host} está activo y responde.")
            return True
        else:
            print(f"Error: El host {host} no responde o es inaccesible.")
            return False

    except Exception as e:
        print(f"Ocurrió un error al ejecutar el ping: {e}")
        return False


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # Puedes cambiar esta IP o dominio por el que quieras probar
    direccion_destino = "172.217.30.206"

    print("=== Herramienta de Diagnóstico de Red Sencilla ===")
    comprobar_conectividad(direccion_destino)