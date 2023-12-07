#숫자 입력
n=int(input())

#배열&중복제거
arr=set()
for i in range(n):
  arr.add(input()) #set=add

#다시 리스트 만들기
arr=list(arr)

#정렬
arr.sort()
arr.sort(key=len)

#출력
for item in arr:
  print(item)