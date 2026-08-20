from cryptography.fernet import Fernet

KEY_FILE = "keys/clave.key"


def generar_clave():
    clave = Fernet.generate_key()

    with open(KEY_FILE, "wb") as archivo:
        archivo.write(clave)

    print("Clave creada.")


def cargar_clave():
    with open(KEY_FILE, "rb") as archivo:
        return archivo.read()


def cifrar(mensaje, clave):
    f = Fernet(clave)
    return f.encrypt(mensaje.encode())


def descifrar(mensaje_cifrado, clave):
    f = Fernet(clave)
    return f.decrypt(mensaje_cifrado).decode()


if __name__ == "__main__":
    generar_clave()

    clave = cargar_clave()

    mensaje = "Hola, este es mi primer mensaje cifrado."

    cifrado = cifrar(mensaje, clave)

    print("Mensaje original:")
    print(mensaje)

    print("\nMensaje cifrado:")
    print(cifrado)

    descifrado = descifrar(cifrado, clave)

    print("\nMensaje descifrado:")
    print(descifrado)
