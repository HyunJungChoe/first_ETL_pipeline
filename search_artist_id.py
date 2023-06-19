import requests
import pprint
from  get_acesstoken import get_token
from secret_key import *

# Spotify API 액세스 토큰
token = get_token(client_id, client_secret)

def search_artist_id(token):

    # Spotify API 검색 엔드포인트
    auth_url = "https://api.spotify.com/v1/search"

    # 검색할 아티스트 이름
    artist_name = "BTS"

    # 검색 유형 (artist, album, track 중 하나)
    search_type = "artist"

    # 쿼리 매개변수
    params = {
        "q": artist_name,
        "type": search_type,
        "limit": 1
    }

    # 검색 요청 보내기
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(auth_url, headers=headers, params=params)

   # 검색 결과 확인하기
    if response.status_code == 200:
        json_response = response.json()

        # pprint.pprint(json_response)  # 받은 json 을 컬럼 별 분리
        split_data(json_response)

                
    elif response.status_code == 401:   
        print(f"{response.status_code} : 잘못되었거나 만료된 토큰입니다.")
        token = get_token(client_id,client_secret)
        print(f" ** 재발급 완료 **")

        search_artist_id(token)

    elif response.status_code == 429:    
        print(f"{response.status_code} : 앱이 속도 제한을 초과하였습니다.")

    else:
        print(f"{response.status_code} : 검색 요청에 실패하였습니다.")


# 데이터 보기 쉽게 변환 
def split_data(json_response):
        # 검색 결과에서 아티스트의 ID 추출하기

        data = json_response

        # 아티스트 테이블에 데이터 적재
        artist_id = data['artists']['items'][0]['id']
        artist_name = data['artists']['items'][0]['name']
        popularity = data['artists']['items'][0]['popularity']
        images = data['artists']['items'][0]['images'][0]['url']

        print(f"artist_id: {artist_id}  \n \
            ,artist_name: {artist_name} \n \
            ,popularity: {popularity}   \n \
            ,images: {images}")


search_artist_id(token)



# ** RETURN 예시 ** 
# artist_id: 3Nrfpe0tUJi4K4DXYWgMUX 
#,artist_name: BTS 
#,popularity: 91   
#,images: https://i.scdn.co/image/ab6761610000e5eb5704a64f34fe29ff73ab56bb
