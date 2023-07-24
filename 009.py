'''
손코드

데이터 입력 
a,b
문자열리스트
x,y,z,k


길이를 n이라고 하고 막대의 길이를 4라고 하면 n-4 + 1 즉 n - 3
>> n - m + 1 만큼의 슬라이딩을 해서 이거만큼 반복

for i in range(n-m+1):
    시작인덱스:4로 들어가서 개수세기


--- 해답 ---


2개의 함수 구현 해당하는 슬라이더에 들어있는 데이터를 세는 함수
슬라이더에서 빠지면서 데이터의 개수를 빼는 함수

몇개를 충족했는지 세기 위해서 0으로 채워진 길이를 맞춰서 만족될때마다 하나씩 더하기

데이터는 고유 4개이니 4를 충족하면 모두 만족하는 것 만약 3이면 1개의 데이터 개수가 부족함


    



'''


checkArr = [0] * 4
myArr = [0] * 4
checkSecret = 0

# 함수 정의
def myadd(c): #새로 들어온 문자를 처리하는 함수
    global checkArr,myArr,checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

def myremove(c): #제거되는 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkArr = list(map(int, input().split()))
for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1


for i in range(P):  #초기 P 부분 문자열 처리 부분 이후 하나씩 앞으로 가면서 더하고 뻄
    myadd(A[i])


if checkSecret == 4: #4자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    Result += 1


for i in range(P, S): # P 10 S 20이라고 하면 J는 일단 0,1,2,3 이렇게 하나씩 올라감
    j = i - P         # 해당 요소에서 한개씩 더해지고 앞에서 한개씩 빼지면서 개수를 세기
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1
print(Result)