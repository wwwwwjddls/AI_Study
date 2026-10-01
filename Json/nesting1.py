'''
과제 1
각 사용자가 작성한 질문의 총 개수를 출력해라.
예상 결과:

철수 : 3
영희 : 3
민수 : 2


과제 2
AI 카테고리 질문만 찾아서 다음 형태로 출력해라.

철수 : AI란 무엇인가?
철수 : 머신러닝이란?
영희 : LLM이란?

과제 3
각 사용자의 질문 중 조회수가 가장 높은 질문을 찾아라.
예상 결과:

철수 : AI란 무엇인가? (350)
영희 : LLM이란? (500)
민수 : REST API란? (320)


과제 4 ⭐
다음 함수를 만들어라.

def get_questions_by_category(users, category):
    # 작성
사용:

result = get_questions_by_category(users, 'ai')
print(result)
결과에는 AI 카테고리 질문들만 들어 있어야 한다.

각 사용자의 평균 조회수를 구하는 함수를 만들어라.

def get_average_views(users):
    # 작성
예상 결과:

철수 : 250.0
영희 : 383.33
민수 : 250.0
'''
users = [
    {
        'id': 1,
        'name': '철수',
        'questions': [
            {'title': 'Python 기초', 'category': 'python', 'views': 120},
            {'title': 'AI란 무엇인가?', 'category': 'ai', 'views': 350},
            {'title': '머신러닝이란?', 'category': 'ai', 'views': 280}
        ]
    },
    {
        'id': 2,
        'name': '영희',
        'questions': [
            {'title': 'Java 기본 문법', 'category': 'java', 'views': 200},
            {'title': 'Spring이란?', 'category': 'java', 'views': 450},
            {'title': 'LLM이란?', 'category': 'ai', 'views': 500}
        ]
    },
    {
        'id': 3,
        'name': '민수',
        'questions': [
            {'title': 'HTTP란?', 'category': 'web', 'views': 180},
            {'title': 'REST API란?', 'category': 'web', 'views': 320}
        ]
    }
]

# 과제 1
for user in users:
    print(f'{user["name"]} : {len(user['questions'])}')
    
# 과제 2
for user in users:
    ai_questions = [ question['title'] for question in user['questions'] if question['category'] == 'ai' ]
    
    for question in ai_questions:
        print(f'{user["name"]} : {question}')
        
# 과제 3
for user in users:
    max_views = max(user['questions'], key=lambda x: x['views'])
    print(f'{user["name"]} : {max_views["title"]} ({max_views["views"]})')

# 과제 4
def get_questions_by_category(users, category):
    result = []
    
    for user in users:
        ai_questions = [ question for question in user['questions'] if question['category'] == category ]
        result.extend(ai_questions)
        
    return result

result = get_questions_by_category(users, 'ai')
print(result)


# 과제 5
def get_average_views(users):
    result = ''
    
    for user in users:
        avg = sum([ question['views'] for question in user['questions'] ])/len(user['questions'])
        result += '{} : {}\n'.format(user['name'], round(avg, 2))
        
    return result   
        
result = get_average_views(users)
print(result)