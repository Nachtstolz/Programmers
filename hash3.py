# 전화번호 목록 # 성공
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577#

def solution(phone_book):
    answer = True
    
    # 직접 비교 : 효율성 쓰레기

    '''
    # 길이 순으로 정렬
    phone_book.sort(key = lambda phone:len(phone))    

    for i in range(len(phone_book)) :
        length = len(phone_book[i])
        for j in range(i+1, len(phone_book)) :
            if phone_book[i] == phone_book[j][:length] :
                answer = False
                return answer
    '''
    
    ''' 정렬 -> 반복문 '''
    '''
    phone_book.sort()
    
    # 단방향 비교만 해도 괜찮다
    for i in range(len(phone_book)-1) :
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:length] :
            answer = False
            return answer
    '''
        
    ''' 해시 '''
    d = {}
    for phone in phone_book :
        d[phone] = 1 # 딕셔너리에 저장
    
    for phone in phone_book :
        front = ""
        for number in phone :
            front += number
            if front in d and front != phone :
                answer = False
                return answer

    return answer