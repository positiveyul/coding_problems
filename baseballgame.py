import sys

from random import *
import random

#for y in range(20): 
#    print(randint(111,999))

def get_digit(number):

    result = number.isdigit()

    return result

def check_diff_number(number):
    """
    입력 숫자 같은 숫자가 있는지 확인
    :PARAMS str number: 사용자가 입력한 숫자
    :PARAMS result_final:
    :rtype Boolean
    
    """


    number_list = list(number)
    result_list = []
    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if i< j :
                if number_list[i]==number_list[j]:
                    result = False
                    result_list.append(result)
                else:
                    result = True 
                    result_list.append(result)
    if False in result_list:
        result_final = False
    else:
        result_final = True

    return result_final      




    # set으로 둬서 len 값이 3인지 확인해도 됨
    # number_set = set(number)
    # if len(number_set) == 3:
    #     return True
    # else:
    #     return False

# print(check_diff_number(input("디프쳌 test: ")))

#     return result






# def is_digit():


# def  is_between_100_and_999(x):
#     if 100<x<999:
#         return True
#     else: 
#         return False

# def is_duplicated_number(x):
#     if answer.split():


#     return True



numlist=[1,2,3,4,5,6,7,8,9]
# for i in range(1,10):
#     numlist.append(i)

# print(type(numlist))
question = random.sample(numlist,3)
# sample은 확률 - 조합 처럼 값을 3개 뽑는다.
#print(question)

answer = str(100*int(question[0])+10*int(question[1])+int(question[2]))
print(answer)    #맞춰야 할 답

# answer_list= list(answer)
# print(answer_list) 

# quess_answer = input("숫자를 맞춰보세요. ")
# list_

# a= "2"
# print(a.isdigit()) #문자열이 숫자로만 이뤄져있는지 확인



