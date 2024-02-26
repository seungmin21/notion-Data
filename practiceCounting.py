file_path = "./testData.py"

# encording은 사용할 수 없는 단어
# encoding으로 작성해야한다.
with open(file_path, "r", encoding="utf-8") as file:
    data = file.read()

target = "id"

#소문자 변환
counting = data.lower().count(target.lower())

#대문자 변환
counting = data.upper().count(target.upper())

#통일성이 없는 경우
counting = data.count(target)

print(f"지정한 파일에서 '{target}' {counting}개 입니다.")
