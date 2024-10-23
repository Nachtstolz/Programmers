# 타겟넘버 # 성공
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

answer = 0

def dfs(turn, target, numbers, idx, res) :
    # print(turn, idx, res)

    if idx == turn :
        if res == target :
            global answer
            answer+=1
        return
    
    dfs(turn, target, numbers, idx+1, res-numbers[idx])
    dfs(turn, target, numbers, idx+1, res+numbers[idx])
    
    


def solution(numbers, target):
    
    turn = len(numbers)
    # print(turn)
    # dfs 재귀
    dfs(turn, target, numbers, 1, -(numbers[0]))
    dfs(turn, target, numbers, 1, numbers[0])
    
    # print(answer)
    return answer

# solution([1,1,1,1,1], 3)