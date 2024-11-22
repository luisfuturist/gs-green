import requests
import json
from save_to_db import save_data_to_db

API_URL = "https://dadosabertos.aneel.gov.br/api/3/action/datastore_search"
RESOURCE_ID = "ff80dd21-eade-4eb5-9ca8-d802c883940e"

def fetch_aneel_data(limit=10):
    params = {"resource_id": RESOURCE_ID, "limit": limit}
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["result"]["records"]
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

if __name__ == "__main__":
    data = fetch_aneel_data(limit=10)
    
    if data:
        save_data_to_db(data)
    else:
        print("No data to save.")
