'''
과제 1
각 사용자가 작성한 카테고리 종류를 중복 없이 출력해라.
예상 결과:

철수 : ['ai', 'web']
영희 : ['ai', 'python']
민수 : ['web', 'java']

과제 2
각 사용자가 작성한 질문 중 조회수가 300 이상인 질문의 개수를 구해라.
예상 결과:

철수 : 1
영희 : 3
민수 : 1

과제 3
각 카테고리별 전체 질문 개수를 구해라.
예상 결과:

ai : 4
web : 2
python : 1
java : 1


과제 4 ⭐
각 카테고리별 전체 조회수 합계를 구해라.
예상 결과:

ai : 1400
web : 500
python : 300
java : 180

과제 5 ⭐⭐
다음 함수를 만들어라.

def get_top_category(users):
    # 작성
조회수 합계가 가장 높은 카테고리와 그 조회수를 반환해라.
예상 결과:

ai : 1400

'''
users = [
    {
        "name": "철수",
        "questions": [
            {"title": "AI란 무엇인가?", "category": "ai", "views": 350},
            {"title": "머신러닝이란?", "category": "ai", "views": 200},
            {"title": "REST API란?", "category": "web", "views": 180}
        ]
    },
    {
        "name": "영희",
        "questions": [
            {"title": "LLM이란?", "category": "ai", "views": 500},
            {"title": "Python이란?", "category": "python", "views": 300},
            {"title": "RAG란?", "category": "ai", "views": 350}
        ]
    },
    {
        "name": "민수",
        "questions": [
            {"title": "REST API란?", "category": "web", "views": 320},
            {"title": "Spring이란?", "category": "java", "views": 180}
        ]
    }
]

# 과제 1
for user in users:
    question = [ q['category'] for q in user['questions'] ]
    print(f'{user["name"]} : {list(set(question))}')
    
# 과제 2
for user in users:
    question = [ q for q in user['questions'] if q['views'] >= 300 ]
    print(f'{user["name"]} : {len(question)}')
    
# 과제 3
category = {}

for user in users:
    for q in user['questions']:
        category[q['category']] = category.get(q['category'], 0) + 1

for key, value in category.items():
    print(f'{key} : {value}')
    
# 과제 4
category = {}

for user in users:
    for q in user['questions']:
        category[q['category']] = category.get(q['category'], 0) + q['views']

for key, value in category.items():
    print(f'{key} : {value}')
    
# 과제 5
def get_top_category(users):
    category = {}
    
    for user in users:
        for q in user['questions']:
            category[q['category']] = category.get(q['category'], 0) + q['views']
            
    return max(category.items(), key=lambda x: x[1])  
      
result = get_top_category(users);          
print(f'{result[0]} : {result[1]}')