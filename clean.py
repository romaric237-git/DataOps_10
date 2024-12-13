import pandas as pd

def compress_to_parquet(data_frame, filename):
    data_frame.to_parquet(filename)

if __name__ == "__main__":
    df = pd.DataFrame({'column1': [1, 2, 3]})
    compress_to_parquet(df, 'data.parquet')