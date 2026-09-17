'''
과제 1 — AI 관련 질문만 출력
category가 'ai'인 질문만 출력해봐.

머신러닝이 뭐야? 
LLM이 뭐야?


과제 2 — 카테고리별 질문 개수
각 카테고리의 질문 개수를 구해봐.

programming : 2 
finance : 2 
ai : 2


과제 3 — 카테고리 검색 함수
def get_questions_by_category(questions, category): # 작성
result = get_questions_by_category(questions, 'finance') print(result)


[
    {'question': '주식이 오를까?', 'category': 'finance'},
    {'question': '삼성전자 주가 알려줘', 'category': 'finance'}
]


과제 4 — 질문으로 카테고리 찾기
def get_category(questions, question): # 작성
print(get_category(questions, 'LLM이 뭐야?'))

ai  없으면 None

과제 5 ⭐ AI 개발 연결 문제
사용자가 질문을 하나 입력한다고 생각하자

user_question = '삼성전자 주가 알려줘'

1. 질문을 찾고 
2. 카테고리를 확인하고 
3. 다음처럼 출력하도록 만들어봐. 

질문: 삼성전자 주가 알려줘
카테고리: finance
'''

questions = [ 
    {'question': '파이썬이 뭐야?', 'category': 'programming'}, 
    {'question': '주식이 오를까?', 'category': 'finance'}, 
    {'question': '머신러닝이 뭐야?', 'category': 'ai'}, 
    {'question': '삼성전자 주가 알려줘', 'category': 'finance'}, 
    {'question': '리스트와 딕셔너리 차이는?', 'category': 'programming'}, 
    {'question': 'LLM이 뭐야?', 'category': 'ai'}, 
]

# 과제 1
ai_questions = [ question['question'] for question in questions if question['category'] == 'ai' ]
print(ai_questions)

# 과제 2
cnt_category = {}

for question in questions:
    category = question['category']
    cnt_category[category] = cnt_category.get(category, 0) + 1
       
for key, value in cnt_category.items():
    print(f'{key} : {value}')

# 과제 3
def get_questions_by_category(questions, category): 
    filter_questions = [ question for question in questions if question['category'] == category ]
    return filter_questions

result = get_questions_by_category(questions, 'finance')
print(result)

# 과제 4
def get_category(questions, question): 
    category = None
    
    for que in questions:
        if que['question'] == question:
            category = que['category']
            break
    
    return category
    
print(get_category(questions, 'LLM이 뭐야?'))

# 과제 5
user_question = '삼성전자 주가 알려줘'
user_category = get_category(questions, user_question)

print(f'질문: {user_question}\n카테고리: {user_category}')