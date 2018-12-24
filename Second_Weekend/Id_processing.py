import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data)) # sub(바꿀문자열, 대상 문자열)


# =======================================정규화======================================
# re 객체  + 1번 이상 반복 , * 0번 이상 반복, {m, n} m번 이상 반복 n 까지!!
# ? 있던지 없던지 >
# 0-9 A-Za-z
# \d \D \s \S \w \W 숫자 매치, 문자 매치, 숫자 문자 매치
# . \n을 제외한 모든 문자 매치 a[.]b a.b와만 매치

# re 모듈 4가지 메소드 제공 match(), search() - 매치 찾음, findall() - 매치하는 모든 것 ' ' ,  ' ' 이런식으로 나타남. , finditer() > iterator 객체로 리턴 match와 같은 객체값 리턴
# 컴파일 후 4가지 메소드 사용!  p = re.compile('[a-z]+') 숫자는 매치되지 않아 None 리턴
# m.group() m.start() m.end() m.span() < 범위!
# 정규식의 컴파일 옵션 > re.compile('a.b', re.DOTALL or re.S)
# re.DOTALL(S) > .은 \n을 포함하지 않음. \n포함하는 방법
# re.IGNORECASE(I) > 대소문자 구분 X Python 가능
# re.MULTILINE(M) > 여러 ^python 들어가있는 file > python 여러개 출력 가능
# re.VERBOSE(X) > 보기 편하게 함 # 주석 사용 가능 + whitespace 제거
# ^문자열 $문자열 > 처음과 끝을 나타내는 Meta문자 / 문자 자체를 위해서는 [^], [$], \^, \$
# \A는 ^와 비슷하지만, 그냥 처음 하나와만 매치 \Z는 마지막
# \b는 구분자의 역할, whitespace(보통) >>> p = re.compile(r'\bclass\b')
#                                       >>> print(p.search('no class at all'))
#                                       <_sre.SRE_Match object at 0x01F6F3D8>
# \B는 반대의 역할 구분 안됀경우만!
# 정규식을 group()으로 가능 grouping 가능
# (?P<그룹명>...)으로 그룹화된 것을 이름 작명 가능하다.