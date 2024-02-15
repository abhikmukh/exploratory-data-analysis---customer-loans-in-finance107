import yaml

from sqlalchemy import create_engine
from sqlalchemy import inspect

import pandas as pd


class RDSDatabaseConnector:
    def __init__(self, credential_dict: dict) -> None:
        self.credentials_dict = credential_dict

    def _init_db_engine(self) -> create_engine:
        database_cred = self.credentials_dict
        print(database_cred)
        database_uri = f"postgresql+psycopg2://{database_cred['RDS_USER']}" \
                       f":{database_cred['RDS_PASSWORD']}@{database_cred['RDS_HOST']}:" \
                       f"{database_cred['RDS_PORT']}/{database_cred['RDS_DATABASE']}"
        database_engine = create_engine(database_uri)
        return database_engine

    def list_db_table(self) -> list
        engine = self._init_db_engine()
        inspector = inspect(engine)
        list_all_tables = inspector.get_table_names()
        return list_all_tables

    def read_rds_table(self, table_name: str) -> pd.DataFrame:

        all_tables = self.list_db_table()
        for table in all_tables:
            if table_name == table:
                df = pd.read_sql_table(table, self._init_db_engine())
                return df

    @staticmethod
    def write_csv_file(df: pd.DataFrame, file_name: str) -> None:
        return df.to_csv(file_name, index=False)

