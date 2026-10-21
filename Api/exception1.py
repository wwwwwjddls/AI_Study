'''
과제 1. 오류 확인하기
아래 코드를 실행하고 어떤 오류가 발생하는지 확인해 봐.

과제 2. 예외 처리하기
try / except를 사용해서 숫자로 변환할 수 없는 경우에도 프로그램이 종료되지 않도록 작성해 봐.

실행 결과는 다음과 같아야 해.
- views = '800' → 800 출력
- views = 'abc' → 조회수는 숫자여야 합니다. 출력

과제 3. 조회수 검증하기
과제 2의 코드를 확장해 봐.
- 조회수가 숫자라면 정수로 변환
- 변환한 조회수가 500 이상이면 인기 질문입니다. 출력
- 500 미만이면 일반 질문입니다. 출력
- 숫자가 아니라면 조회수는 숫자여야 합니다. 출력
우선 과제 1부터 실행해 보고 결과를 알려 줘. 결과를 확인한 뒤 과제 2로 넘어가자.

과제 4. 조회수가 0보다 작으면 조회수는 0 이상이어야 합니다.를 출력하도록 코드를 작성해 봐.

'''
question = {
    'title': 'RAG 입문',
    'category': 'ai',
    'views': 'abc'
}



# 과제 1
# eption has occurred: ValueError

views = 'abc'
number_views = int(views)
print(number_views)

# 과제 2
try:
    views = 'abc'
    number_views = int(views)
    print(number_views)
    
    views = '800'
    number_views = int(views)
    print(number_views)
    
except ValueError:
    print('조회수는 숫자여야 합니다.')
    
    
# 과제 3
try:
    number_views = int(question['views'])
    
    if number_views < 0:
        print('조회수는 0 이상이어야 합니다.')
    elif number_views >= 500:
        print('인기 질문입니다.')
    else:
        print('일반 질문입니다.')
    
except ValueError:
    print('조회수는 숫자여야 합니다.')