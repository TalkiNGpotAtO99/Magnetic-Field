# 컴퓨터와 가위바위보를 하는 게임이다.

import random

print("-------------가위바위보 게임 시작-------------")
print("성적 : 0승 0패")
win = 0
lose = 0
round = 1
game = ["가위", "바위", "보"]

while(lose != 3 and win != 3) :
    print("(라운드 ", round, ")", sep = '')
    
    computer = random.choice(game)
    print("컴퓨터가 결정했습니다.")
    
    user = input("무엇을 내시겠습니까? (가위, 바위, 보) : ")
    
    if computer == user :
        print("컴퓨터는 ", computer, ", 당신은 ", user, ", 비겼습니다.", sep = '')
        round += 1
    elif computer == "가위" :
        if user == "바위" :
            print("컴퓨터는 ", computer, ", 당신은 ", user, ", 당신이 이겼습니다.", sep = '')
            win += 1
            round += 1
        elif user == "보" :
            print("컴퓨터는 ", computer, ", 당신은 ", user, ", 당신은 졌습니다.", sep = '')
            lose += 1
            round += 1
    elif computer == "바위" :
        if user == "보" :
            print("컴퓨터는 ", computer, ", 당신은 ", user, ", 당신은 이겼습니다.", sep = '')
            win += 1
            round += 1
        elif user == "가위" :
            print("컴퓨터는 ", computer, ", 당신은 ", user, ", 당신은 졌습니다.", sep = '')
            lose += 1
            round += 1
    else :
        if user == "가위" :
            print("컴퓨터는 ", computer, ", 당신은 ", user, ", 당신은 이겼습니다.", sep = '')
            win += 1
            round += 1
        elif user == "바위" :
            print("컴퓨터는 ", computer, ", 당신은 ", user, ", 당신은 졌습니다.", sep = '')
            lose += 1
            round += 1
    
    print("성적 : ", win, "승 ", lose, "패", sep = '')
    
print("-------------가위바위보 게임 종료--------------")