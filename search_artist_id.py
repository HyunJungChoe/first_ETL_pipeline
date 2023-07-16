import requests
import pprint
from  get_acesstoken import get_token
from secret_key import *

# Spotify API 액세스 토큰
token = get_token(client_id, client_secret)

def search_artist_id(token):

    # Spotify API 검색 엔드포인트
    auth_url = "https://api.spotify.com/v1/search"

    # 검색 유형 (artist, album, track 중 하나)
    search_type = "artist"

    # 쿼리 매개변수
    params = {
        "q": "artirst",  # 많은 아티스트 추출 하기
        "type":  search_type,
        "limit": 10,    # 1~50
        "offset":0      # 0~1000
    }

    # 검색 요청 보내기
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(auth_url, headers=headers, params=params)

   # 검색 결과 확인하기
    if response.status_code == 200:
        json_response = response.json()

        # pprint.pprint(json_response) 
        return split_data(json_response)

                
    elif response.status_code == 401:   
        print(f"{response.status_code} : 잘못되었거나 만료된 토큰입니다.")
        token = get_token(client_id,client_secret)
        print(f" ** 재발급 완료 **")
        search_artist_id(token)

    elif response.status_code == 429:    
        print(f"{response.status_code} : 앱이 속도 제한을 초과하였습니다.")

    else:
        print(f"{response.status_code} : 검색 요청에 실패하였습니다.")


def split_data(json_response):
        """
        JSON 데이터에서 원하는 컬럼만 추출하여 반환
        INPUT : {원본 JSON DATA}
        OPTPUT : {'artist_name': '', 'artist_id': '', 'followers': 394, 'genres': [], 'popularity': 34}, ... {}
        """
       
        data = json_response

        # 검색 결과에서 아티스트의 ID 추출하기
        artist_list_count = len(data['artists']['items'])
        extact_data = []
        artist_name, artist_id, followers, genres, popularity = [], [] ,[] ,[], []

        # 아티스트 테이블에 데이터 적재
        for i in range(artist_list_count): 
            artist_name.append(data['artists']['items'][i]['name'])
            artist_id.append(data['artists']['items'][i]['id'])
            followers.append(data['artists']['items'][i]['followers']['total'])
            genres.append(data['artists']['items'][i]['genres'])
            popularity.append(data['artists']['items'][i]['popularity'])
            
            artist = {
                "artist_name": artist_name[i]
                ,"artist_id": artist_id[i]
                ,"followers": followers[i]
                ,"genres": genres[i]
                ,"popularity": popularity[i]
            }
            extact_data.append(artist)

        # 변수들을 딕셔너리로 구성하여 반환
        return extact_data
    
    
# 실행 
# search_artist_id(token)

# ** RETURN 예시 ** 
# {artist_id: 3Nrfpe0tUJi4K4DXYWgMUX  
# ,artist_name: BTS 
# ,followers: 66667198
# ,genres: ['k-pop', 'k-pop boy group', 'pop'] 
# ,popularity: 90 } ... {}