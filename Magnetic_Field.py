# 자기장 생성기 찾기

import random
import math
import sys

x = random.randint(20, 80)
y = random.randint(20, 80)
r = 15

print("자기장 생성기를 찾으세요 (크기 15)")
i_x, i_y = map(int, input("좌표는? : ").split())

if (math.sqrt((x - i_x)**2 + (y - i_y)**2) > r) :
    print("(", i_x, ", ", i_y, ") 은 자기장 밖입니다. 자기장 생성기에 가까워졌습니다. (크기 14.5)", sep = '')
else :
    if (math.sqrt((x - i_x)**2 + (y - i_y)**2 < 1.5)) :
        print("(", i_x, ", ", i_y, ") 은 자기장 안입니다. 자기장 생성기를 찾았습니다. (거리 ",\
            math.sqrt((x - i_x)**2 + (y - i_y)**2),")", sep = '')
        print("자기장 생성기의 좌표는 (", x, ", ", y, ") 입니다. 오늘은 치킨이닭!", sep = '')
        sys.exit()
    else :
        print("(", i_x, ", ", i_y, ") 은 자기장 안입니다. 자기장 생성기에 가까워졌습니다. (크기 14.5)", sep = '')

temp_x, temp_y = i_x, i_y
r = r - 0.5

for i in range(1, 30) :
    i_x, i_y = map(int, input("좌표는? : ").split())
    
    if (math.sqrt((x - i_x)**2 + (y - i_y)**2) > r) :
        r = r - 0.5
        if (math.sqrt((temp_x - x)**2 + (temp_y - y)**2) >= math.sqrt((x - i_x)**2 + (y - i_y)**2)) :
            print("(", i_x, ", ", i_y, ") 은 자기장 밖입니다. 자기장 생성기에 가까워졌습니다. (크기 ", r, ")", sep = '')
        else :
            print("(", i_x, ", ", i_y, ") 은 자기장 밖입니다. 자기장 생성기에서 멀어졌습니다. (크기 ", r, ")", sep = '')
    else :
        r = r - 0.5
        if (math.sqrt((x - i_x)**2 + (y - i_y)**2 < 1.5)) :
            print("(", i_x, ", ", i_y, ") 은 자기장 안입니다. 자기장 생성기를 찾았습니다. (거리 ", \
                math.sqrt((x - i_x)**2 + (y - i_y)**2),")", sep = '')
            print("자기장 생성기의 좌표는 (", x, ", ", y, ") 입니다. 오늘은 치킨이닭!", sep = '')
            break
        elif (math.sqrt((temp_x - x)**2 + (temp_y - y)**2) >= math.sqrt((x - i_x)**2 + (y - i_y)**2)) :
            print("(", i_x, ", ", i_y, ") 은 자기장 안입니다. 자기장 생성기에 가까워졌습니다. (크기 ", r, ")", sep = '')
        else :
            print("(", i_x, ", ", i_y, ") 은 자기장 안입니다. 자기장 생성기에서 멀어졌습니다. (크기 ", r, ")", sep = '')
            
    temp_x, temp_y = i_x, i_y

sys.exit()
