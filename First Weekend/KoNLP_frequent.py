from konlpy.tag import Twitter
from collections import Counter


def get_tags(text, noun_count):
    spliter = Twitter()
    # konlpy의 Twitter객체
    nouns = spliter.nouns(text)
    # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    print(noun_count)

    for n, c in count.most_common(noun_count):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장합니다.
    return return_list


def main():
    # 분석할 파일
    noun_count = 20
    # 최대 많은 빈도수 부터 20개 명사 추출
    OpenFile = open('Medical Data4.txt', 'r')  # 디스크 # 통증 #흉터 #약 #파열 #상처 #화상 # 무릎 # 허리 # 어깨 # 발목 # 손목 # 치료
    # 분석할 파일을 open
    text = OpenFile.read()  # 파일을 읽습니다.
    tags = get_tags(text, noun_count)  # get_tags 함수 실행
    OpenFile.close()  # 파일 close


    for tag in tags:

        print("%s : %s" % (tag['tag'], tag['count']))

if __name__ == '__main__':
    main()