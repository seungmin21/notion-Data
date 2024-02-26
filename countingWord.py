# 파일 경로
file_path = "./testData.py"

# 파일 열기 (텍스트 모드로 읽기)
with open(file_path, "r", encoding="utf-8") as file:
    # 파일 내용 읽기
    data = file.read()

# 읽은 데이터에서 특정 단어를 카운트
target_words = ["Response", "request"]

word_counts = {}
for target_word in target_words:
    word_counts[target_word] = data.lower().count(target_word.lower())

#word_count = data.lower().count(target_word.lower())

# 결과 출력
for target_word, count in word_counts.items():
    print(f"파일에서 단어 '{target_word}'는 총 {count}번 출현합니다.")

#print(f"파일에서 단어 '{target_word}'는 총 {word_count}번 출현합니다.")
