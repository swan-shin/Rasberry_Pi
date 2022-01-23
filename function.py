# def functhin_name([param1, ...]):
#     ["""문서화 주석(documentation comment) - 함수에 대한 설명."""]
#     함수기능 작성
#     [return 반환 값] # [] 생략 가능

# 함수 정의(definition)
# def subtract(x, y):
#     """숫자 2개(x, y)를 전달받아서 x - y 를 반환하는 함수."""
#     return x - y

# 함수 호출(call, invoke)
# 함수를 호출할 때 parameter(변수)를 명시하지 않으면, argument는 순서대로 전달됨.
# result = subtract(10, 20)
# print(result)
#
# result = subtract(y=10, x=20)
# print(result)
#
# def add(x, y):
#     """숫자 2개(x, y)를 전달받아서 x + y를 반환."""
#     return x + y
# result = add(1, 2)
# print(result)
# result = add('1','2') # 문자열 1과 2를 붙여주는 역할, concatenate
# print(result)

# def plus_and_minus(x, y):
#     """두 개 이상의 숫자(x,y)를 전달받아서,
#     x + y, x - y를 리턴하는 함수"""
#     return x+y, x-y # 반환하는 값은 쉼표로만 구분 해주면 됨
# result = plus_and_minus(1,2)
# print(result) # 2개 이상의 값을 리턴하는 함수란 tuple을 리턴하는 함수
# tuple decomposition(분해): x, y = (value1, values2)
# plus, minus = plus_and_minus(1,2)
# print(plus)
# print(minus)

# 값을 반환하지 않는 함수 정의
# def repeat_message(message, n):
#     """문자열 message와 정수 n을 전달 받아서
#     message를 n번 반복해서 출력하는 함수."""
#     for _ in range(n):
#         print(message)
#
# result = repeat_message('hello', 3)
# print(result)

import random # 난수 사용 위해서
import math # 수학 함수들을 사용하기 위해서서
def make_list(start, end, n):
    """start 이상 end 미만의 정수 난수 n개를 갖는 리스트를 생성해서 반환"""
    return random_list = [random.randrange(start, end) for _ in range(n)]

result = make_list(3, 100, 20)
print(result)

# def calculate_sum():
