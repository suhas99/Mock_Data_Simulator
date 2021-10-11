import pandas as pd


class ProcessData(object):
    def __init__(self, df):
        self.df = df

    def add_data_to_df(self, json_data):
        self.df = self.df.append(json_data, ignore_index=True)
        self.get_avg_rates(self.df)

    def get_df(self):
        self.df.to_csv('output.csv')

    def get_avg_rates(self, df):
        temp_df = df
        temp_df['avg_hr'] = temp_df['heart_rate'].mean()
        temp_df['max_hr'] = temp_df['heart_rate'].max()
        temp_df['avg_rr'] = temp_df['respiration_rate'].mean()
        temp_df['max_rr'] = temp_df['respiration_rate'].max()

