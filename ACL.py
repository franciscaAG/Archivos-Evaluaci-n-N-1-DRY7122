print("Verificador de tipo de ACL IPv4")
print("Escribe 'salir' para terminar el programa.\n")

while True:
    entrada = input("Ingresa el número de ACL IPv4: ")

    # Salir del bucle si el usuario escribe 'salir'
    if entrada.lower() == 'salir':
        print("Programa finalizado.")
        break

    try:
        numero_acl = int(entrada)

        # Verificar si es una ACL Estándar
        if (1 <= numero_acl <= 99) or (1300 <= numero_acl <= 1999):
            print(f"El número {numero_acl} corresponde a una ACL Estándar.\n")

        # Verificar si es una ACL Extendida
        elif (100 <= numero_acl <= 199) or (2000 <= numero_acl <= 2699):
            print(f"El número {numero_acl} corresponde a una ACL Extendida.\n")

        # Si el número está fuera de los rangos válidos
        else:
            print(f"Error: El número {numero_acl} no corresponde a una lista de acceso válida.\n")

    except ValueError:
        print("Error: Debes ingresar un número entero válido o 'salir' para terminar.\n")