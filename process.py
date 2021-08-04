# Extracts data from individual agency data inventory templates
import pandas as pd
import os


def import_one_inventory(file):
    temp = pd.read_excel("data/raw/" + file,
                         sheet_name='Data Sources',
                         header=0,
                         skiprows=6,
                         usecols='B:M',
                         na_values='nan')
    return temp


if __name__=='__main__':
    files = os.listdir('data/raw')
    data_inventory = pd.DataFrame()
    data_inventory = [import_one_inventory(file) for file in files if '~' not in file]
    data_inventory = pd.concat(data_inventory)
    data_inventory = data_inventory[data_inventory.Agency.notnull()]
    data_inventory = data_inventory[data_inventory['Name of System or Data Source'].notnull()]
    data_inventory.to_excel('data_source_inventory.xlsx')