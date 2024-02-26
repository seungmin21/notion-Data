# 3번의 클래스 선언은 notion-sdk 설치에만 존재
# notion-sdk-py v0.0.1 버전이기 때문에 clident가 없다.

from notion.client import NotionClient

# Notion API 토큰 설정
token_v2 = "secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY"

# Notion 페이지 URL (페이지 ID를 사용해도 됨)
notion_url = "https://www.notion.so/rrr-8c9d9a905a074adf8397951fd399a459"

# Notion Client 생성
client = NotionClient(token_v2=token_v2)

# Notion 페이지 열기
page = client.get_block(notion_url)

# Main 블록 찾기
main_block = None
for block in page.children:
    if block.title.lower() == "main":
        main_block = block
        break

# Main 블록이 있을 경우 텍스트 출력
if main_block:
    main_text = main_block.get_text()
    print("Main Text:", main_text)
else:
    print("Main Block not found.")
