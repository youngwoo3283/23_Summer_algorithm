import sys #거의 보고 풀었음
input = sys.stdin.readline #input 재정의
n,m = map(int, input().split()) #데이터 개수, 질의 개수
N = list(map(int, input().split())) #구간합을 구할 대상 배열
M = [0] #합배열 저장할 배열
temp = 0

# 합배열 만들기
for i in N:
    temp += i #누적합
    M.append(temp) #첫 번째 요소는 0으로 남겨두고 합배열 생성

for _ in range(m):
    start, end = map(int, input().split()) #시작 번호와 끝 번호
    print(M[end] - M[start-1])