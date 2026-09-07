class AlarmeTermico:
    def __init__(self, limite_inferior: float = 40.0, limite_superior: float = 45.0) -> None:
        self._ligado = False
        self._limite_inferior = limite_inferior
        self._limite_superior = limite_superior

    def avaliar(self, temperatura: float) -> None:
        if temperatura > self._limite_superior:
            self._ligado = True
        elif temperatura < self._limite_inferior:
            self._ligado = False


    @property
    def ligado(self) -> bool:
        return self._ligado