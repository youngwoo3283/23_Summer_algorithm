# my code
n = input() # 숫자 개수
number = list(str(input()).split(" ")) # 원래 성적
max_num = max(number) # 최대값 찾기
new_num = [] #수정한 점수를 담을 리스트
for i in number: # 점수 수정하기
    j = int(i) / int(max_num) * 100
    new_num.append(j)
print(sum(new_num) / n) # 새로운 평균 구하기

# answer
n = input()
mylist = list(map(int,input().split())) #원래 성적 : split한 뒤, int로 받음
mymax = max(mylist) #최대값 구하기
mysum = sum(mylist) #평균만 계산하면 되기 때문에 일일히 수정하지 말고 총합을 변경한다
print(mysum / mymax / int(n) * 100)

# retry
n = input()
number = list(map(int, input().split())) # 틀린 부분1
max_num = max(number)
mysum = sum(number)
print(mysum / max_num / int(n) * 100)