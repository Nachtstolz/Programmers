# 포켓몬 # 성공
# 문제 링크 | https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    
    n = len(nums)
    answer = n//2
    
    tmp_set = set(nums)
    # print(tmp_set)
    if len(tmp_set) < answer : 
        answer = len(tmp_set)
    
    return answer