import requests

notion_token = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY'
block_id = "3972f73f-e894-4100-9d6a-d9b020e6c854"  # 블록의 자식 ID

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
