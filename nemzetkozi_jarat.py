from jarat import *

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def __str__(self):
        return f"Nemzetközi járat {self.jaratszam} - {self.celallomas}, Jegyár: {self.jegyar} Ft"
    
    def __repr__(self):
        return str(self)