import requests

notion_token = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY'
block_id = "24219f95-4883-46d4-a284-8161330ab506"  # 가져올 자식 블록들이 있는 블록의 ID를 여기에 입력하세요

headers = {
    'Authorization' : f'Bearer {notion_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}

response = requests.get(f'https://api.notion.com/v1/blocks/{block_id}/children', headers=headers)

if response.status_code == 200:
    children_data = response.json()
    print(children_data)
else:
    print(f"Failed to fetch children blocks. Status code: {response.status_code}")
    print(response.text)
