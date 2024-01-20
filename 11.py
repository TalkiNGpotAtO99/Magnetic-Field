# 사용자가 입력한 메뉴의 총액을 표시하라

menu = ['국수', '비빔밥', '햄버거', '국밥', '스파게티', '피자']
total = 0

while True :
    order = input("메뉴? (끝내려면 '종료' 입력) : ")
    
    if order == '국수' :
        total += 6000
    elif order == '햄버거' :
        total += 4500
    elif order == '비빔밥' :
        total += 8000
    elif order == '국밥' :
        total += 7500
    elif order == '스파게티' :
        total += 11000
    elif order == '피자' :
        total += 9900
    elif order == '종료' :
        break
    else :
        print("그런 메뉴는 없습니다.")

print("총액은 ", total, "원 입니다.", sep = '')