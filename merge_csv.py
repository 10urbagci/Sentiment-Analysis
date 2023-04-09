import pandas as pd
import glob


path = r'C:\Users\Onur\Desktop\john_wick'


all_files = glob.glob(path + "/*.csv")


df_merged = pd.DataFrame()


for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df_merged = pd.concat([df_merged, df])


df_merged.to_csv('john_wick_data.csv', index=False)