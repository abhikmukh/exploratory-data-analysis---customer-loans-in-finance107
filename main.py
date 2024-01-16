from db_utils import RDSDatabaseConnector
import yaml


def read_db_creds(credential_file):
    with open(credential_file, 'r') as file:
        credential_dict = yaml.safe_load(file)
        return credential_dict


def main():
    credential_file = 'credentials.yaml'
    credential_dict = read_db_creds(credential_file)
    db_connector = RDSDatabaseConnector(credential_dict)
    df = db_connector.read_rds_table(table_name="loan_payments")
    db_connector.write_csv_file(df, file_name='data/loan_payments.csv')


if __name__ == '__main__':
    main()
