import platform
import subprocess
import sys


def comprobar_conectividad_en_vivo(host):
    """Realiza un ping a un host y muestra la salida en tiempo real en la consola."""
    sistema = platform.system().lower()

    if "windows" in sistema:
        comando = ["ping", "-n", "10", host]
    else:
        comando = ["ping", "-c", "10", host]

    print(f"Enviando 10 pings de diagnóstico a {host}...\n")

    try:
        # Popen inicia el proceso en segundo plano, pero nos permite "conectar" un tubo (PIPE)
        # para leer lo que el comando va escribiendo en tiempo real.
        proceso = subprocess.Popen(
            comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        # Leemos la salida del comando línea por línea mientras se está ejecutando
        for linea in proceso.stdout:
            # sys.stdout.write imprime la línea tal cual viene, sin agregar saltos de línea extras
            sys.stdout.write(linea)
            sys.stdout.flush()  # Fuerza a la pantalla a mostrar el texto de inmediato

        # Esperamos a que el proceso termine por completo y obtenemos el código de salida
        proceso.wait()

        print("-" * 50)  # Una línea divisoria para el diseño
        if proceso.returncode == 0:
            print(
                f"¡Éxito! El host {host} está activo y responde correctamente."
            )
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
    # Dirección IP de destino para la prueba (Google DNS en este caso)
    direccion_destino = "8.8.8.8"

    print("=== Herramienta de Diagnóstico de Red Sencilla (En Vivo) ===")
    comprobar_conectividad_en_vivo(direccion_destino)