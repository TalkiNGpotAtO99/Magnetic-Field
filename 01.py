# 사용자로부터 숫자 정수 하나를 입력 받은 후 , 그 절대값을 화면에 출력하라.
# 사용자가 0 을 입력할 때까지 이 과정을 반복하라.

while True :
    n = int(input("숫자를 입력하세요 : "))
    
    if n > 0 :
        print(n)
    elif n < 0 :
        print(-n)
    else :
        break