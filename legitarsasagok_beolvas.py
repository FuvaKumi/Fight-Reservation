import pandas as pd
import os

from legitarsasag import *
from belfoldi_jarat import *
from nemzetkozi_jarat import *

def legitarsasagok_beovas(mappa: str):
    print('Légitársaságok beolvasása...')
    legitarsasagok: list[LegiTarsasag] = []
    for fajlnev in os.listdir(mappa):
        if fajlnev.endswith('.xlsx'):
            legitarsasag_nev = fajlnev.replace('.xlsx', '')
            legitarsasagok.append(LegiTarsasag(legitarsasag_nev))
            df = pd.read_excel(f'{mappa}/{fajlnev}')
            for index in df.index:
                legitarsasagok[-1].add_jarat(BelfoldiJarat(df['ID'][index], df['Cel'][index], df['Ar'][index]) if df['Jarat'][index] == 'B' else NemzetkoziJarat(df['ID'][index], df['Cel'][index], df['Ar'][index]))
    
    print('Légitársaságok beolvasva!')
    return legitarsasagok