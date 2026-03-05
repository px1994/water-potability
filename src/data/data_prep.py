import os
import numpy as np
import pandas as pd

def load_data(filepath: str):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f'Error loading data from{filepath}:{e}')
    

def fill_missing_with_mean(df):
    try:
        for column in df.columns:
            if df[column].isnull().any():
                mean_value = df[column].mean()
                df[column].fillna(mean_value,inplace=True)
        return df
    except Exception as e:
        raise(f'Error Filling missing values:{e}')


def save_data(df: pd.DataFrame,filepath: str) -> None:
    try:
        df.to_csv(filepath, index=False)
    except Exception as e:
        raise Exception(f'Error Saving Data to{filepath}:{e}')

def main():
    raw_data_path = './data/raw' # loading data from data collection
    processed_data_path = './data/processed' # after processing saving data 
 
    train_data = load_data(os.path.join(raw_data_path,'train.csv'))
    test_data = load_data(os.path.join(raw_data_path,'test.csv'))

    train_processed_data = fill_missing_with_mean(train_data)
    test_processed_data = fill_missing_with_mean(test_data)

    os.makedirs(processed_data_path)

    save_data(train_processed_data, os.path.join(processed_data_path,'train_processed_mean.csv'))
    save_data(test_processed_data, os.path.join(processed_data_path,'test_processed_mean.csv'))


if __name__ == '__main__':
    main()






