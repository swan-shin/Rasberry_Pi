    # 정수를 입력받아 변수에 저장

# 정수 3개를 입력받고 변수에 저장
korean = int(input('국어 점수 입력>>> '))
english = int(input('영어 점수 입력>>> '))
math = int(input('수학 점수 입력>>> '))

# 평균 계산
average = (korean + english + math) / 3
print('평균:', average)

# 학점 출력
# 90 이상이면 'A'
# 80 이상이면 'B'
# 70 이상이면 'C' 출력
# 70 미만이면 'F' 출력

if average >= 90:
    print('학점 A')
elif average >= 80:
    print('학점 B')
else :
    print('학점 F')
