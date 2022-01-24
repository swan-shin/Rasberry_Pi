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

# make_list
# 기능: start 이상 end 미만의 정수 난수 n개를 갖는 리스트를 생성해서 반환

def make_list(start, end, n):
    """start 이상 end 미만의 정수 난수 n개를 갖는 리스트를 생성해서 반환"""
    random_list = [random.randrange(start, end,5) for _ in range(n)]
    return random_list

array1 = make_list(1, 20 , 5)
print(array1)

def calculate_sum(array):
    return sum(array)
sum_result = calculate_sum(array1)
print(sum_result)

print('원소의 개수: ', len(array1))
def calculate_mean(array):
    something = []
    for i in array:
        something.append(i)
    return sum(something)/len(something)
mean_array = calculate_mean(array1)
print(mean_array)

def calculate_var(array):
    var = 0
    for x in array:
        var += (x - calculate_mean(array))**2
    v = var/(len(array)-1)
    return v
result = calculate_var([1, 2, 3, 4, 5])
print(result)
print(calculate_mean([1, 2, 3]))

def calculate_stddev(array):
    var = calculate_var(array)
    return math.sqrt(var)
squr = calculate_stddev([1,2,3,4,5])
print(squr)

def find_min_and_max(array):
    """두 개 이상의 값을 return하는 함수는 tuple을 return 하는 함수"""
    min_array = array[0] #첫 번째 원소를 넣어야 다음 수를 비교 가능
    for x in array:
        if x < min_array:
            min_array = x
            # ... max도 동일



find_min_and_max([1,2,3,4,5])
print(find_min_and_max([1,2,3,4,5]))

def fin_min_and_max2(array):
    """전달받은 리스트를 오름차순 정렬하는 함수,
    정렬된 리스트의 첫번째 원소(최솟값), 마지막 원소(최댓값)"""
    arrange = []
    for x in array:
        arrange.append(x)

print(sorted([1, 3, 4, 5, 8, 11, 99, 843, 64 ,32], reverse=1))
