from legitarsasag import LegiTarsasag
from jegyfoglalas import JegyFoglalas
import pandas as pd

def foglalasok_mentese(tarsasagok: list[LegiTarsasag], mappa: str):
    # Dataframe létrehozása a foglalásokból
    data = {
        'Társaság': [],
        'Járat': [],
        'Név': []
    }

    for tarsasag in tarsasagok:
        foglalas: JegyFoglalas
        for foglalas in tarsasag.foglalasok:
            data['Társaság'].append(tarsasag.nev)
            data['Járat'].append(foglalas.jarat.jaratszam)
            data['Név'].append(foglalas.utas_neve)

    df = pd.DataFrame(data)

    # Exportálás xlsx fájlba
    df.to_excel(mappa)
    