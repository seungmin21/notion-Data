import requests

notion_token = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY'
notion_id = "8c9d9a905a074adf8397951fd399a459"

headers = {
    'Authorization' : f'Bearer {notion_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}

response = requests.get(f'https://api.notion.com/v1/blocks/{notion_id}', headers=headers)

if response.status_code == 200:
    page_data = response.json()
    print(page_data)
else:
    print(f"Failed to fetch Notion page. Status code: {response.status_code}")
    print(response.text)