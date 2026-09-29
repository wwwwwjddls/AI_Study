'''
과제 1 — AI 질문만 추출
category가 ai인 질문의 question 값만 리스트로 만들어라.
예상 결과:

['LLM이란?', 'RAG란?', '임베딩이란?']


과제 2 — 조회수 200 이상인 질문만 추출
views가 200 이상인 데이터만 추출하라.
결과에는 전체 dictionary가 들어가야 한다.


과제 3 — AI 질문을 조회수 내림차순으로 정렬
조건:
	• category == 'ai' 
	• views가 높은 순서 
예상 순서:

RAG란?       450
LLM이란?     320
임베딩이란?  280


과제 4 — 카테고리별 평균 조회수
결과를 다음과 같은 dictionary로 만들어라.

{
    'ai': ...,
    'java': ...,
    'db': ...
}

⭐ 과제 5 — 함수로 만들기
아래 함수를 완성해라.

def get_questions(category, min_views):
    # 여기에 작성
예를 들어:

get_questions('ai', 300)
실행하면

LLM이란? 320
RAG란? 450
'''

questions = [
    {'id': 1, 'category': 'ai', 'question': 'LLM이란?', 'views': 320},
    {'id': 2, 'category': 'java', 'question': '상속이란?', 'views': 180},
    {'id': 3, 'category': 'ai', 'question': 'RAG란?', 'views': 450},
    {'id': 4, 'category': 'db', 'question': '인덱스란?', 'views': 220},
    {'id': 5, 'category': 'ai', 'question': '임베딩이란?', 'views': 280},
    {'id': 6, 'category': 'java', 'question': '스레드란?', 'views': 150},
]

# 과제 1
filter_ai_questions = [ question['question'] for question in questions if question['category'] == 'ai' ]
print(filter_ai_questions)

# 과제 2
filter_200_questions = [ question for question in questions if question['views'] >= 200 ]
print(filter_200_questions)

# 과제 3
sort_ai_questions = sorted([ question for question in questions if question['category'] == 'ai' ], key=lambda x: x['views'], reverse=True)
print(sort_ai_questions)

# 과제 4
avg_category = {}
cnt_category = {}

for question in questions:
    category = question['category']
    
    avg_category[category] = avg_category.get(category, 0) + question['views']
    cnt_category[category] = cnt_category.get(category, 0) + 1
    
avg_category = dict(map(lambda x: (x[0], x[1]/cnt_category.get(x[0])), avg_category.items()))
print(avg_category)

# 과제 5
def get_questions(category, min_views):
    result = ''
    
    for question in questions:
        if question['category'] == category and question['views'] >= min_views:
            result += '{} {}\n'.format(question['question'], question['views'])
        
    return result
    
print(get_questions('ai', 300))