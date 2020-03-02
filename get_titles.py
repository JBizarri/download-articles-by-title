import os

import pandas as pd

from exc.exceptions import WrongFolderLength, WrongFileFormat


# This function will return all article titles from your spreadsheet in list format
def get_titles():
    excel_folder = os.path.join(os.getcwd(), 'Spreadsheet')
    os.makedirs(excel_folder, exist_ok=True)
    excel_folder_files = os.listdir(excel_folder)
    if len(excel_folder_files) != 1:
        raise WrongFolderLength(len(excel_folder_files))
    artigo_path = os.path.join(excel_folder, excel_folder_files[0])
    try:
        if excel_folder_files[0].endswith('.xlsx'):
            df = pd.read_excel(artigo_path)
        elif excel_folder_files[0].endswith('.csv'):
            df = pd.read_csv(artigo_path)
        else:
            raise WrongFileFormat
    except Exception as e:
        raise e

    return df['Title'].to_list()
