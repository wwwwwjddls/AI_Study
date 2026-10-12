'''
과제 1. 사용자별 총 조회수 구하기
각 사용자가 작성한 모든 질문의 views를 더해서 출력해 봐.
예상 출력:
철수 : 1500
영희 : 1000
민수 : 450

민수 : 450


과제 2. 카테고리별 질문 개수 구하기
모든 사용자의 질문을 대상으로 카테고리별 질문 개수를 구해 봐.
예상 출력:
ai : 3
python : 3
cs : 1

과제 3. 가장 조회수가 높은 질문 찾기
모든 사용자의 질문 중 조회수가 가장 높은 질문의 제목과 조회수를 출력하는 함수를 만들어 봐.
함수 이름은 get_top_question(users)로 해 보자.
예상 출력:
RAG 입문 : 800
'''
users = [
    {
        'name': '철수',
        'questions': [
            {'title': 'LLM 기초', 'category': 'ai', 'views': 500},
            {'title': 'Python 기초', 'category': 'python', 'views': 200},
            {'title': 'RAG 입문', 'category': 'ai', 'views': 800}
        ]
    },
    {
        'name': '영희',
        'questions': [
            {'title': 'FastAPI 입문', 'category': 'python', 'views': 400},
            {'title': 'LLM 활용', 'category': 'ai', 'views': 600}
        ]
    },
    {
        'name': '민수',
        'questions': [
            {'title': 'Python 함수', 'category': 'python', 'views': 300},
            {'title': '자료구조', 'category': 'cs', 'views': 150}
        ]
    }
]

# 과제 1
for user in users:
    cnt_views = sum([ q['views'] for q in user['questions'] ])
    print(f'{user["name"]} : {cnt_views}')
    
# 과제 2
category_cnt = {}

for user in users:
    for q in user['questions']:
        category_cnt[q['category']] = category_cnt.get(q['category'], 0) + 1
        
for key, value in category_cnt.items():
    print(f'{key} : {value}')
    
# 과제 3
def get_top_question(usrs):
    questions = []
    
    for user in users:
        questions += user['questions']

    max_q = max(questions, key=lambda x: x['views'])
    
    return f'{max_q["title"]} : {max_q["views"]}'
        
result = get_top_question(users)
print(result)