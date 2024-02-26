import requests

notion_token = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY'
notion_id = "24219f95488346d4a2848161330ab506"

headers = {
    'Authorization' : f'Bearer {notion_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}

# response = requests.get(f'https://api.notion.com/v1/pages/{notion_id}', headers=headers)
endpoint_url = f'https://api.notion.com/v1/pages/{notion_id}/blocks'
response = requests.get(endpoint_url, headers=headers)
data = response.json()

# 블록 데이터 처리
if 'results' in data:
    blocks = data['results']
    for block in blocks:
        # 블록 데이터를 원하는 방식으로 처리
        block_id = block['id']
        block_type = block['type']
        print(f'Block ID: {block_id}, Block Type: {block_type}')
else:
    print('No blocks found in the response.')

# if response.status_code == 200:
    # page_data = response.json()
    # print(page_data)
# else:
    # print(f"Failed to fetch Notion page. Status code: {response.status_code}")
    # print(response.text)