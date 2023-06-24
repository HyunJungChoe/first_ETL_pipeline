from google.cloud import bigquery

# 인증 정보 로드
credentials_path = '/path/to/service_account_key.json'
client = bigquery.Client.from_service_account_json(credentials_path)

# 삽입할 데이터 준비
data = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 28},
    # 추가 데이터 준비
]

# 데이터 삽입을 위한 빅쿼리 테이블 정보
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'
table_id = 'your-table-id'

# 데이터 삽입
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)
errors = client.insert_rows(table, data)

if errors == []:
    print("데이터가 성공적으로 삽입되었습니다.")
else:
    print("데이터 삽입 중에 오류가 발생했습니다:", errors)
