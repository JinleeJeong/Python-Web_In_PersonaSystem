# ==========================1번============================
# a = ('이의덕,이재명,권종수,이재수,박철호,강동희,이재수,김지석,최승만,이성만,박영희,박수호,전경식,송우환,김재식,이유정,이김박')
#
# kim = 0
# park = 0
#
# names = a.split(",")
# for name in names:
#     if name.startswith('김'):
#         kim += 1
#     elif name.startswith('박'): # startswith('박', 2)
#         park += 1
#
# names = list(set(names))                                               # >>> 중복 삭제 list(set(x))
#
# print(kim, park)
# print(names.count('이재수'))
# print(names)
# print(sorted(names))
# ============================2번============================
# sum_1 = 0
# sum_2 = 0
# result_1 = 0
# result_2 = 0
# for i in range(101):
#     sum_1 = i * i
#     result_1 += sum_1
#
# for i in range(101):
#     sum_2 += i
# result_2 = sum_2 * sum_2
#
# print(result_2 - result_1)

# ============================3번============================= 100까지 숫자 별 갯수
# from collections import defaultdict
#
# d = defaultdict(int)
# for number in range(1, 101):
#     for c in str(number):
#         d[c] += 1
#
# print(dict(d))
# ============================4번==============================
# data = "4546793"
#
# numbers = list(map(int, data))  # 숫자 문자열을 숫자 리스트로 변경
# result = []
#
# for i, num in enumerate(numbers): # 열거하는 enumerate 함수
#     result.append(str(num))
#     if i < len(numbers)-1:  # 다음수가 있다면
#         is_odd = num % 2 == 1  # 현재수가 홀수
#         is_next_odd = numbers[i+1] % 2 == 1  # 다음수가 홀수
#         if is_odd and is_next_odd: # 연속 홀수
#             result.append("-")
#         elif not is_odd and not is_next_odd: # 연속 짝수
#             result.append("*")
#
# print("".join(result))
#
# # >>> a = [1.2, 2.5, 3.7, 4.6]
# >>> a = list(map(int, a))                    # list map 함수
# >>> a
# [1, 2, 3, 4]

# =============================5번===============================
# def compress_string(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s:
#         if c!=_c:
#             _c = c
#             if cnt:
#                 result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt +=1
#     if cnt: result += str(cnt)
#     return result
#
# print (compress_string("aaabbcccccca"))

# =============================6번================================
# def chkDupNum(s):
#     result = [ ]
#     for num in s:
#         if num not in result:
#             result.append(num)
#         else:
#             return False
#     return len(result) == 10
#
# print (chkDupNum('6789012345'), chkDupNum('123433'))

# =============================7번==================================
# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#     '-.--':'Y','--..':'Z'
# }
#
# def morse(src):
#     result = []
#     for word in src.split("  "):
#         for char in word.split(" "):
#             result.append(dic[char])
#         result.append(" ")
#     return "".join(result)
#
#
# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

# ===============================8번===================================

# import re
# p = re.compile("a[.]{3,}b")
#
# print (p.match("a....b"))
# print (p.match("a.cccb"))

# ===============================10번===================================

# import re
# data = """
#     park 010-9999-9988
#     kim 010-9909-7789
#     lee 010-8789-7768
# """
#
#
# pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
# result = pat.sub("\g<1>-####", data)
# print (result)

# ===============================11번===================================

# import re
#
# pat = re.compile("\w+[@]\w+[.](?=net$|com$)")
#
# print (pat.match("pahkey@gmail.com"))
# print (pat.match("kim@daum.net"))
# print (pat.match("lee@myhome.co.kr"))

