import pandas as pd

def load_data(data_frame, file_path):
    data_frame.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Simuler des données
    df = pd.DataFrame({'column1': [1, 2, 3]})
    load_data(df, 'output_data.csv')