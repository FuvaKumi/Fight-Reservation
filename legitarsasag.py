from jegyfoglalas import *

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def add_jarat(self, jarat):
        self.jaratok.append(jarat)

    def foglalas(self, jaratszam, utas_neve):
        jarat = self._get_jarat_by_jaratszam(jaratszam)
        if jarat:
            foglalas = JegyFoglalas(jarat, utas_neve)
            self.foglalasok.append(foglalas)
            return foglalas
        return "Nincs ilyen járat."

    def _get_jarat_by_jaratszam(self, jaratszam):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None

    def lemondas(self, jaratszam, utas_neve):
        for foglalas in self.foglalasok:
            if foglalas.jarat.jaratszam == jaratszam and foglalas.utas_neve == utas_neve:
                self.foglalasok.remove(foglalas)
                return f"Foglalás lemondva: {utas_neve} - {jaratszam}"
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