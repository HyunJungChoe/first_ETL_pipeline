import requests
import base64

client_id = '7a94dfe19f6a4f25a787c58b0411b1e8'
client_secret = '7904df2d8bf447d8bf99b8ef6d56899c'

auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

auth_data = {
    "grant_type": "client_credentials"
}

auth_headers = {
    "Authorization": f"Basic {b64_auth_str}"
}

auth_url = "https://accounts.spotify.com/api/token"

auth_response = requests.post(auth_url, data=auth_data, headers=auth_headers)

if auth_response.status_code == 200:
    token = auth_response.json()["access_token"]
    print(token)
else:
    print(f"Authentication failed with status code {auth_response.status_code}")

# Return 된 Key:  BQAUe3E3z9qHvkYqcnoIvDagdUZRfjNBNuittjKxlUB5S2wMVtexKbL1mwi01mUdPOgQACXIFUQmjRHREWZy4dkiw41-mDKoW63MdxOsNRwjH7WI5Ksb
