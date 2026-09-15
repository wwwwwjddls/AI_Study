'''
과제 1 — 합격자 찾기
점수가 80점 이상인 학생의 이름을 출력해.

철수 영희 지수

과제 2 — 평균 점수 구하기
전체 학생의 평균 점수를 구해서 출력해.

평균 점수: 83.0

과제 3 — 최고 점수 학생
가장 높은 점수를 받은 학생의 이름과 점수를 출력해.


최고 점수: 지수 95

과제 4 — 함수 만들기 ⭐
이번에는 함수를 만들어보자.
학생 데이터를 전달하면 평균 점수를 반환하는 함수를 만들어.

def get_average(students):
    # 여기에 작성
average = get_average(students)
print(f'평균 점수: {average}')

평균 점수: 83.0

과제 5 — AI 개발자식 데이터 처리 ⭐⭐
학생마다 grade를 추가해봐.

• 90점 이상 → A 
• 80점 이상 → B 
• 70점 이상 → C 
• 60점 이상 → D 
• 60점 미만 → F
{'name': '철수', 'score': 85, 'grade': 'B'}

철수 B 영희 A 민수 C 지수 A 현우 D
'''


students = [ 
    {'name': '철수', 'score': 85}, 
    {'name': '영희', 'score': 92}, 
    {'name': '민수', 'score': 78}, 
    {'name': '지수', 'score': 95}, 
    {'name': '현우', 'score': 65} 
]

# 과제 1
for student in students:
    if student['score'] >= 80:
        print(student['name'])
        
# 과제 2
avg = sum([student['score'] for student in students ])/len(students)
print(avg)

# 과제 3
max_score = 0
max_name  = ''

for student in students:
    if student['score'] > max_score:
        max_score = student['score']
        max_name  = student['name']

print(f'최고 점수: {max_name} {max_score}')


# 과제 4
def get_average(students):
    avg = sum([student['score'] for student in students ])/len(students)
    return avg
    
average = get_average(students)
print(f'평균 점수: {average}')

# 과제 5
for student in students:
    score = student['score']
    
    if score >= 90:
        student['grade'] = 'A'
    elif score >= 80:
        student['grade'] = 'B'
    elif score >= 70:
        student['grade'] = 'C'
    elif score >= 60:
        student['grade'] = 'D'
    else:
        student['grade'] = 'F'
        
    print(f'{student["name"]} {student["grade"]}')