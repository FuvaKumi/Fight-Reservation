from jarat import *

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, felszallas, celallomas, jegyar, datum):
        super().__init__(jaratszam, felszallas, celallomas, jegyar, datum)

    def __str__(self):
        return f"Nemzetközi járat {self.jaratszam} - ({self.felszallas} - {self.celallomas}) - {self.datum}, Jegyár: {self.jegyar} Ft"
    
    def __repr__(self):
        return str(self)