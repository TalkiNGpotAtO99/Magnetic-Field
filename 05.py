# BMI지수 (Body Mass Index:BMI 카우프지수)

height = int(input("키(cm)는? "))
weight = int(input("몸무게(kg)는? "))

bmi = weight / ((height / 100) ** 2)

if bmi <= 18.5 :
    print("BMI는 ", "%.2f" %bmi, "로 저체중입니다.", sep = '')
elif bmi <= 22.9 :
    print("BMI는 ", "%.2f" %bmi, "로 정상입니다.", sep = '')
elif bmi <= 24.9 :
    print("BMI는 ", "%.2f" %bmi, "로 과체중입니다.", sep = '')
else :
    print("BMI는 ", "%.2f" %bmi, "로 비만입니다.", sep = '')