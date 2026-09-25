'''
과제 1
전체 사용자의 questions 합계를 구해봐.
예상 결과:

총 질문 수 : 57

과제 2
질문을 15개 이상 한 사용자만 찾아서 이름을 출력해봐.
예상 결과:

철수
민수


과제 3
questions가 가장 많은 사용자의 이름과 질문 수를 출력해봐.
예상 결과:

민수 : 22

과제 4 ⭐
다음 함수를 만들어봐.

def get_user_by_id(users, user_id):
    ...
user_id를 전달하면 해당 사용자의 정보를 반환하는 함수야.
예:

user = get_user_by_id(users, 3)
print(user)
결과:

{'id': 3, 'name': '민수', 'age': 31, 'questions': 22}

과제 5 ⭐⭐
다음 함수를 만들어봐.

def get_active_users(users, min_questions):
    ...
min_questions 이상 질문한 사용자만 List로 반환하는 함수야.
예:

active_users = get_active_users(users, 15)
print(active_users)

'''
users = [ 
    { 'id': 1, 'name': '철수', 'age': 28, 'questions': 15 }, 
    { 'id': 2, 'name': '영희', 'age': 24, 'questions': 8 }, 
    { 'id': 3, 'name': '민수', 'age': 31, 'questions': 22 }, 
    { 'id': 4, 'name': '지수', 'age': 26, 'questions': 12 } 
]

# 과제 1
sum_question = sum([ user['questions'] for user in users ])
print(sum_question)

# 과제 2
question_15 = [ user['name'] for user in users if user['questions'] >= 15 ]
for name in question_15:
    print(name)
    
# 과제 3
max_user = max(users, key=lambda x: x['questions'])
print(f'{max_user["name"]} : {max_user["questions"]}')

# 과제 4
def get_user_by_id(users, user_id):
    user = [ user for user in users if user['id'] == user_id ]
    return user
    
user = get_user_by_id(users, 3)
print(user)

# 과제 5
def get_active_users(users, min_questions):
    filter_user = [ user for user in users if user['questions'] >= min_questions ]
    return filter_user
    
active_users = get_active_users(users, 15)
print(active_users)

