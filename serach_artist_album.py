import requests
import pprint
from  get_acesstoken import get_token
from secret_key import *

# Spotify API 액세스 토큰
token = get_token(client_id, client_secret)

# 아티스트 id 전송 예시
id = '3Nrfpe0tUJi4K4DXYWgMUX'

def get_artist_album(token, id):   
    
    # Spotify API 검색 엔드포인트
    auth_url = "https://api.spotify.com/v1/artists/{}/albums".format(id)
    
    # 쿼리 매개변수
    params = {
        "limit": 10
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

        get_artist_album(token)

    elif response.status_code == 429:    
        print(f"{response.status_code} : 앱이 속도 제한을 초과하였습니다.")

    else:
        print(f"{response.status_code} : 검색 요청에 실패하였습니다.")


# 데이터 보기 쉽게 변환 
def split_data(json_response):
        data = json_response

        # 모든 앨범 데이터를 저장하기 위한 리스트 생성 
        album_list_count = len(data['items'])
        album = []
        extact_data = []
        album_names, album_id, total_tracks, release_date = [], [], [], []

        # 앨범 리스트에 데이터 적재
        for i in range(album_list_count):
            album_names.append(data['items'][i]['name'])
            album_id.append(data['items'][i]['id'])
            total_tracks.append(data['items'][i]['total_tracks'])
            release_date.append(data['items'][i]['release_date'])

            album = {
                "album_name": album_names[i]
                ,"album_id": album_id[i]
                ,"total_tracks": total_tracks[i]
                ,"release_date": release_date[i]
            }
            extact_data.append(album)

        print(extact_data)
        
        # 변수들을 딕셔너리로 구성하여 반환
        return extact_data
        
get_artist_album(token, id)

# ** RETURN 예시 ** 
# album_name: Proof  
#              ,album_id: 6al2VdKbb6FIz9d7lU7WRB 
#              ,total_tracks: 35 
#              ,release_date: 2022-06-10
# album_name: BE  
#              ,album_id: 1aAjA5rYVUh1JhVIafOmbQ 
#              ,total_tracks: 8 
#              ,release_date: 2020-11-20
# album_name: MAP OF THE SOUL : 7 ~ THE JOURNEY ~  
#              ,album_id: 1nScVw87kRJiT2bg2Kswhp 
#              ,total_tracks: 13 
#              ,release_date: 2020-07-14
# album_name: MAP OF THE SOUL : 7  
#              ,album_id: 4I1cAiu9Gko1xwJPZ4lViH 
#              ,total_tracks: 20 
#              ,release_date: 2020-02-21
# album_name: MAP OF THE SOUL : PERSONA  
#              ,album_id: 1vuZRBjsQH7B8x6wLFe9nz 
#              ,total_tracks: 7 
#              ,release_date: 2019-04-12
# album_name: Love Yourself 結 'Answer'  
#              ,album_id: 50a3txbpZf1NqzydC8acoU 
#              ,total_tracks: 26 
#              ,release_date: 2018-08-24
# album_name: Love Yourself 轉 'Tear'  
#              ,album_id: 7eUEmsQKoGVzjKjX3lLX8A 
#              ,total_tracks: 11 
#              ,release_date: 2018-05-18
# album_name: FACE YOURSELF  
#              ,album_id: 66J1OXSaS3hBZASOV3el8t 
#              ,total_tracks: 12 
#              ,release_date: 2018-04-04
# album_name: Love Yourself 承 'Her'  
#              ,album_id: 1OvAmvGLH3ngDeXktemYMx 
#              ,total_tracks: 9 
#              ,release_date: 2017-09-18
# album_name: You Never Walk Alone  
#              ,album_id: 1ldyIW90eel4OGhWov8ybM 
#              ,total_tracks: 18 
#              ,release_date: 2017-02-13