#1920
#시간 초과
import sys
input=sys.stdin.readline
#입력받기
N=int(input())
N_list=list(map(int,input().split(' ')))
M=int(input())
M_list=list(map(int,input().split(' ')))

#이진탐색 함수
def binary_search(start,end,target):
  while start<=end:
    mid=(start+end)//2
    if N_list[mid]==target:
      return 1
    elif N_list[mid]>target:
      end=mid-1
    else:
      start=mid+1
  return 0

#M찾기-이분탐색
N_list.sort()
for i in range(len(M_list)):
  print(binary_search(0,N-1,M_list[i]))
