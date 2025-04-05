import requests
from config import config as cfg
import json

url = "https://api.github.com/repos/NiallRussell/aprivateone"

apiKey = cfg["testprivatekey"]
#headers = {"Authorization": f"token {apiKey}"}
#response = requests.get(url, headers=headers)

response = requests.get(url, auth=("token", apiKey))

repoJSON = response.json()

with open("private.json", "w") as fp:
    json.dump(repoJSON, fp, indent = 4)