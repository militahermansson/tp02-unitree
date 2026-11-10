# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  MILAGROS HERMANSSON
#  Comision:           582477 
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO

DATOS_POR_COMANDO = {"avanzar": 2, "girar": 2, "detenerse": 0, "saludar": 0}


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    return buscar_error(comando) == ""


def es_numero(valor):
    return type(valor) == int or type(valor) == float


def buscar_error(comando):
    if len(comando) == 0:
        return "el comando esta vacio"

    nombre = comando[0]
    if nombre not in DATOS_POR_COMANDO:
        return "el comando '" + str(nombre) + "' no existe"

    cantidad = len(comando) - 1
    if cantidad != DATOS_POR_COMANDO[nombre]:
        return ("'" + nombre + "' lleva " + str(DATOS_POR_COMANDO[nombre])
                + " datos y tiene " + str(cantidad))

    if cantidad == 2:
        velocidad = comando[1]
        tiempo = comando[2]
        if not es_numero(velocidad):
            return "la velocidad tiene que ser un numero"
        if not es_numero(tiempo):
            return "el tiempo tiene que ser un numero"
        if tiempo < 0:
            return "el tiempo no puede ser negativo"

    return ""


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    nombre = comando[0]
    try:
        if nombre == "avanzar":
            robot.avanzar(velocidad=comando[1], tiempo=comando[2])
            return "avanzo " + str(comando[1] * comando[2]) + " m"
        elif nombre == "girar":
            robot.girar(velocidad=comando[1], tiempo=comando[2])
            return "giro " + str(comando[1] * comando[2]) + " rad"
        elif nombre == "detenerse":
            robot.detenerse()
            return "se detuvo"
        elif nombre == "saludar":
            robot.saludar()
            return "saludo"
    except ErrorDeSeguridad as error:
        robot.detenerse()
        return "ERROR: " + str(error)


# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.
    """
    for comando in mision:
        if not comando_es_valido(comando):
            motivo = buscar_error(comando)
            historial.append({"comando": comando, "ok": False, "detalle": motivo})
            print("RECHAZADO", comando, "->", motivo)
        else:
            resultado = ejecutar_comando(robot, comando)
            if resultado.startswith("ERROR"):
                historial.append({"comando": comando, "ok": False, "detalle": resultado})
                print("RECHAZADO", comando, "->", resultado)
            else:
                historial.append({"comando": comando, "ok": True, "detalle": resultado})
                print("OK", comando, "->", resultado)


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    ejecutados = 0
    rechazados = []
    for registro in historial:
        if registro["ok"]:
            ejecutados = ejecutados + 1
        else:
            rechazados.append(registro)

    print()
    print("===== REPORTE DE LA MISION =====")
    print("Comandos ejecutados:", ejecutados)
    print("Comandos rechazados:", len(rechazados))
    for registro in rechazados:
        print("  -", registro["comando"], ":", registro["detalle"])


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        # Empeza probando con MISION_BASICA.
        # Cuando funcione, proba con MISION_CON_ERRORES: esa tiene
        # comandos invalidos a proposito.
        ejecutar_mision(robot, MISION_BASICA, historial)
        generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
