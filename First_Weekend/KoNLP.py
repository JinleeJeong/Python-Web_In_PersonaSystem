from konlpy.tag import Komoran
from konlpy.utils import pprint
from konlpy.corpus import kolaw
from konlpy.corpus import kobill
komoran = Komoran()
print(komoran.morphs(u'우왕 코모란도 오픈소스가 되었어요'))
print(komoran.nouns(u'오픈소스에 관심 많은 멋진 개발자님들!'))
print(komoran.pos(u'한글형태소분석기 코모란 테스트 중 입니다.'))
pprint(komoran.pos(u'아버지 가방에 들어가신다'))

# c = kolaw.open('constitution.txt').read()
# d = kobill.open('1809890.txt').read()
# print(c[:120])
# print(d[:120])