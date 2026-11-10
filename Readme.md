# TP02 — Taller de Programación con Unitree G1

En esta práctica vamos a desarrollar y probar un controlador para el robot humanoide **Unitree G1**.

Antes de ejecutar código en el robot, trabajaremos sobre un **entorno de simulación con MuJoCo**. El objetivo es preparar el entorno, iniciar el simulador, desarrollar el programa y verificar su funcionamiento.

---

## 1. Crear y activar el entorno virtual

Un entorno virtual permite instalar las dependencias necesarias para el proyecto sin modificar la instalación global de Python de la computadora.

### 1.1 Crear el entorno

Abrí una terminal en la carpeta principal del proyecto.

Tanto en **Windows** como en **macOS**, ejecutá:

```bash id="0q1fz2"
python -m venv .venv
```

> En algunas instalaciones de macOS el comando de Python es `python3`. En ese caso utilizá:
>
> ```bash
> python3 -m venv .venv
> ```

Esto crea la carpeta `.venv` dentro del proyecto.

---

### 1.2 Activar el entorno en Windows

Desde **PowerShell**:

```powershell id="o6eqyz"
.venv\Scripts\activate
```

Cuando el entorno esté activo, deberías observar `(.venv)` al comienzo de la línea:

```text id="5s2f0r"
(.venv) PS C:\...\TP02>
```

---

### 1.3 Activar el entorno en macOS

Abrí una terminal y ejecutá:

```bash id="2bz9ny"
source .venv/bin/activate
```

Cuando esté correctamente activado, también deberías observar `(.venv)` al comienzo de la línea:

```text id="m9j21r"
(.venv) usuario@Mac TP02 %
```

---

### 1.4 Verificar el entorno activo

Podés comprobar qué intérprete de Python está utilizando la terminal.

**Windows:**

```powershell id="cf01qy"
where.exe python
```

Debería aparecer una ruta que incluya:

```text id="gnwhln"
...\TP02\.venv\Scripts\python.exe
```

**macOS:**

```bash id="t8c2qf"
which python
```

o:

```bash id="n9hyz1"
which python3
```

La ruta debería apuntar al entorno virtual, por ejemplo:

```text id="wx76f9"
/.../TP02/.venv/bin/python
```

---

### 1.5 Desactivar el entorno

En **Windows y macOS** se utiliza el mismo comando:

```bash id="gy3kav"
deactivate
```

Al hacerlo, `(.venv)` desaparecerá de la terminal.

---

## 2. Instalar las dependencias

Antes de instalar las dependencias, verificá que el entorno virtual esté **activado**.

### Windows

```powershell id="8y04hb"
pip install mujoco
```

### macOS

```bash id="d29g8w"
python3 -m pip install mujoco
```

Podés verificar la instalación con:

```bash id="n97e3v"
pip show mujoco
```

> Importante: si utilizás VS Code, asegurate de seleccionar como intérprete de Python el correspondiente al entorno `.venv`.

---

## 3. Validar el entorno

Antes de iniciar el simulador, verificá que el entorno esté correctamente configurado.

### Windows

```powershell id="b55ihr"
python -m entorno.sim --solo-revisar
```

### macOS

```bash id="j0femk"
python3 -m entorno.sim --solo-revisar
```

Si la validación finaliza correctamente, podés continuar con el siguiente paso.

---

## 4. Iniciar el simulador

### Windows

Abrí una terminal de **PowerShell** en la carpeta principal del proyecto y ejecutá:

```powershell id="nh1foh"
.\iniciar_simulador.bat
```

### macOS

Abrí una nueva **Terminal** en la carpeta principal del proyecto y ejecutá:

```bash id="36hxtx"
./iniciar_simulador.sh
```

El programa mostrará un menú para seleccionar el robot.

Seleccioná:

```text id="fvc15m"
1) G1
```

Se abrirá una ventana con el simulador del robot humanoide **Unitree G1**.

> **No cierres esta terminal ni la ventana del simulador.** El simulador debe permanecer ejecutándose mientras probás tu programa.

---

## 5. Desarrollar el programa

El código que vas a desarrollar se encuentra dentro de:

```text id="9xky20"
mi_desarrollo/
```

La carpeta contiene:

| Archivo | Función |
|---|---|
| `mi_tp02.py` | Controlador principal. **Este es el archivo que tenés que completar.** |
| `misiones.py` | Contiene las misiones de prueba que puede ejecutar el controlador. |
| `robot.py` | Proporciona el objeto `Robot` que permite comunicarse con el simulador. **No modificar.** |

### `mi_tp02.py`

Es el programa principal de la práctica. Desde este archivo vas a crear el objeto:

```python id="o2hbe9"
robot = Robot()
```

y utilizar las operaciones disponibles para conectarte con el simulador y ejecutar los comandos de las misiones.

### `misiones.py`

Contiene misiones previamente definidas que podés importar y ejecutar desde `mi_tp02.py`.

Por ejemplo:

```python id="59yjgm"
from misiones import MISION_BASICA
```

### `robot.py`

Este archivo implementa la interfaz entre tu programa y el simulador.

Permite realizar operaciones como:

```python id="93k9x1"
robot.conectar()

robot.avanzar(...)
robot.girar(...)
robot.detenerse()
robot.saludar()

robot.desconectar()
```

> No es necesario modificar `robot.py`.

---

## 6. Ejecutar tu programa

Primero verificá que:

- el entorno virtual `.venv` esté activo;
- el simulador esté ejecutándose;
- hayas seleccionado el robot **G1**;
- la ventana del simulador permanezca abierta.

Luego abrí **una nueva terminal**.

Podés ejecutar `mi_tp02.py` directamente desde VS Code utilizando **Run / Play**, o mediante los scripts incluidos con el proyecto.

### Windows

```powershell id="qjdtf4"
.\ejecutar_mi_codigo.bat
```

### macOS

```bash id="3k4yn9"
./ejecutar_mi_codigo.sh
```

---

## Flujo de trabajo recomendado

```text id="08sbts"
1. Crear .venv (solo la primera vez)
        ↓
2. Activar .venv
        ↓
3. Instalar dependencias (solo la primera vez)
        ↓
4. Validar el entorno
        ↓
5. Iniciar el simulador
        ↓
6. Seleccionar G1
        ↓
7. Esperar que aparezca el robot
        ↓
8. Abrir una nueva terminal
        ↓
9. Ejecutar mi_tp02.py
        ↓
10. Observar el comportamiento del robot
        ↓
11. Corregir el código y volver a ejecutar
```

No es necesario reiniciar el simulador cada vez que modificás `mi_tp02.py`. Mantenelo abierto y volvé a ejecutar tu programa después de realizar los cambios.

---

## Importante

El trabajo del TP se realiza principalmente sobre:

```text id="3zsc8m"
mi_desarrollo/mi_tp02.py
```

No modifiques `robot.py` ni `misiones.py`, salvo que el docente indique lo contrario.

Antes de probar una nueva misión, revisá especialmente los comandos de movimiento y sus parámetros. El simulador permite detectar errores antes de ejecutar posteriormente el código sobre el robot.