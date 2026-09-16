'''
과제 1 — 등급 추가하기
각 학생에게 grade를 추가해줘.

[
    {'name': '철수', 'score': 95, 'grade': 'A'},
    ...
]

과제 2 — 평균 점수 함수
결과는 소수점 둘째 자리까지 출력되도록 해봐.

def get_average(students):
    # 여기를 작성
print(get_average(students))

과제 3 — 특정 등급 학생 찾기

def get_students_by_grade(students, grade): # 여기를 작성
print(get_students_by_grade(students, 'A'))

['철수', '지수']

과제 4 — 가장 어려운 문제
학생 데이터를 받아서 성적 통계를 반환하는 함수를 만들어봐.

def get_statistics(students): # 여기를 작성

{
    'average': 82.4,
    'max_score': 95,
    'min_score': 68,
    'max_student': '철수',
    'min_student': '현우'
}

'''
import math

students = [ 
    {'name': '철수', 'score': 95}, 
    {'name': '영희', 'score': 82}, 
    {'name': '민수', 'score': 76}, 
    {'name': '지수', 'score': 91}, 
    {'name': '현우', 'score': 68} 
]

# 과제 1
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
    
    print(student)
    
# 과제 2
def get_average(students):
    avg_score = sum([student['score'] for student in students])/len(students)
    
    return avg_score
    
print('{:.2f}'.format(get_average(students)))

# 과제 3
def get_students_by_grade(students, grade):
    
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
        
    return list(map(lambda y: y['name'], filter(lambda x: x['grade'] == grade, students)))
    
print(get_students_by_grade(students, 'A'))

# 과제 4
def get_statistics(students):
    avg_score = math.trunc(sum([student['score'] for student in students])/len(students)*100)/100
    arr = sorted(students, key=lambda x: x['score'], reverse=True)
    
    return {
        'average'     : avg_score,
        'max_score'   : arr[0]['score'],
        'min_score'   : arr[-1]['score'],
        'max_student' : arr[0]['name'],
        'min_student' : arr[-1]['name']
    }
    
print(get_statistics(students))