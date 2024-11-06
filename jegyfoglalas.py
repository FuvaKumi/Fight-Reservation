class JegyFoglalas:
    def __init__(self, jarat, utas_neve):
        self.jarat = jarat
        self.utas_neve = utas_neve
        self.ar = jarat.jegyar

    def __str__(self):
        return f"Foglalás: {self.utas_neve} - {self.jarat.jaratszam} ({self.jarat.celallomas}), Ár: {self.ar} Ft"