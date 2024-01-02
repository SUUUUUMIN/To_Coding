import sys
string_in=sys.stdin.read().replace('\n','').replace(' ','')
#소문자리스트
word=[0 for _ in range(26)]

#'a'의 아스키코드 :97
for s in string_in:
    word[ord(s)-97]+=1

#최대값찾기
for i in range(26):
  if word[i]==max(word):
    print(chr(i+97),end='')