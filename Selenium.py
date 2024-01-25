from selenium import webdriver

# Chrome 드라이버 초기화 (executable_path 전달하지 않음)
driver = webdriver.Chrome()

# 구글 홈페이지 열기
driver.get('https://www.google.com')

# 브라우저 닫기
driver.quit()

# 라이브러리 업데이트로 인해 타입 에러가 발생하는 작성법
# driver = webdriver.Chrome(executable_path=driver_path)