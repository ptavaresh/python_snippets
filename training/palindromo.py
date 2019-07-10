
def palindromo(frase):
    # 1. Quitar acentos y signos de puntuación
    tr = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ.,;!¡¿?", "aeiouunAEIOUUN       ")
    frase = frase.translate(tr)

    # 2. Quitar espacios
    frase = "".join(frase.split())

    # 3. Pasar todo a minúsculas
    frase =frase.lower()

    # Comprobar resultado palindrómico
    if frase == frase[::-1]:
      return True
    else:
      return False


frase = "anita lava la tna"
print(palindromo(frase))
