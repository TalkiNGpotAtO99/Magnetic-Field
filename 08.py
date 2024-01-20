# 구구단 출력 프로그램이다. 사용자로부터 N, M (N, M 은 각각 2 에서 9 사이의 숫자이고 , N <= M 이다) 을 입력 받는다 . 
# 0 <= M N <= 3 이다 N 단부터 M 단까지를 화면에 출력한다 .
# 출력 시 화면의 공백을 잘 활용하여 표시한다 (출력 내용이 화면 중앙에 , 적당한 간격과 함께 ).

print("구구단을 외자! 구구단을 외자!")

while True :
    n = int(input("몇단부터? : "))
    m = int(input("몇단까지? : "))
    
    if m - n < 0 or m - n > 3 :
        print("유효하지 않은 범위! 다시 시도하세요.")
    elif m - n == 0 :
        print("%40d단" %n, sep = '')
        for i in range(1, 10) :
            print("%37d * %d = %d" %(n, i, n * i), sep = '')
        break
    elif m - n == 1 :
        print("%30d단%45d단" %(n, m), sep = '')
        for i in range(1, 10) :
            print("%27d * %d = %-39d%d * %d = %d" %(n, i, n * i, m, i, m * i), sep = '')
        break
    elif m - n == 2 :
        print("%20d단%35d단%38d단" %(n, n+1, m), sep = '')
        for i in range(1, 10) :
            print("%17d * %d = %-29d%d * %d = %-32d%d * %d = %d" %(n, i, n * i, n + 1, i, n + 1 * i, m, i, m * i), sep = '')
        break
    else :
        print("%15d단%28d단%32d단%36d단" %(n, n+1,n+2, m), sep = '')
        for i in range(1, 10) :
            print("%12d * %d = %-22d%d * %d = %-26d%d * %d = %-30d%d * %d = %d" \
                %(n, i, n * i, n + 1, i, n + 1 * i, n + 2, i, n + 2 * i, m, i, m * i), sep = '')
        break
