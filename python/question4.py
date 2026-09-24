'''
과제 1 — 조회수 평균
전체 질문의 평균 조회수를 구해라.
출력 예:

평균 조회수 : 202.85

과제 2 — 카테고리별 평균 조회수
카테고리별로 조회수 평균을 구해라.
원하는 형태:

stock : 135.0
ai : 230.0
python : 185.0
crypto : 320.0

과제 3 — 조회수가 200 이상인 질문만 추출
결과를 high_view_questions에 저장해라.

high_view_questions = [...]

그리고 질문 제목만 출력:

LLM이 무엇인가요?
비트코인이 왜 오르나요?
머신러닝과 딥러닝의 차이는?

과제 4 — 가장 인기 있는 카테고리 찾기 ⭐
카테고리별 조회수 합계를 구한 다음,
가장 조회수가 높은 카테고리를 찾아라.
예:

가장 인기 있는 카테고리 : ai
힌트:

category_views[category] = …

과제 5 — 함수 만들기 ⭐⭐
다음 함수를 만들어라.

def get_questions_by_category(questions, category):
    # 해당 카테고리의 질문만 반환
사용:

ai_questions = get_questions_by_category(questions, 'ai')

print(ai_questions)
결과에는 category == 'ai'인 질문만 들어가야 해.
'''
import math

questions = [
    {'id': 1, 'question': '삼성전자 주가가 오를까요?', 'category': 'stock', 'views': 120},
    {'id': 2, 'question': 'LLM이 무엇인가요?', 'category': 'ai', 'views': 250},
    {'id': 3, 'question': '파이썬 리스트와 튜플의 차이는?', 'category': 'python', 'views': 180},
    {'id': 4, 'question': '비트코인이 왜 오르나요?', 'category': 'crypto', 'views': 320},
    {'id': 5, 'question': '머신러닝과 딥러닝의 차이는?', 'category': 'ai', 'views': 210},
    {'id': 6, 'question': '삼성전자 배당금은 얼마인가요?', 'category': 'stock', 'views': 150},
    {'id': 7, 'question': '파이썬에서 딕셔너리란?', 'category': 'python', 'views': 190},
]

# 과제 1
avg_views = sum([ question['views'] for question in questions ])/len(questions)
print(f'평균 조회수 : {math.trunc(avg_views*100)/100}')

# 과제 2
summary = {}

for question in questions:
    sm = summary.setdefault(question['category'], {
        'cnt' : 0,
        'view': 0
    })
    
    sm['cnt']  += 1
    sm['view'] += question['views']
    
for key, value in summary.items():
    print(f'{key} : {value["view"]/value["cnt"]}')
    

# 과제 3
question_200 = [ question['question'] for question in questions if question['views'] >= 200 ]

for q200 in question_200:
    print(q200)

# 과제 4
max_question = max(summary, key=lambda x: summary[x]['view'])
print(max_question)

# 과제 5
def get_questions_by_category(questions, category):
    return list(filter(lambda x: x['category'] == category, questions))

ai_questions = get_questions_by_category(questions, 'ai')

print(ai_questions)