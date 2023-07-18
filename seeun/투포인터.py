# 수들의 합5
N = int(input()) # n 입력
count, start, end, sum = 1,1,1, 1 #변수 초기화

while end != N: #마지막 숫자가 input과 같을 때까지 반복문 실행
    if sum == N: 
        count += 1 #count 횟수 증가
        end += 1 #종료 위치 1씩 증가
        sum += end #합계 = 기존 합계 + 종료 위치
        
    elif sum > N:
        sum -= start #합계 = 기존 합계 - 시작 위치
        start += 1 #시작 위치 1씩 증가
        
    else:
        end += 1 #종료 위치 1씩 증가
        sum += end #합계 = 기존 합계 + 종료 위치
        
print(count)

# 주몽의 명령
N = int(input()) # 재료 데이터
M = int(input()) #갑옷 : 재료 데이터 2개의 합이 갑dht이 되어야 한다
I = list(map(int, input().split())) # 재료들
I.sort() #재료 정렬
start = 0
end = N-1
count = 0

while start < end: #start와 end가 같아질 때까지 반복문 실행
    if I[start] + I[end] < M: #재료 데이터의 합이 갑옷보다 작은 경우
        start += 1 #시작 위치 1 증가
    elif I[start] + I[end] > M: #재료 데이터의 합이 갑옷보다 큰 경우
        end -= 1
    else: #정답 케이스 : count, start는 1씩 증가, end는 1씩 감소
        count += 1
        start += 1
        end -= 1

print(count)

# 좋은 수 구하기
## 좋은 수 = 다른 두 수의 합으로 표현되는 수
N = int(input()) #수의 개수
count = 0 # 좋은 수의 개수를 셀 수
A = list(map(int, input().split())) #수의 개수만큼 주어진 수
A.sort() #숫자 정렬

for k in range(N):
    start = 0 ; end = N-1 # 투 포인터 정의
    while start < end: #첫 번째가 두 번째보다 커지기 전까지 반복문 실행
        if A[start] + A[end] == A[k]: # 두 수의 합이 특정 수인 경우
            if (start != k) and (end != k): #자기 자신이 아니라면
                count += 1 #좋은 수의 개수 증가
                break
            elif start == k: #시작 위치가 자기 자신인 경우 포인터 변경
                start += 1
            elif end == k: #종료 위치가 자기 자신인 경우
                end -= 1
        elif A[start] + A[end] < A[k]: # 두 수의 합이 찾는 수보다 작은 경우
            start += 1 #시작 위치 변경
        else: #두 수의 합이 찾는 수보다 큰 경우
            end -= 1

print(count)