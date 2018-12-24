# import json
#
# j1 = {"name" : "진리",
#       "age" : "24",
#       "birth" : "0118",
#     } # Dictionary 정의
#
# s1 = json.dumps(j1)
# print(s1+'\n') # 보기 좋게 정렬 indent 들여쓰기 왼쪽 2
# print(json.dumps(j1, indent=2) + '\n')
#
# d1 = json.loads(s1) # Python 객체로 변환  load는 파일을 읽고, loads는 문자열을 읽는다.
# print(d1)

#=====================================================sorted
from operator import attrgetter, itemgetter


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return repr((self.name, self.age, self.grade))

student_objects = {
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
}
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
# result = sorted(student_objects, key=lambda student: student.age)
result = sorted(students, key=itemgetter(1),reverse=True) #reverse 역순
# result = sorted(student_objects, key=attrgetter('age'))
print(result)


# a = [5,3,1,4,2]    b = {"c":90, "b":45, "a": 88}
# sorted(a)          sorted(b)
# [1,2,3,4,5] 출력   ['a', 'b', 'c']



# ======================================================= json 요청 후 json File로 받아온다.
# import json
# import urllib.request
#
# url = "http://ip.jsontest.com"  # URL
#
# d = {'name': '홍길동', 'birth': '0525', 'age': 30}
# params = json.dumps(d).encode("utf-8")  # encode: 문자열을 바이트로 변환
# req = urllib.request.Request(url, data=params,
#                              headers={'content-type': 'application/json'})
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf8'))  # decode: 바이트를 문자열로 변환