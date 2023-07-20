import requests
import pprint
from  get_acesstoken import get_token
from secret_key import *

# Spotify API 액세스 토큰
token = get_token(client_id, client_secret)

def get_audio_feature(token, track_name, tracks_id, tracks_popularity):   
        
    # Spotify API 검색 엔드포인트
    auth_url = "https://api.spotify.com/v1/audio-features"

    unpack = ",".join(tracks_id)

    # 쿼리 매개변수
    params = {
        "ids" : unpack
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
        return split_data(json_response, track_name, tracks_id, tracks_popularity)

                
    elif response.status_code == 401:   
        print(f"{response.status_code} : 잘못되었거나 만료된 토큰입니다.")
        token = get_token(client_id,client_secret)
        print(f" ** 재발급 완료 **")
        get_audio_feature(token)

    elif response.status_code == 429:    
        print(f"{response.status_code} : 앱이 속도 제한을 초과하였습니다.")

    else:
        print(f"{response.status_code} : 검색 요청에 실패하였습니다.")

def isnone(data, true_case, false_case):
    """
    데이터가 None인 경우 true_case를 반환하고, 그렇지 않은 경우 false_case를 반환하는 함수입니다.
    """
    if data is None:
        return true_case
    else:
        return false_case
    

# 데이터 보기 쉽게 변환 
def split_data(json_response, track_name, tracks_id, tracks_popularity):
        data = json_response

         # 모든 앨범 데이터를 저장하기 위한 리스트 생성 
        track_len = len(data['audio_features'])
        extact_data = []
        acousticness, danceability, duration_ms, energy, instrumentalness = [],[],[],[],[]
        key, liveness, loudness, mode, speechiness, tempo, valence = [],[],[],[],[],[],[]


        # 앨범 리스트에 데이터 적재
        for i in range(track_len):
            acousticness.append(data['audio_features'][i]['acousticness'])
            danceability.append(data['audio_features'][i]['danceability'])
            duration_ms.append(data['audio_features'][i]['duration_ms'])
            energy.append(data['audio_features'][i]['energy'])
            instrumentalness.append(data['audio_features'][i]['instrumentalness'])

            key.append(data['audio_features'][i]['key'])
            liveness.append(data['audio_features'][i]['liveness'])
            loudness.append(data['audio_features'][i]['loudness'])
            mode.append(data['audio_features'][i]['mode'])
            speechiness.append(data['audio_features'][i]['speechiness'])
            tempo.append(data['audio_features'][i]['tempo'])
            valence.append(data['audio_features'][i]['valence'])

            feature = {
                "track_name": track_name[i]
                ,"tracks_id" : tracks_id[i]
                , "tracks_popularity" : tracks_popularity[i]

                ,"acousticness": acousticness[i]
                ,"danceability": danceability[i]
                ,"duration_ms": duration_ms[i]
                ,"energy": energy[i]
                ,"instrumentalness": instrumentalness[i]

                ,"key": key[i]
                ,"liveness": liveness[i]
                ,"loudness": loudness[i]
                ,"mode": mode[i]
                ,"speechiness": speechiness[i]
                ,"tempo": tempo[i]
                ,"valence": valence[i]
            }
            extact_data.append(feature)

        # 변수들을 딕셔너리로 구성하여 반환
        # print(extact_data)
        return extact_data

# 테스트 실행 
if __name__ == "__main__":
    track_name = ['Take Two','FAKE LOVE'] 
    tracks_id = ['5IAESfJjmOYu7cHyX557kz','4a9tbd947vo9K8Vti9JwcI'] 
    tracks_popularity = [88, 81]
    get_audio_feature(token, track_name, tracks_id, tracks_popularity)

# acousticness, danceability, duration_ms, energy, instrumentalness, liveness, key, liveness, loudness, mode, speechiness, tempo, valence

# ** RETURN 예시 ** 
# {'audio_features': [{'acousticness': 0.158,
#                      'danceability': 0.71,
#                      'duration_ms': 201391,
#                      'energy': 0.879,
#                      'instrumentalness': 0.00142,
#                      'key': 0,
#                      'liveness': 0.439,
#                      'loudness': -4.218,
#                      'mode': 1,
#                      'speechiness': 0.0422,
#                      'tempo': 114.993,
#                      'valence': 0.341}]}