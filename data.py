import requests

# 노션 페이지의 ID와 통합 토큰 설정
page_id = 'd15140f3-942b-4a63-bed4-a0c3cd54556f'
notion_api_token = 'Bearer secret_VbYBREnh0zg7G60GIfpeQgBC8sCkoGb0zWqAOhy925u'

# 노션 API 엔드포인트와 헤더 설정
url = f'https://api.notion.com/v1/pages/{page_id}'
headers = {
    'Authorization': notion_api_token,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',  # 유효한 Notion API 버전 사용
}

# API 요청 보내기
response = requests.get(url, headers=headers)

# 응답 확인
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")
