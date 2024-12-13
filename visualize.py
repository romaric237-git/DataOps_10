import matplotlib.pyplot as plt

def visualize_data(data):
    plt.plot(data['old_column'], data['new_column'])
    plt.title('Visualisation des données')
    plt.xlabel('Ancienne colonne')
    plt.ylabel('Nouvelle colonne')
    plt.savefig('visualisation.png')

if __name__ == "__main__":
    data = {'old_column': [1, 2, 3], 'new_column': [2, 4, 6]}
    visualize_data(data)