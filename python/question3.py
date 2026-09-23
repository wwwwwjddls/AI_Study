'''
과제 1 — 카테고리별 질문 개수
category별 질문 개수를 구해라.
ai : 3 python : 3


과제 2 — 조회수가 가장 높은 질문
views가 가장 높은 질문의 질문 내용과 조회수를 출력해라.
결과:

LLM이란? : 350

과제 3 — 특정 키워드 검색 함수
다음과 같은 함수를 만들어라.

search_questions(keyword)


search_questions('AI')
를 실행하면 질문에 'AI'가 포함된 데이터를 찾아 반환한다.
힌트

과제 4 — 카테고리 + 최소 조회수 조건
다음 함수를 만들어라.

get_questions(category, min_views)
예를 들어

get_questions('ai', 200)
를 실행하면:

LLM이란? : 350
머신러닝이란? : 280
만 나오도록 만들어라.
조건은 두 가지다.

category가 일치
AND
views가 min_views 이상

과제 5 ⭐ — 조회수 내림차순 정렬
4번의 결과를 조회수가 높은 순서대로 정렬해라.
예:

LLM이란? : 350
머신러닝이란? : 280
AI란 무엇인가? : 120

'''
questions = [ 
    {'question': 'AI란 무엇인가?', 'category': 'ai', 'views': 120}, 
    {'question': '파이썬이란?', 'category': 'python', 'views': 200}, 
    {'question': 'LLM이란?', 'category': 'ai', 'views': 350}, 
    {'question': '리스트와 튜플 차이', 'category': 'python', 'views': 180}, 
    {'question': '머신러닝이란?', 'category': 'ai', 'views': 280}, 
    {'question': '딕셔너리 사용법', 'category': 'python', 'views': 150}, 
]

# 과제 1
category_cnt = {}

for question in questions:
    category = question['category']
    category_cnt[category] = category_cnt.get(category, 0) + 1
    
for key, value in category_cnt.items():
    print(f'{key} : {value}')
    
# 과제 2
sort_questions = sorted(questions, key=lambda x: x['views'])
max_views_question = sort_questions[-1]

print(f'{max_views_question["question"]} : {max_views_question["views"]}')

# 과제 3
def search_questions(keyword):
    result = []
    
    for question in questions:
        q = question['question']
        
        if keyword.lower() in q.lower():
            result.append(question)
            
    return result
    
print(search_questions('AI'))

# 과제 4
def get_questions(category, min_views):
    result = []
    
    for question in questions:
        if question['category'] == category and question['views'] >= min_views:
            result.append(question)
            
    return result
    
print(get_questions('ai', 200))

# 과제 5
sort_questions = sorted(get_questions('ai', 200), key=lambda x: x['views'], reverse=True)
print(sort_questions)