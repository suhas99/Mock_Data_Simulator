import pandas as pd
import yaml

config_yaml_file = open("/Users/suhaskashyap/PycharmProjects/pythonProject/config.yaml")
config = yaml.load(config_yaml_file, Loader=yaml.FullLoader)
config = config["Configrations"]


class ProcessData(object):
    def __init__(self, df):
        self.df = df
        self.output_df = pd.DataFrame()

    def add_data_to_df(self, json_data):
        if len(self.df) != 0 and len(self.df) % config["timeToSegregate"] == 0:
            self.get_avg_rates(self.df)
            self.df.drop(self.df.index, inplace=True)
        self.df = self.df.append(json_data, ignore_index=True)

    def get_df(self):
        self.output_df.columns = ['seg_start', 'seg_end', 'avg_hr', 'max_hr', 'avg_rr', 'max_rr']
        self.output_df.insert(0, 'user_id', self.df['user_id'])

        self.output_df.to_csv("output.csv")

    def get_avg_rates(self, df):
        data = [[df['timestamp'].iloc[0], df['timestamp'].iloc[len(df) - 1], df['heart_rate'].mean(),
                 df['heart_rate'].max(), df['respiration_rate'].mean(), df['respiration_rate'].max()]]
        self.output_df = self.output_df.append(data)
