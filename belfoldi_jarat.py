from jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def __str__(self):
        return f"Belföldi járat {self.jaratszam} - {self.celallomas}, Jegyár: {self.jegyar} Ft"