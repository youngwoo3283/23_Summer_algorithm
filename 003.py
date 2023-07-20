#문제 003 구간합 구하기1 43
import sys


input = sys.stdin.readline
a,b = map(int,input().split())
list = list(map(int,input().split()))

#합배열 만들기
[5,4,3,2,1]

sum_li = [0]
temp = 0

for i in list:
    
    temp += i 
    sum_li.append(temp)

for i in range(b):
    c,d = map(int,input().split())
    print(sum_li[d] - sum_li[c])