'''
과제 1 — 점수순으로 정렬
학생들을 점수가 높은 순서로 정렬해서 출력해봐.

지수 95 영희 92 준호 88 철수 85 민수 78 현우 65

과제 2 — 80점 이상만 추출
80점 이상인 학생만 새로운 리스트로 만들어봐.

[
    {'name': '철수', 'score': 85},
    {'name': '영희', 'score': 92},
    {'name': '지수', 'score': 95},
    {'name': '준호', 'score': 88}
]

과제 3 — 상위 3명 ⭐
점수가 높은 순서로 정렬한 뒤 상위 3명만 출력해봐.

지수 95 영희 92 준호 88

과제 4 — 함수 만들기 ⭐⭐
아래 함수를 완성해봐.
count에 3을 넣으면 상위 3명, 2를 넣으면 상위 2명이 나오도록 만들어야 해.

def get_top_students(students, count): # 여기에 작성 top_students = get_top_students(students, 3) for student in top_students: print(student['name'], student['score'])

과제 5 — 조금 더 AI 개발자스럽게 ⭐⭐⭐
평균 점수 이상인 학생들만 점수순으로 반환하는 함수를 만들어봐.

def get_above_average_students(students): # 여기에 작성

지수 95 영희 92 준호 88 철수 85
'''
students = [ 
    {'name': '철수', 'score': 85}, 
    {'name': '영희', 'score': 92}, 
    {'name': '민수', 'score': 78}, 
    {'name': '지수', 'score': 95}, 
    {'name': '현우', 'score': 65}, 
    {'name': '준호', 'score': 88} 
]

# 과제 1
sort_students = sorted(students, key=lambda x: x['score'], reverse=True)
print(sort_students)

# 과제 2
filter_students = []

for student in students:
    if student['score'] >= 80:
        filter_students.append(student)
        
print(filter_students)

# 과제 3
sort_students = sorted(students, key=lambda x: x['score'], reverse=True)
print(sort_students[:3])


# 과제 4
def get_top_students(students, count):
    output = sorted(students, key=lambda x: x['score'], reverse=True)
    
    return output[:count]
    
top_students = get_top_students(students, 3) 

for student in top_students: 
    print(student['name'], student['score'])
    
# 과제 5
def get_above_average_students(students):
    avg_score = sum([student['score'] for student in students])/len(students)
    output    = sorted(filter(lambda x: x['score'] >= avg_score, students), key=lambda x: x['score'], reverse=True)
    
    return output
        
avg_student = get_above_average_students(students)

for student in avg_student:
    print(student['name'], student['score'])