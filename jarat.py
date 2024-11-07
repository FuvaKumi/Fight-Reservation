from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, felszallas, celallomas, jegyar, datum):
        self.jaratszam = jaratszam
        self.felszallas = felszallas
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.datum = datum
    
    @abstractmethod
    def __str__(self):
        pass