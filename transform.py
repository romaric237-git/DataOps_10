import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    df['new_column'] = df['old_column'] * 2
    return df

if __name__ == "__main__":
    # Simuler des données
    data = [{'old_column': 1}, {'old_column': 2}]
    transformed_data = transform_data(data)
    print(transformed_data)