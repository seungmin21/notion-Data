import requests

notion_token = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY'
notion_id = "8c9d9a905a074adf8397951fd399a459"

headers = {
    'Authorization' : f'Bearer {notion_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',
}

response = requests.get(f'https://api.notion.com/v1/pages/{notion_id}', headers=headers)

if response.status_code == 200:
    page_data = response.json()

    # 페이지의 "main" 내용 출력
    if 'main' in page_data.get('properties', {}):
        main_block_id = page_data['properties']['main'][0]['id']
        children = [block for block in page_data.get('children', []) if block.get('parent_id') == main_block_id]

        for child in children:
            if child['object'] == 'block' and child['type'] == 'paragraph':
                text = child.get('paragraph', {}).get('text', [])
                if text:
                    # Find the div block within the paragraph
                    div_block = next((span for span in text if span.get('type') == 'div'), None)

                    if div_block:
                        div_text = div_block.get('text', [])
                        if div_text:
                            print(f"Div Text: {div_text[0]['plain_text']}")
    else:
        print("No 'main' block found on the page.")

else:
    print(f"Failed to fetch Notion page. Status code: {response.status_code}")
    print(response.text)
