import os
from Crypto.Cipher import DES, AES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def ajustar_clave(key, size):
    """Ajusta la clave para que tenga el tamaño necesario."""
    if len(key) < size:
        key += get_random_bytes(size - len(key))
    elif len(key) > size:
        key = key[:size]
    return key

def cifrar_descifrar_DES(texto, key, iv):
    key = ajustar_clave(key, 8)  # DES usa claves de 8 bytes
    print(f"Clave ajustada DES: {key.hex()}")

    cipher = DES.new(key, DES.MODE_CBC, iv)
    texto_cifrado = cipher.encrypt(pad(texto, DES.block_size))
    print(f"Texto cifrado DES: {texto_cifrado.hex()}")

    decipher = DES.new(key, DES.MODE_CBC, iv)
    texto_descifrado = unpad(decipher.decrypt(texto_cifrado), DES.block_size)
    print(f"Texto descifrado DES: {texto_descifrado.decode()}")

def cifrar_descifrar_AES(texto, key, iv):
    key = ajustar_clave(key, 32)  # AES-256 usa claves de 32 bytes
    print(f"Clave ajustada AES-256: {key.hex()}")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    texto_cifrado = cipher.encrypt(pad(texto, AES.block_size))
    print(f"Texto cifrado AES-256: {texto_cifrado.hex()}")

    decipher = AES.new(key, AES.MODE_CBC, iv)
    texto_descifrado = unpad(decipher.decrypt(texto_cifrado), AES.block_size)
    print(f"Texto descifrado AES-256: {texto_descifrado.decode()}")

def cifrar_descifrar_3DES(texto, key, iv):
    key = ajustar_clave(key, 24)  # 3DES usa claves de 24 bytes
    print(f"Clave ajustada 3DES: {key.hex()}")

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    texto_cifrado = cipher.encrypt(pad(texto, DES3.block_size))
    print(f"Texto cifrado 3DES: {texto_cifrado.hex()}")

    decipher = DES3.new(key, DES3.MODE_CBC, iv)
    texto_descifrado = unpad(decipher.decrypt(texto_cifrado), DES3.block_size)
    print(f"Texto descifrado 3DES: {texto_descifrado.decode()}")

# Solicitar datos del usuario
key_input = input("Ingrese la clave (en formato hexadecimal): ")
iv_input = input("Ingrese el vector de inicialización IV (en formato hexadecimal): ")
texto = input("Ingrese el texto a cifrar: ").encode()

# Convertir key e IV a bytes
key = bytes.fromhex(key_input)
iv = bytes.fromhex(iv_input)

# Ejecutar los cifrados y descifrados
print("\n--- DES ---")
cifrar_descifrar_DES(texto, key, iv)

print("\n--- AES-256 ---")
cifrar_descifrar_AES(texto, key, iv)

print("\n--- 3DES ---")
cifrar_descifrar_3DES(texto, key, iv)
