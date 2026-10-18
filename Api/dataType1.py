'''
과제 1. 자료형 확인
views의 자료형을 출력하는 코드를 작성해 봐.
힌트: type() 함수

과제 2. 문자열을 숫자로 변환
views를 정수형으로 변환한 뒤 다시 딕셔너리에 저장해 봐.
힌트: int() 함수

과제 3. 조건 검사
변환한 조회수가 500 이상이면 인기 질문입니다., 아니면 일반 질문입니다.를 출력해 봐.
힌트: if / else

'''

question = {
    'title': 'RAG 입문',
    'category': 'ai',
    'views': '800'
}

# 과제 1
v_type = type(question['views'])
print(v_type)

# 과제 2
number_views = int(question['views'])
question['views'] = number_views
print(question)

# 과제 3
if question['views'] >= 500:
    print('인기 질문입니다.')
else:
    print('일반 질문입니다.')
