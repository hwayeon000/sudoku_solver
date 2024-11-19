import dotori, daramg
from daramg import CheckNumber
import copy

print("감자")


# 1. 스도쿠 문제 입력
# p = problem
# problem and answer
p = [[0,1,0,9,0,0,0,8,7], 
     [0,0,0,2,0,0,0,0,6],
     [0,0,0,0,0,3,2,1,0],
     [0,0,1,0,4,5,0,0,0],
     [0,0,2,1,0,8,9,0,0],
     [0,0,0,3,2,0,6,0,0],
     [0,9,3,8,0,0,0,0,0],
     [7,0,0,0,0,1,0,0,0],
     [5,8,0,0,0,6,0,9,0]]

a = [[2,1,5,9,6,4,3,8,7], 
     [8,3,9,2,1,7,4,5,6], 
     [6,4,7,5,8,3,2,1,9], 
     [9,7,1,6,4,5,8,2,3], 
     [3,6,2,1,7,8,9,4,5], 
     [4,5,8,3,2,9,6,7,1], 
     [1,9,3,8,5,2,7,6,4], 
     [7,2,6,4,9,1,5,3,8], 
     [5,8,4,7,3,6,1,9,2]]

# 2. 문제 풀기

#   1) 바로 풀 수 있으면 다 풀기
#   2) 바로 풀 수 없으면 하나씩 대입
#   3) 모순을 발견하면 가장 최근에 대입했던 곳으로 돌아가기(스택을 사용)


# 3. 푼 결과 출력

# __main__ 블록
if __name__ == "__main__":
    # 원래 문제 출력
    print("스도쿠 문제:")
    for row in p:
        print(row)

    # 도토리 알고리즘 실행
    p_dotori = copy.deepcopy(p)
    dotori.solve(p_dotori)


    # 다람쥐 알고리즘 실행
    p_daramg = copy.deepcopy(p)
    
    daramg.solve(p_daramg)
    p2 = CheckNumber(p_daramg)
    p2.devide()
    p2.solvee()
    p2.printP()
    # 원본이 바뀌었는지 확인
    print(p2.p == a)  # False여야 원본이 변경되지 않은 것

            