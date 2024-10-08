# K번째 수 # 성공
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for com in commands :
        i, j, k = com # i, j, k 분류하기
        tmp = sorted(array[i-1:j]) # 원하는 배열 추출 -> 정렬하기
        answer.append(tmp[k-1]) # k 번째 원소 찾아서 저장하기
        # print(answer)
    
    return answer