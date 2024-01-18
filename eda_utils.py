import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot


class DataTransform:
    """
    This class is used to transform the data
    """
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def change_date_format(self, column_name: str, date_format: str) -> pd.DataFrame:
        """
        This function is used to change the date format of a column
        :param column_name:
        :param date_format:
        :return: dataframe
        """
        self.df[column_name] = pd.to_datetime(self.df[column_name], format=date_format)
        self.df[column_name] = self.df[column_name].dt.date.apply(lambda x: x.strftime('%Y-%m'))
        return self.df

    def change_column_type(self, column_name: str, new_type: str) -> pd.DataFrame:
        """
        This function is used to change the type of a column
        :param column_name:
        :param new_type:
        :return: dataframe
        """
        self.df[column_name] = self.df[column_name].astype(new_type)
        return self.df


class DataFrameTransform:
    """
    This class is used to transform the dataframe
    """

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def fill_null_values_with_mean(self, column_name: str) -> pd.DataFrame:
        """
        This function is used to fill the null values with mean
        :param column_name:
        :return:
        """
        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].mean())
        return self.df

    def fill_null_values_with_median(self, column_name: str) -> pd.DataFrame:
        """
        This function is used to fill the null values with median
        :param column_name:
        :return:
        """
        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].median())
        return self.df

    def fill_null_values_with_mode(self, column_name: str) -> pd.DataFrame:
        """
        This function is used to fill the null values with mode
        :param column_name:
        :return:
        """
        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].mode()[0])
        return self.df

    def fill_null_values_with_custom_value(self, column_name: str, value: float) -> pd.DataFrame:
        """
        This function is used to fill the null values with custom value
        :param column_name:
        :param value:
        :return:
        """
        self.df[column_name] = self.df[column_name].fillna(value)
        return self.df

    def fill_null_values_with_most_frequent_value(self, column_name: str) -> pd.DataFrame:
        """
        This function is used to fill the null values with most frequent value
        :param column_name:
        :return:
        """
        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].value_counts().index[0])
        return self.df


class DataFrameInfo:
    """
    This class is used to get information about the dataframe
    """
    @staticmethod
    def get_df_mean(df: pd.DataFrame, column_name: str) -> None:
        """
        This function is used to get the mean of a column
        :param df:
        :param column_name:
        :return:
        """
        print(f"mean: {df[column_name].mean()}, median: {df[column_name].median()}, mode: {df[column_name].mode()[0]}")

    @staticmethod
    def count_null_values_percentage(df: pd.DataFrame,  list_of_columns: list) -> None:
        """
        This function is used to get the percentage of null values in a column
        :param df:
        :param list_of_columns:
        :return: None
        """
        for column in list_of_columns:
            print(f"Percentage of nulls in {column}: {df[column].isnull().sum()/len(df)}")

    @staticmethod
    def get_all_null_values(df) -> pd.DataFrame:
        """
        This function is used to get the total number of null values in a column
        :return: dataframe
        """
        return df.isnull().sum()

    @staticmethod
    def get_df_unique_values(df: pd.DataFrame) -> pd.Series:
        """
        This function is used to get the unique values in a column
        :param df:
        :return:
        """
        return df.nunique()

    @staticmethod
    def list_all_numeric_columns(df: pd.DataFrame) -> list:
        """
        This function is used to get the list of all numeric columns
        :param df:
        :return: List
        """
        return df.select_dtypes(include='number').columns.tolist()

    @staticmethod
    def list_all_categorical_columns(df: pd.DataFrame) -> list:
        """
        This function is used to get the list of all categorical columns
        :param df:
        :return: List
        """
        return df.select_dtypes(include='object').columns.tolist()

    @staticmethod
    def list_all_datetime_columns(df: pd.DataFrame) -> list:
        """
        This function is used to get the list of all datetime columns
        :param df:
        :return: List
        """
        return df.select_dtypes(include='datetime').columns.tolist()

    @staticmethod
    def list_all_columns_with_missing_values(df: pd.DataFrame) -> list:
        """
        This function is used to get the list of all columns with missing values
        :param df:
        :return: List
        """
        return df.columns[df.isnull().any()].tolist()

    @staticmethod
    def get_log_transform(df: pd.DataFrame, column_name: str) -> pd.Series:
        """
        This function is used to get the log transform of a column
        :param df:
        :param column_name:
        :return: Series
        """
        return df[column_name].map(lambda i: np.log(i) if i > 0 else 0)

    @staticmethod
    def analyse_categorical_data(df: pd.DataFrame, column_name: str) -> pd.Series:
        """
        This function is used to get the value counts of a column
        :param df:
        :param column_name:
        :return: series
        """
        return df[column_name].value_counts()

    @staticmethod
    def calculate_z_score(df: pd.DataFrame, column_name: str) -> pd.Series:
        """
        This function is used to calculate the z-score of a column
        :param df:
        :param column_name:
        :return: series
        """
        return (df[column_name] - df[column_name].mean()) / df[column_name].std()

    @staticmethod
    def calculate_iqr(df: pd.DataFrame, column_name: str) -> pd.Series:
        """
        This function is used to calculate the iqr of a column
        :param df:
        :param column_name:
        :return: series
        """
        return df[column_name].quantile(0.75) - df[column_name].quantile(0.25)


class DataFrameVisualize:
    """
    This class is used to visualize the dataframe
    """

    @staticmethod
    def plot_histogram(df: pd.DataFrame, column_name: str) -> None:
        """
        This function is used to plot a histogram
        :param df:
        :param column_name:
        :return:
        """
        return sns.histplot(data=df, y=column_name, kde=True)

    @staticmethod
    def plot_boxplot(df: pd.DataFrame, column_name: str):
        """
        This function is used to plot a boxplot
        :param df:
        :param column_name:
        :return:
        """
        return df.boxplot(column=column_name)

    @staticmethod
    def plot_scatter(df: pd.DataFrame, x, y):
        """
        This function is used to plot a scatter plot
        :param df:
        :param x:
        :param y:
        :return:
        """
        return df.plot.scatter(x=x, y=y)

    @staticmethod
    def plot_correlation_matrix(df: pd.DataFrame):
        """
        This function is used to plot a correlation matrix
        :param df:
        :return:
        """
        return df.corr()

    @staticmethod
    def plot_heatmap(df: pd.DataFrame):
        """
        This function is used to plot a heatmap
        :param df:
        :return:
        """
        plt.figure(figsize=(10, 8))
        return sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

    @staticmethod
    def plot_qqplot(df: pd.DataFrame, column_name: str):
        return qqplot(df[column_name], scale=1, line='q', fit=True)

    @staticmethod
    def plot_prob_distribution(df: pd.DataFrame, column_name: str):
        probs = df[column_name].value_counts(normalize=True)

        # Create bar plot
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        return sns.barplot(y=probs.values, x=probs.index)

    @staticmethod
    def box_plot_with_scatter_points(df: pd.DataFrame, column_name: str):
        sns.boxplot(y=df[column_name], color='lightgreen', showfliers=True)
        sns.swarmplot(y=df[column_name], color='black', size=5)
        plt.title(f'Box plot with scatter points {column_name}')














