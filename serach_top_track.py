import requests
import pprint
from  get_acesstoken import get_token
from secret_key import *
from serach_audio_feature import *

# Spotify API 액세스 토큰
token = get_token(client_id, client_secret)

def get_top_track(token, id):   
    
    # Spotify API 검색 엔드포인트
    auth_url = "https://api.spotify.com/v1/artists/{}/top-tracks".format(id)
    
    # 쿼리 매개변수
    params = {
        "market" : 'US'
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
        track_name, track_id, tracks_popularity = split_data(json_response)
        if (track_name == [] or track_id == []) :
            pass
            print('track_name 또는 track_id 값이 없어 pass 되었습니다.')
        else:
            return get_audio_feature(token, track_name, track_id, tracks_popularity)
                
    elif response.status_code == 401:   
        print(f"{response.status_code} : 잘못되었거나 만료된 토큰입니다.")
        token = get_token(client_id,client_secret)
        print(f" ** 재발급 완료 **")
        get_top_track(token)

    elif response.status_code == 429:    
        print(f"{response.status_code} : 앱이 속도 제한을 초과하였습니다.")

    else:
        print(f"{response.status_code} : 검색 요청에 실패하였습니다.")


# 데이터 보기 쉽게 변환 
def split_data(json_response):
    data = json_response

    # 모든 앨범 데이터를 저장하기 위한 리스트 생성 
    track_len = len(data['tracks'])
    track_name, track_id, tracks_popularity= [], [], []

    # 앨범 리스트에 데이터 적재
    for i in range(track_len):
        track_name.append(data['tracks'][i]['name'])
        track_id.append(data['tracks'][i]['id'])
        tracks_popularity.append(data['tracks'][i]['popularity'])

    # print(track_name, track_id, tracks_popularity)
    return track_name, track_id, tracks_popularity

if __name__ == '__main__':
    # 임시 아티스트 id 전송 -> 이후 빅쿼리에서 가져오기 
    id = '4cS0IGoIwn4vOj3uzkiOrK'
    get_top_track(token, id)

# ** RETURN 예시 ** 
# [{'track_name': 'Take Two', 'track_id': '5IAESfJjmOYu7cHyX557kz', 'tracks_popularity': 95}
# ,{'track_name': 'Left and Right', 'track_id': '5Odq8ohlgIbQKMZivbWkEo', 'tracks_popularity': 88} ... {}]