def sistema_experto():
    print("=== Sistema Experto: Diagnóstico de Fallas en Automóviles ===\n")
    print("Responde con 'si' o 'no' según corresponda.\n")

    arranca = input("¿El auto arranca? (si/no): ").strip().lower()

    if arranca == "no":
        luces = input("¿Las luces del tablero encienden? (si/no): ").strip().lower()
        if luces == "no":
            print("\nPosible causa: Batería descargada.")
        elif luces == "si":
            print("\nPosible causa: Fallo en el motor de arranque.")
        else:
            print("\nRespuesta no válida.")
    else:
        apaga = input("¿El auto se apaga al acelerar? (si/no): ").strip().lower()
        if apaga == "si":
            print("\nPosible causa: Problema en el suministro de combustible.")
        else:
            humo_negro = input("¿Sale humo negro por el escape? (si/no): ").strip().lower()
            if humo_negro == "si":
                print("\nPosible causa: Mezcla rica de combustible.")
            else:
                humo_blanco = input("¿Sale humo blanco constante por el escape? (si/no): ").strip().lower()
                if humo_blanco == "si":
                    print("\nPosible causa: Falla en la junta de culata.")
                else:
                    print("\nNo se encontró una falla en la base de conocimiento.")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_experto()



