import pandas as pd
import os
import shutil
from datetime import datetime

from legitarsasag import *
from belfoldi_jarat import *
from nemzetkozi_jarat import *

def create_backup(file_path, backup_dir):
    if not os.path.exists(file_path):
        print(f"A fájl nem található: {file_path}")
        return
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    file_name = os.path.basename(file_path).split('.')[0]
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"{file_name}_{date_str}.xlsx"

    backup_path = os.path.join(backup_dir, backup_name)

    shutil.copy(file_path, backup_path)
    print(f"Backup sikeresen létrehozva: {backup_path}")

def foglalasok_beolvas(tarsasagok: list[LegiTarsasag], foglalasok_file: str):
    # Backup a fájlról beolvasás előtt
    create_backup(foglalasok_file, './Foglalások/Backup')

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