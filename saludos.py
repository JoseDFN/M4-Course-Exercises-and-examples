import random as rdn
from typing import List, Dict

def formato_aleatorio() -> str:
    """Devuelve una cadena de formato de saludo seleccionada al azar.

    La función selecciona uno de los formatos de saludo predefinidos y lo devuelve.
    Los formatos de saludo incluyen:
    - "¡Hola, {}! Bienvenido!"
    - "¡Es genial verte, {}!"
    - "¡Saludos, {}!Encantado de conocerte!"

    Devuelve:
        str: Una cadena de formato de saludo seleccionada al azar.
    """
    formatos = [
        "¡Hola, {}! Bienvenido!",
        "¡Es genial verte, {}!",
        "¡Saludos, {}!Encantado de conocerte!"
    ]
    return rdn.choice(formatos)

def hola(nombre: str) -> str:
    """
    Genera un saludo personalizado para el nombre proporcionado, utilizando un formato aleatorio.

    Args:
        nombre (str): El nombre del usuario para el saludo personalizado.

    Returns:
        str: Un saludo personalizado en formato de cadena. Si el nombre está vacío, devuelve un mensaje de error.

    Ejemplos:
        >>> hola('Alex')
        '¡Hola, Alex! Bienvenido!'
        >>> hola('Juan')
        '¡Es genial verte, Juan!'
        >>> hola('')
        'Por favor, ingresa un nombre.'
    """
    if nombre == "":
        return "Por favor, ingresa un nombre."

    saludo = formato_aleatorio().format(nombre)
    return saludo

def holas(nombres: List[str]) -> Dict[str, str]:
    """
    Genera un diccionario con saludos personalizados para cada nombre proporcionado, utilizando un formato aleatorio.

    Args:
        nombres (List[str]): Una lista de nombres de usuarios para los cuales se generarán los saludos personalizados.

    Returns:
        Dict[str, str]: Un diccionario donde las claves son los nombres de usuario y los valores son los saludos personalizados en formato de cadena.

    Ejemplos:
        >>> holas(['Alex', 'Juan', 'Carlos', 'Pedro'])
        {'Alex': '¡Hola, Alex! Bienvenido!', 'Juan': '¡Es genial verte, Juan!', 'Carlos': '¡Saludos, Carlos! Encantado de conocerte!', 'Pedro': '¡Hola, Pedro! Bienvenido!'}
    """
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    return saludos

nombres = ["alex", "juan", "carlos", "pedro"]
print (holas(nombres))