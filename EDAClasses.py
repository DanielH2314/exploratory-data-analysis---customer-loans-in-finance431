import pandas as pd
import numpy as np

class DataChange:
    def __init__(self, database):
        self.database = database

    def remove_duplicates(self):
        self.database.drop_duplicates()
    
    def change_datatype(self, colnames, datatype):
        self.database[[colnames]] = self.database[[colnames]].astype('datatype')

    def change_to_bool(self, colnames, truevalue, falsevalue):
        self.database[[colnames]] = self.database[[colnames]].map({truevalue: True, falsevalue: False})

    def change_to_datetime(self, colnames, dateformat):
        self.database[colnames] = pd.to_datetime(self.database[colnames], format = dateformat)

class GetInfo:
    def __init__(self):
        self = self
    
    def statistics(self, database):
        database.describe()
    
    def percentage_null(self, database):
        print((1 - database.count() / len(database)) *100)

class DataFrameTransform:
    def __init__(self, database):
        self.database = database

    def impute_mode(self, column):
        self.database[column] = self.database[column].fillna(self.database[column].mode())

    def impute_median(self, column):
        self.database[column] = self.database[column].fillna(self.database[column].median())

    def impute_mean(self, column):
        self.database[column] = self.database[column].fillna(self.database[column].mean())
    
class Plotter:
    def __init__(self, database):
        self.database = database
        

        
    
