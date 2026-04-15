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