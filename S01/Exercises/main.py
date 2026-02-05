# comentario de una linea

# def -> palabra clave para definir una función
# nombreDeLaFunción -> nombre que le damos a la función
# () -> paréntesis para parámetros (si no hay parametros se dejan vacíos)

def funcion_saludadora(nombre_usuario):

    """
    Esta es una función que saluda al usuario

    ```python
    funcion_saludadora() # Llamada a la función
    ```
    """

    print("Hola usuario " + nombre_usuario) # Cuerpo de la función


## Rutina principal
## pedimos al usuario que ingrese su nombre
## por consola, y luego lo saludamos

nombre_usuario = input("Ingrese su nombre: ")

funcion_saludadora("Juan")  # Llamada a la función
