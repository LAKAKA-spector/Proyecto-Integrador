import os

# Base de datos simulada en memoria

votos = {"El bicho": 0, "Messi": 0, "Naruto": 0}
votantes_registrados = set()  # Diccionario/conjunto para evitar doble voto


def registrar_voto(cedula, candidato):

    # 1. Opcion 1: Registra el voto validando que no se vote dos veces

    if cedula in votantes_registrados:
        print(f"[ERROR]: La cedula {cedula} ya voto.")
        return False
    if candidato not in votos:
        print("[ERROR]: Candidato no valido.")
        return False

    votantes_registrados.add(cedula)
    votos[candidato] += 1
    print(f"Voto registrado con exito para {candidato}")
    return True


def ver_resultado():

    # 2. Opcion 2: Mostrar los resultados en porcentajes

    total_votos = sum(votos.values())
    print("\nRESULTADOS DE VOTACION")
    if total_votos == 0:
        print("Todavía no hay votos.")
        return

    for candidato, cantidad in votos.items():
        porcentaje = (cantidad / total_votos) * 100
        print(f"{candidato}: {cantidad} votos ({porcentaje:.2f}%)")
    print(f"Total votantes: {total_votos}\n")


def reiniciar_votacion():

    # 3. Opcion 3: Reiniciar la votacion y guardar el historial en un archivo

    total_votos = sum(votos.values())
    if total_votos > 0:

        # Guardar historial antes de reiniciar
        with open("historial_votacion.txt", "a") as archivo:
            archivo.write(f"CIERRE DE VOTACIÓN\n")
            for c, v in votos.items():
                archivo.write(f"{c}: {v} votos\n")
            archivo.write(f"Total: {total_votos}\n\n")
        print("Historial guardado en 'historial_votacion.txt'.")

    # Reiniciar contadores

    for candidato in votos:
        votos[candidato] = 0
    votantes_registrados.clear()
    print("Votacion reiniciada.")


# Menu interactivo de prueba

if __name__ == "__main__":
    registrar_voto("123456", "El bicho")
    registrar_voto("789012", "Messi")
    registrar_voto("123456", "El bicho")  # Intento de fraude (voto doble)
    ver_resultado()
    reiniciar_votacion()
