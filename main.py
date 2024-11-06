from legitarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from legitarsasagok_beolvas import legitarsasagok_beovas

# 6. GUI
def menu():
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")

def main():
    # Légitársaságok
    tarsasagok = legitarsasagok_beovas('./Légitársaságok')
    
    
    while True:
        menu()
        valasztas = input("Válassz egy műveletet: ")
        
        if valasztas == "1":
            print(tarsasagok)
            jaratszam = input("Add meg a járatszámot: ")
            utas_neve = input("Add meg az utas nevét: ")
            foglalas = tarsasagok[0].foglalas(jaratszam, utas_neve)
            if foglalas:
                print(f"Foglalás sikeres: {foglalas}")
            else:
                print("Járat nem található.")
        
        elif valasztas == "2":
            jaratszam = input("Add meg a járatszámot: ")
            utas_neve = input("Add meg az utas nevét: ")
            eredmeny = tarsasagok[0].lemondas(jaratszam, utas_neve)
            print(eredmeny)
        
        elif valasztas == "3":
            print("Aktuális foglalások:")
            print(tarsasagok[0].listaz_foglalasok())
        
        elif valasztas == "4":
            print("Kilépés...")
            break
        
        else:
            print("Érvénytelen választás. Kérlek próbáld újra.")

if __name__ == "__main__":
    main()