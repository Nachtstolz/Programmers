# 소수찾기 # 성공
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

def solution(numbers):
    answer = []
    
    li = list(numbers)
    # print(li)
    
    for i in range(1, len(numbers)+1) :
        per = set(permutations(li, i))
        # print(per)
        for j in per :
            tmp = int(''.join(j))
            # print(tmp)
            if tmp == 1 or tmp == 0:
                continue
            else : # 소수 판별 # 제곱근까지만 보면 됨
                prime = True
                for k in range(2, int(math.sqrt(tmp))+1) :
                    if tmp % k == 0 :
                        prime = False
                        break
                        
                if prime == True :
                    answer.append(tmp)        
                
    res = set(answer)
    # print(res)
    return len(res)