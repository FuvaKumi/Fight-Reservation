from legitarsasag import *
from belfoldi_jarat import *
from nemzetkozi_jarat import *
from legitarsasagok_beolvas import *

def menu():
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")

def jarat_input(tarsasagok):
    for i in range(len(tarsasagok)):
        print(F'{i + 1}. {tarsasagok[i].nev}')
    while True:
        tarsasag_str = input("Add meg a légitársaság számát: ")
        try:
            tarsasag = int(tarsasag_str)-1
            if tarsasag in range(len(tarsasagok)):
                break
            else:
                raise Exception("Out of range.")
        except:
            print("Érvénytelen társaság szám!")

    print(tarsasagok[tarsasag])
    jaratszam = input("Add meg a járatszámot: ")
        
    utas_neve = input("Add meg az utas nevét: ")

    return tarsasag, jaratszam, utas_neve

def main():
    # Légitársaságok beolvasása
    tarsasagok = legitarsasagok_beovas('./Légitársaságok')
    
    
    while True:
        menu()
        valasztas = input("Válassz egy műveletet: ")
        
        if valasztas == "1":
            tarsasag, jaratszam, utas_neve = jarat_input(tarsasagok)
            
            eredmeny = tarsasagok[tarsasag].foglalas(jaratszam, utas_neve)
            print(eredmeny)
        
        elif valasztas == "2":
            tarsasag, jaratszam, utas_neve = jarat_input(tarsasagok)

            eredmeny = tarsasagok[tarsasag].lemondas(jaratszam, utas_neve)
            print(eredmeny)
        
        elif valasztas == "3":
            print("Aktuális foglalások:")
            for i in range(len(tarsasagok)):
                print(f'{tarsasagok[i].nev}:\n{tarsasagok[i].listaz_foglalasok()}')
        
        elif valasztas == "4":
            print("Kilépés...")
            break
        
        else:
            print("Érvénytelen választás. Kérlek próbáld újra.")

if __name__ == "__main__":
    main()