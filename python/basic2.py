'''
과제 1
80점 이상 학생 찾기

철수 영희 지수

과제 2
최고 점수 학생 찾기

최고 점수 학생: 지수 점수: 98

과제 3
평균 점수 함수 만들기

def get_average(students): # 여기에 작성
average = get_average(students) print(average)
83.0

과제 4 - AI 개발자 관점의 작은 응용
학생의 점수를 입력하면 등급을 반환하는 함수를 만들어봐.

def get_grade(score): # 여기에 작성

90점 이상 → A 80점 이상 → B 70점 이상 → C 60점 이상 → D 60점 미만 → F

print(get_grade(92)) print(get_grade(76)) print(get_grade(55))
A C F
'''
students = [ 
    {"name": "철수", "score": 85}, 
    {"name": "영희", "score": 92}, 
    {"name": "민수", "score": 76}, 
    {"name": "지수", "score": 98}, 
    {"name": "현우", "score": 64} 
]

# 과제 1
for student in students:
    if 80 <= student['score']:
        print(student['name'])
        
# 과제 2
max_score = 0
max_name  = ''
for student in students:
    if max_score < student['score']:
        max_name  = student['name']
        max_score = student['score']
        
        
print(f'최고 점수 학생: {max_name} 점수: {max_score}')

# 과제 3
def get_average(students):
    answer = sum([ student['score'] for student in students ])/len(students)
    return answer
    
average = get_average(students)
print(average)

# 과제 4
def get_grade(score):
    answer = ''
    
    if(90 <= score):
        answer = 'A'
    elif(80 <= score):
        answer = 'B'
    elif(70 <= score):
        answer = 'C'
    elif(60 <= score):
        answer = 'D'
    else:
        answer = 'F'    
    
    return answer

print(get_grade(92))
print(get_grade(76))
print(get_grade(55))