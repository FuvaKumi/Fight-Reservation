import pandas as pd
import os

from legitarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat

def legitarsasagok_beovas(mappa):
    legitarsasagok = []
    for fajlnev in os.listdir(mappa):
        if fajlnev.endswith('.xlsx'):
            print(f'{mappa}/{fajlnev}')
            legitarsasag_nev = fajlnev.replace('.xlsx', '')
            legitarsasagok.append(LegiTarsasag(legitarsasag_nev))
            df = pd.read_excel(f'{mappa}/{fajlnev}')
            for index in df.index:
                legitarsasagok[-1].add_jarat(BelfoldiJarat(df['ID'][index], df['Cel'][index], df['Ar'][index]) if df['Jarat'][index] == 'B' else NemzetkoziJarat(df['ID'][index], df['Cel'][index], df['Ar'][index]))
    return legitarsasagok