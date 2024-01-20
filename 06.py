# 사용자로부터 원금과 금리를 입력 받아 , 향후 20 년간 복리로 계산했을 때의 금액
# 원금 + 이자 을 화면에 출력하는 프로그램을 작성하라

principal = int(input("원금을 입력하세요(원). "))
rate = int(input("금리를 입력하세요(%). "))

print("원금 ", principal, ", 금리 ", rate, "% 입니다.", sep = '')

print("   기간     합계")
for i in range(1, 21) :
    print("%5d년%11.1f" %(i, principal * ((1 + rate / 100)** i)), sep = '')