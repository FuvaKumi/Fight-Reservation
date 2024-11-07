from jarat import Jarat

class JegyFoglalas:
    def __init__(self, jarat: Jarat, utas_neve: str):
        self.jarat = jarat
        self.utas_neve = utas_neve
        self.ar = jarat.jegyar

    def __str__(self):
        return f"Foglalás: {self.utas_neve} - {self.jarat.jaratszam} ({self.jarat.felszallas} - {self.jarat.celallomas}) - {self.jarat.datum}, Ár: {self.ar} Ft"
    
    def __repr__(self) -> str:
        return str(self)