import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd

def loads_yaml_file():
    with open('eda_loans\credentials.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


cred_yaml = loads_yaml_file()

class RDSDatabaseConnector():
    def __init__(self, creds):
        self.creds = creds
    
    def initialise_engine(self):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = self.creds['RDS_HOST']
        USER = self.creds['RDS_USER']
        PASSWORD = self.creds['RDS_PASSWORD']
        DATABASE = self.creds['RDS_DATABASE']
        PORT = self.creds['RDS_PORT']
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        engine.connect()
        return engine

    def extract_RDS_database(self):
        engine = self.initialise_engine()
        loan_payments = pd.read_sql_table("loan_payments", engine)
        return loan_payments

    def saves_data(self, loan_payments, file_location):
        loan_payments.to_csv(file_location, index=False)
    
connector = RDSDatabaseConnector(cred_yaml)
df = connector.extract_RDS_database()
connector.saves_data(df, 'eda_loans\data.csv')


