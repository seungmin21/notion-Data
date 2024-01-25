from selenium import webdriver

# Chrome 드라이버 초기화 (executable_path 전달하지 않음)
driver = webdriver.Chrome()

# 구글 홈페이지 열기
driver.get('https://www.google.com')

# 브라우저 닫기
driver.quit()