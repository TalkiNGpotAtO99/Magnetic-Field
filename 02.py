# 사용자로부터 문자열을 입력 받은 후 , 리스트에 없는 동이면 리스트 에 추가하고,
# 리스트에 있는 동이면 해당 동이 몇 번째 데이터인지 화면에 표시하라 .
# 계속 반복되고 , 종료 라고 입력하면 프로그램이 종료된다.

location = ['흑석동', '사당동', '상도동', '노량진동', '규동']

while True :
    local = input("동을 입력하세요 : ")

    if local in location :
        print(location.index(local)+1, "번째 동입니다.", sep = '')
    elif local == '종료':
        print("프로그램이 종료됩니다.")
        break
    else :
        print("새로운 동명입니다. ", location.index(location[-1]) + 2, "번째 동으로 등록합니다.", sep = '')
        location.append(local)