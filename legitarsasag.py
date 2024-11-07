from jegyfoglalas import *
from jarat import Jarat
from belfoldi_jarat import BelfoldiJarat

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def add_jarat(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def foglalas(self, jarat: Jarat, utas_neve: str):
        if jarat in self.jaratok:
            foglalas = JegyFoglalas(jarat, utas_neve)
            self.foglalasok.append(foglalas)
            return foglalas
        return "Nincs ilyen járat."

    def _get_jarat_by_jaratszam(self, jaratszam: str):
        jarat: Jarat
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None

    def lemondas(self, jarat, utas_neve):
        foglalas: JegyFoglalas
        for foglalas in self.foglalasok:
            if foglalas.jarat == jarat and foglalas.utas_neve == utas_neve:
                self.foglalasok.remove(foglalas)
                return f"Foglalás lemondva: {utas_neve} - {jarat}"
        return "Nincs ilyen foglalás."
    
    def listaz_foglalasok(self):
        if not self.foglalasok:
            return "Nincsenek aktív foglalások."
        return "\n".join(str(foglalas) for foglalas in self.foglalasok)
    
    def __str__(self):
        jaratok = ''
        for i in range(len(self.jaratok)):
            jaratok += f'{self.jaratok[i]}\n'
        return f'{self.nev}:\n{jaratok}'
    