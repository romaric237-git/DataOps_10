import requests

def get_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_url = "https://api.example.com/data"  # Remplacez par votre URL d'API
    data = get_data(api_url)
    print(data)