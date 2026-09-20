'''
과제 1 — filter
views가 200 이상인 질문만 출력해봐.

과제 2 — lambda
각 질문에서 question 내용만 뽑아서 리스트로 만들어봐.

[ '삼성전자 주가 알려줘', 'LLM이 뭐야?', ... ]


과제 3 — sorted
views가 높은 순서 → 낮은 순서로 정렬해봐.


과제 4 — 함수 만들기 ⭐
다음 함수를 만들어봐.
하면 조회수가 200 이상인 데이터만 반환하도록 만들어.

def get_questions_by_views(questions, min_views): # 여기에 작성
result = get_questions_by_views(questions, 200)
print(result)

과제 5 — 종합 ⭐⭐
함수를 하나 만들어봐.

def get_top_questions(questions, count): # 여기에 작성

• 조회수 기준 내림차순 정렬 
• 상위 count개만 반환

결과는 조회수가 높은 질문 3개가 되어야 해.
result = get_top_questions(questions, 3) 
print(result)
'''

questions = [ 
    {'question': '삼성전자 주가 알려줘', 'category': 'stock', 'views': 120}, 
    {'question': 'LLM이 뭐야?', 'category': 'ai', 'views': 250}, 
    {'question': '파이썬 리스트 설명해줘', 'category': 'python', 'views': 180}, 
    {'question': '비트코인 왜 올라?', 'category': 'crypto', 'views': 320}, 
    {'question': 'ChatGPT가 뭐야?', 'category': 'ai', 'views': 280}, 
    {'question': '딕셔너리 사용법 알려줘', 'category': 'python', 'views': 150} 
]

# 과제 1
filter_question = [ question for question in questions if question['views'] >= 200 ]
print(filter_question)

# 과제 2
filter_question = [ question['question'] for question in questions]
print(filter_question)

# 과제 3
sort_question = sorted(questions, key=lambda x: x['views'], reverse=True)
print(sort_question)

# 과제 4
def get_questions_by_views(questions, min_views):
    filter_question = [ question for question in questions if question['views'] >= min_views ]
    return filter_question
    
result = get_questions_by_views(questions, 200)
print(result)

# 과제 5
def get_top_questions(questions, count):
    sort_question = sorted(questions, key=lambda x: x['views'], reverse=True)
    return sort_question[:count]

result = get_top_questions(questions, 3) 
print(result)
    