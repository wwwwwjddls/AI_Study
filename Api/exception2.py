'''
과제 1. 조회수 검증 함수 만들기

check_views(views) 함수를 작성해 봐.
- '800'을 전달하면 인기 질문입니다. 출력
- '200'을 전달하면 일반 질문입니다. 출력
- 'abc'를 전달하면 조회수는 숫자여야 합니다. 출력
- '-10'을 전달하면 조회수는 0 이상이어야 합니다. 출력

과제 2. 다음 리스트의 각 조회수를 check_views() 함수에 전달하고 결과를 출력해 봐.
views_list = ['800', '200', 'abc', '-10']

과제 3. 결과를 변수에 저장하고 활용하는 방법을 배워 보자.

과제 4. results 리스트에서 인기 질문이 몇 개인지 세는 코드를 작성해 봐.

과제 5. 결과를 딕셔너리로 집계하기
지금까지는 인기 질문의 개수만 세었어. 이번에는 결과별 개수를 모두 집계해 보자.
'''
# 과제 1
def check_views(views):
    result = ''
    
    try:
        number_views = int(views)
        
        if number_views < 0:
            result = '조회수는 0 이상이어야 합니다.'
        elif number_views == 200:
            result = '일반 질문입니다.'
        elif number_views == 800:
            result = '인기 질문입니다.'
        
    except ValueError:
        result = '조회수는 숫자여야 합니다.'
        
    return result

# 과제 2
views_list = ['800', '200', 'abc', '-10']

for views in views_list:
    print(check_views(views))
    
# 과제 3
results = []

for views in views_list:
    results.append(check_views(views))
    
print(results)

# 과제 4
count = 0

for views in views_list:
    result = check_views(views)
    
    if result == '인기 질문입니다.':
        count += 1
        
print(count)

# 과제 5
results = {}

for views in views_list:
    result = check_views(views)

    results[result] = results.get(result, 0) + 1
    
print(results)