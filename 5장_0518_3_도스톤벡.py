'''
작성일: 2023년 5월 18일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 사용자로부터 입력받은 숫자에 해당하는 구구단을 출력하는 프로그램을 for문을 사용하여 
작성하시오. 또한 같은 문제를 while문으로도 작성하여 비교하시오.
'''


# for문을 이용한 구구단 출력
dan = int(input("출력을 원하는 단을 입력 : "))

print("***",dan,"단 ***")          # 단 제목을 출력

for i in range(1,10) :             # 1부터 9까지 반복
    
    print(dan,"*", i, "=",dan*i)   # 구구단 출력
    
    
    
    
    


# while문을 이용한 구구단 출력
dan = int(input("출력을 원하는 단을 입력 : "))

i = i                               # 변수 초기화
print("***",dan,"단 ***")           # 단 제목 출력

while i <=9 :                       # 9 보다 작거나 같을 때까지 반복
    print(dan,"*", i, "=",dan * i)  # 구구단 출력
    i = i +i                        # 변수값 증가
