'''
과제 1. 딕셔너리를 JSON 문자열로 변환하기
Python의 json 모듈을 사용해서 다음 데이터를 JSON 문자열로 변환해 봐.
import jsonquestion = {    'title': 'RAG 입문',    'category': 'ai',    'views': 800}



조건:
- json.dumps()를 사용해.
- 변환한 결과를 json_data 변수에 저장해.
- print()로 결과를 출력해.

과제 2. JSON 문자열에서 데이터 꺼내기
이번에는 JSON 문자열을 Python 딕셔너리로 변환해 보자.
json_data = '{"title": "RAG 입문", "category": "ai", "views": 800}'



조건:
- json.loads()를 사용해.
- 변환 결과에서 title과 views를 출력해.
- 예상 출력은 다음과 같아.
RAG 입문
800

과제 3. 함수 만들기
AI 서버에서 사용할 수 있는 간단한 데이터 변환 함수를 만들어 보자.
def question_to_json(question):    # 여기에 작성



조건:
- question 딕셔너리를 매개변수로 받는다.
- JSON 문자열로 변환한다.
- 변환한 JSON 문자열을 return한다.
- 함수 안에서는 print()하지 않는다.
예를 들어 question_to_json(question)을 호출하면 해당 질문의 JSON 문자열이 반환되어야 해.
'''

# 과제 1
import json

question = {
    'title': 'RAG 입문',
    'category': 'ai',
    'views': 800
}

json_data = json.dumps(question)
print(json_data)

# 과제 2
data = json.loads(json_data)
print(f'{data["title"]}\n{data["views"]}')

# 과제 3
def question_to_json(question):
    json_data = json.dumps(question)
    return json_data
    
result = question_to_json(question)
print(result)