from secret_key import *
import requests
import base64


def get_token(client_id,client_secret):
    """ 
    ### 클라이언트 자격 증명 토큰을 가져오는 함수
    스포티파이 개발자 홈페이지에서 제공하는 데이터를 가져오기 위해 우선 토큰을 먼저 가져옵니다.
    - 파라미터 값 : `clientID`, `clientSecert`
    - 리턴 값 : `accessToken` 
    - 참고자료 : https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/
    """

    # base64 encoding
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

    # 토큰 받아오기 
    if auth_response.status_code == 200:
        token = auth_response.json()["access_token"]
        return token
    
    else:
        print(f"Authentication failed with status code {auth_response.status_code}")


# token = get_token(client_id,client_secret)
# print(token)

