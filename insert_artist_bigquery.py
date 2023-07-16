from google.cloud import bigquery
from  get_acesstoken import get_token
from secret_key import *
from search_artist_id import *

# 데이터 삽입을 위한 빅쿼리 테이블 정보
project_id = 'de-myproject-202306'
dataset_id = 'spotify_DB'
table_id = 'artist'

# 인증 설정
credentials = "de-myproject-service-key.json"  # 서비스 계정 키 파일 경로
client = bigquery.Client.from_service_account_json(credentials)

# Spotify API 액세스 토큰/ 삽입할 데이터 가져오기
extact_data = search_artist_id(token)


# ------- 데이터 삽입 -------
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)


errors = client.insert_rows_json(table, extact_data)

if errors == []:
    print("데이터가 성공적으로 삽입되었습니다.")
else:
    print("데이터 삽입 중에 오류가 발생했습니다:", errors)

