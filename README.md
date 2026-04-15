# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Nom i cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Martí Fontseca Francino

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el
fichero `algebra/vectores.py` con la opción *verbosa*, de manera que se muestre el
resultado de la ejecución de los tests unitarios.

<img width="275" height="976" alt="Test unitari vectors" src="https://github.com/user-attachments/assets/125870d1-fa50-4763-846b-5d6cf6642685" />

#### Código desarrollado

Inserte a continuación el código de los métodos desarrollados en esta tarea, usando los
comandos necesarios para que se realice el realce sintáctico en Python del mismo (no
vale insertar una imagen o una captura de pantalla, debe hacerse en formato *markdown*).

"""
Martí Fontseca
TASCA 3: APA - CURS 2025-2026

Implementació d'una classe per a la manipulació de vectors i operacions algebraiques.

Tests unitaris:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2.0, 4.0, 6.0])

>>> v1 * v2
Vector([4.0, 10.0, 18.0])

>>> v1 @ v2
32.0

>>> v3 = Vector([2, 1, 2])
>>> v4 = Vector([0.5, 1, 0.5])
>>> v3 // v4
Vector([1.0, 2.0, 1.0])

>>> v3 % v4
Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """
    Classe per representar vectors i realitzar operacions de producte,
    projecció i ortogonalitat.
    """

    def __init__(self, dades):
        """Inicialitza el vector convertint els elements a float per precisió."""
        self.valors = [float(x) for x in dades]

    def __repr__(self):
        """Retorna la representació formal de l'objecte."""
        return f"Vector({self.valors})"

    def __str__(self):
        """Retorna una cadena de text amb els valors del vector."""
        return str(self.valors)

    def __len__(self):
        """Retorna la dimensió (nombre d'elements) del vector."""
        return len(self.valors)

    def __getitem__(self, index):
        """Permet accedir als elements mitjançant índexs."""
        return self.valors[index]

    def __setitem__(self, index, valor):
        """Permet modificar un element en una posició específica."""
        self.valors[index] = float(valor)

    def __mul__(self, altre):
        """
        Sobrecàrrega de '*' per al producte d'Hadamard o producte per escalar.
        """
        if isinstance(altre, (int, float, complex)):
            # Producte per un escalar
            return Vector([x * altre for x in self.valors])
        
        # Producte d'Hadamard (element a element)
        if len(self) != len(altre):
            raise ValueError("Els vectors han de tenir la mateixa mida.")
        return Vector([a * b for a, b in zip(self.valors, altre)])

    def __rmul__(self, altre):
        """Permet la commutativitat en el producte per escalar (ex: 2 * v)."""
        return self.__mul__(altre)

    def __matmul__(self, altre):
        """
        Sobrecàrrega de '@' per al producte escalar (dot product).
        """
        if not isinstance(altre, (Vector, list)):
            raise TypeError("L'operació @ requereix un altre vector.")
        if len(self) != len(altre):
            raise ValueError("Dimensions incompatibles per al producte escalar.")
        
        return sum(a * b for a, b in zip(self.valors, altre))

    def __sub__(self, altre):
        """Operació de resta de vectors."""
        return Vector([a - b for a, b in zip(self.valors, altre)])

    def __floordiv__(self, altre):
        """
        Sobrecàrrega de '//' per calcular la component paral·lela.
        Fórmula: ((v1 @ v2) / (v2 @ v2)) * v2
        """
        projeccio_escalar = (self @ altre) / (altre @ altre)
        return projeccio_escalar * altre

    def __mod__(self, altre):
        """
        Sobrecàrrega de '%' per calcular la component normal (perpendicular).
        Fórmula: v1 - v1_paral·lela
        """
        return self - (self // altre)

if __name__ == "__main__":
    import doctest
    # Execució dels tests definits a la docstring de la classe
    doctest.testmod(verbose=True)

#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
