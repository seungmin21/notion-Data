from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome 드라이버 초기화 (executable_path 전달하지 않음)
driver = webdriver.Chrome()

# 구글 홈페이지 열기
notion_url = 'https://www.notion.so/1-24-9bc07fb161084184b54fc6dc14e1f32a'
driver.get(notion_url)

# 웹 페이지가 완전히 로딩될 때까지 대기
WebDriverWait(driver, 10).until(EC.title_contains('Expected Title'))

driver.quit()