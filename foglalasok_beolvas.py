import pandas as pd
import os

from legitarsasag import *
from belfoldi_jarat import *
from nemzetkozi_jarat import *

def foglalasok_beolvas(tarsasagok: list[LegiTarsasag], foglalasok_file: str):
    print('Foglalások beolvasása...')
    foglalasok = list[JegyFoglalas]
    df = pd.read_excel(foglalasok_file)
    tarsasagnevek = list([LegiTarsasag.nev for LegiTarsasag in tarsasagok])

    for i in df.index:
        if df['Társaság'][i] in tarsasagnevek:
            index_of_tarsasag = tarsasagnevek.index(df['Társaság'][i])
            if tarsasagok[index_of_tarsasag]._get_jarat_by_jaratszam(df['Járat'][i]):
                tarsasagok[index_of_tarsasag].foglalas(tarsasagok[index_of_tarsasag]._get_jarat_by_jaratszam(df['Járat'][i]), df['Név'][i])
            else:
                hibas_jarat = df['Járat'][i]
                print(f'    Hiba ({i + 1}. sor): Nem található ilyen járat a {tarsasagok[index_of_tarsasag].nev} társaságnál! ({hibas_jarat})')
        else:
            hibas_nev = df['Társaság'][i]
            print(f'    Hiba ({i + 1}. sor): Nem található ilyen légitársaság! ({hibas_nev})')

    print('Foglalások beolvasva!')
    return foglalasok