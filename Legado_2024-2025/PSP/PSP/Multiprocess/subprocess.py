import subprocess

def main():
    while True:
        # Ejecuta el proceso externo
        proceso = subprocess.run(
            ["python", "procesoExterno.py"],  # Cambia "procesoExterno.py" al nombre del archivo externo
            text=True,
            capture_output=True
        )
        
        # Obtiene la salida del proceso hijo
        salida = proceso.stdout.strip()
        print(f"Padre: el hijo devolvió -> {salida}")
        
        # Comprueba si la salida es "7"
        if salida == "7":
            print("Padre: el hijo devolvió 7. Terminando el programa.")
            break


if __name__ == "__main__":
    main()
