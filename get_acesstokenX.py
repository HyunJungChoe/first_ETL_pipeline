import requests
import json
import base64
import pprint


client_id = "7a94dfe19f6a4f25a787c58b0411b1e8"  # Github 업로드시 제외 
client_secret = "7904df2d8bf447d8bf99b8ef6d56899c"
endpoint = "https://accounts.spotify.com/api/token"

encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

headers = {"Authorization": "Basic {}".format(encoded)}
payload = {"grant_type": "client_credentials"}

response = requests.post(endpoint, data=payload, headers=headers)
access_token = json.loads(response.text)['access_token']

#참고
pprint.pprint(json.loads(response.text))

# Return 된 Json
# {'access_token': 'BQDfY6BwaFdx35pfAcUgLqAVRqln1PTd18tOW-ghu_DY-YOBABC6U8bizp9p7CxdAThYT2JJ8Lq9zW2Sjzsd45njmAoLeBLUunUYnNJbyAcp-FWIMc-E',
#  'expires_in': 3600,
#  'token_type': 'Bearer'}