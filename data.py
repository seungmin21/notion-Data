import requests

notion_api_url = "https://api.notion.com/v1/"

notion_page_url = "https://www.notion.so/7bd203b757444d8aab7c7a7c7e437158?p=41d7fe9d6e8944feb7dc9d1191c33953&pm=s"

integration_token = "secret_fGEHGgDIMujaJJ3XxWXonCPOu7GYF8G1GpHPEGDIvvS"

headers = {
  "Authorization": f"Bearer {integration_token}",
  "Notion-Version": "2.37.23.13.0.79"
}

# 페이지 정보를 가져오기 위한 요청
response = requests.get(f"{notion_api_url}{notion_page_url}", headers=headers)

# 응답을 JSON 형식으로 파싱
data = response.json()

# 추출한 데이터 출력
print(data)