# 사용자로부터 N 개의 숫자를 입력 받은 후 , 오름차순으로 정렬하여 화면에 출력하라.
# 0 을 입력하면 입력을 종료한다 .

nlist = []
print("데이터를 입력하세요.(입력을 마치려면 0을 입력하세요.)")

while True :
    n = int(input())
    
    if(n == 0) :
        break
    else :
        nlist.append(n)

nlist.sort()        
print("결과 : ", nlist, " (", len(nlist), "개)", sep ='')