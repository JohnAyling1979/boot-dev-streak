import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

url = 'https://accounts.spotify.com/api/token'
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

res = requests.post(url, headers=headers, data=data )

json = res.json()

access_token = json['access_token']
print(access_token)
url = 'https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb'
headers = {
  "Authorization": f"Bearer {access_token}"
}
print(headers)
res = requests.get(url, headers=headers)

print(res.json())
