import pandas as pd


class DataTransform:
    def __init__(self, df):
        self.df = df

    def change_date_format(self, column_name, date_format):
        self.df[column_name] = pd.to_datetime(self.df[column_name], format=date_format)
        self.df[column_name] = self.df[column_name].dt.date.apply(lambda x: x.strftime('%Y-%m'))
        return self.df

    def change_column_type(self, column_name, new_type):
        self.df[column_name] = self.df[column_name].astype(new_type)
        return self.df


class DataFrameInfo:

    def __init__(self, df):
        self.df = df

    def get_df_info(self):
        return self.df.info()

    def get_df_shape(self):
        return self.df.shape

    def get_df_columns(self):
        return self.df.columns

    def get_df_describe(self):
        return self.df.describe()

    def get_df_mean(self):
        return self.df.mean()

    def get_df_median(self):
        return self.df.median()

    def get_df_mode(self):
        return self.df.mode()

    def count_null_values(self):
        for column in self.df.columns:
            print(f"Percentage of nulls in {column}: {self.df[column].isnull().sum()/len(self.df)}")

    def get_df_null_values(self):
        return self.df.isnull().sum()

    def get_df_unique_values(self):
        return self.df.nunique()

    def list_all_numeric_columns(self):
        return self.df.select_dtypes(include='number').columns.tolist()


