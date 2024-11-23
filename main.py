import json
import requests

from decouple import config

# Configuration
cloud_name = config("CLOUD_NAME")
api_key = config("API_KEY")
api_secret = config("API_SECRET")
folder_name = config("FOLDER_NAME")

# Autentication
url = f"https://api.cloudinary.com/v1_1/{cloud_name}/resources/video/upload"
params = {"prefix": folder_name + "/", "max_results": 500}

response = requests.get(url, params=params, auth=(api_key, api_secret))

# Response check
if response.status_code == 200:
    resources = response.json().get("resources", [])
    links = [{"url": resource["secure_url"]} for resource in resources]

    # Guardar como JSON
    with open(f"{folder_name}.json", "w") as json_file:
        json.dump(links, json_file)
else:
    print(f"Error: {response.status_code} - {response.text}")
