import time
from transform import transform_data

def benchmark_transformation(transform_function, data):
    start_time = time.time()
    transform_function(data)
    execution_time = time.time() - start_time
    print(f"Temps d'exécution : {execution_time:.5f} secondes")

if __name__ == "__main__":
    data = [{'old_column': 1}, {'old_column': 2}]
    benchmark_transformation(transform_data, data)