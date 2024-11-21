from daramg import CheckNumber, solve
import copy

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

p2 = [[0,5,0,0,0,1,0,0,0],
      [0,0,2,0,0,0,0,0,6],
      [9,0,0,0,0,8,0,0,0],
      [0,0,6,4,0,0,0,0,0],
      [0,8,0,0,0,0,7,1,0],
      [0,0,0,0,0,0,0,9,0],
      [0,0,0,2,0,0,0,0,0],
      [0,3,0,6,0,0,0,0,0], 
      [1,0,0,0,0,0,0,4,0]]

a2 = [[6,5,3,7,2,1,4,8,9], 
      [8,7,2,9,4,5,1,3,6], 
      [9,4,1,3,6,8,5,2,7], 
      [7,1,6,4,9,2,3,5,8], 
      [4,8,9,5,3,6,7,1,2], 
      [3,2,5,1,8,7,6,9,4], 
      [5,9,4,2,7,3,8,6,1], 
      [2,3,8,6,1,4,9,7,5], 
      [1,6,7,8,5,9,2,4,3]]

# __main__ 블록
if __name__ == "__main__":
    # 원본 문제 유지
    p_daramg = copy.deepcopy(p2)
    # 다람쥐 알고리즘 실행
    solve(p_daramg)
    daram = CheckNumber(p_daramg)
    daram.devide()
    daram.solvee()
    daram.printP()
#     daram.liflif()
    # 원본이 바뀌었는지 확인
    print(daram.p == p2)  # False여야 원본이 변경되지 않은 것
    
#     aa=[[]]
#     if not aa[0]:
#           print(aa[0])
    # aa=[[123]]
    # ppp=[[123],[234],[456]]
    # d=[1,2,3]
    # d.append(ppp)
    # p = d[-1]
    # print(p)