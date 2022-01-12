import random # random 모듈 사용

# random 모듈이 가지고 있는 함수들을 사용하는 방법
# start <= r < stop 범위의 정수 난수를 생성.
random.randrange(start=1, stop=4)

# random. randrange(stop) : 0 <= r < stop 범위의 정수 난수 생성
random.randrange(4)

# random.random(): 0 <= r < 1 범위의 실수 난수 생성
random.random()

print('=== 가위/바위/보 ===')
print("""[1] 가위
[2] 바위
[3] 보""")

user = int(input('선택>>> '))
computer = random.randrange(1, 4)
'''
if computer == user:
    print('비겼습니다.')
elif computer == 1 and user == 2:
    print('당신이 이겼습니다.')
'''
'''
if user == 1:
    if computer == 1:
        print('비김')
    elif computer == 2:
        print('computer win')
    else: print ('user win')
elif user == 2:
    if computer == 1:
        print('비김')
    elif computer == 2:
        print('computer win')
    else: print ('user win')
else:
    if computer == 1:
        print('비김')
    elif computer == 2:
        print('computer win')
    else: print ('user win')
'''
'''
if user == computer: # 비김
    pass
elif user == 1:
    if computer == 2:
        print('computer win')
    elif computer == 3:
        print('user win')
elif user == 2:
    if computer == 1:
        print('user win')
    elif computer == 3:
        print('computer win')
elif user == 3:
    if computer == 1:
        print('computer win')
    elif computer == 2:
        print('user win')'''

if user == computer:
    pass
elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print(1)
else:
    pass

#for 반복문
'''
for 변수 in terable-type:
    반복해서 실행할 블록(문장들)
'''

#   iterable-type: 반복 가능한 데이터 타입,
    #   range, list, tuple, dict, set, str, ...

# range(start, stop, step)