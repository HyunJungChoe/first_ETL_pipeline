
from google.cloud import bigquery

def export_data() :
    # 인증 설정
    credentials = "de-myproject-service-key.json"  # 서비스 계정 키 파일 경로
    client = bigquery.Client.from_service_account_json(credentials)

    # 데이터 추출할 쿼리 작성
    query = """
    SELECT artist_name, artist_id 
    FROM `de-myproject-202306.spotify_DB.artist` 
    LIMIT 100;
    """

    # 쿼리 실행하여 결과 추출
    query_job = client.query(query)
    results = query_job.result()

    # 결과 처리
    rows = list(results)

    artistid_list = []
    for row in rows:
        artistid_list.append(row[1])

    # print(artistid_list)
    return artistid_list

