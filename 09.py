# 사용자가 입력한 일반 문장을 암호화하여 화면에 표시하라 .
# 사용한 암호화 방법 : 문자를 두개 뒤의 알파벳으로 교체

s = input("문장을 입력하세요 : ")
code = ""

for i in s :
    n = ord(i)
    #대문자의 경우
    if n >= 65 and n < 97:
        if n + 2 > 90 :
            n = n + 2 - 26
        else :
            n = n + 2
    #소문자의 경우
    if n >= 97 and n <= 122:
        if n + 2 > 122 :
            n = n + 2 - 26
        else :
            n = n + 2
    m = chr(n)
    code += m

print(code)