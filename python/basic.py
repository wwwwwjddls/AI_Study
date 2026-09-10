'''
학생 성적 처리 프로그램

과제 1
학생들의 이름을 출력
철수 
영희 
민수 
지수

과제 2
평균 점수 계산
평균 점수: 85.0

과제 3
90점 이상인 학생만 출력
철수 90 
지수 95

과제 4 
90점 이상이면 "A"
80점 이상이면 "B"
70점 이상이면 "C"
그 이하는 "D" 로 만들어서

철수 A
영희 B
민수 C
'''

students = [
    {"name": "철수", "score": 90},
    {"name": "영희", "score": 85},
    {"name": "민수", "score": 70},
    {"name": "지수", "score": 95}
]

# 과제 1
for student in students:
    print(student['name'])

# 과제 2
avg_score = sum([student['score'] for student in students])
print(f'평균 점수: {avg_score / len(students)}')

# 과제 3
for student in students:
    score = student['score']
    
    if 90 <= score:
        print(f'{student["name"]} {student["score"]}')
    
# 과제 4
for student in students:
    score = student['score']
    grade = 'A' if 90 <= score else 'B' if 80 <= score else 'C' if 70 <= score else 'D'
    
    print(f'{student["name"]} {grade}')
