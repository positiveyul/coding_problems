import sys

from random import *
import random

#for y in range(20): 
#    print(randint(111,999))

def get_digit(number):
    """
    숫자로 변환하는 지 확인
    True로 나오면 통과
    
    """
    result = number.isdigit()

    return result

def check_diff_number(number):
    """
    입력 숫자 같은 숫자가 있는지 확인
    True로 나오면 통과
    
    :PARAMS str number: 사용자가 입력한 숫자
    :PARAMS result_final: 숫자가 같은 것이 있으면 False
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

def  is_between_100_and_999(x):
    if 100<int(x)<999:
        return True
    else: 
        return False

# 통합 return

def total_input_check(number):
    if get_digit(number)==False or check_diff_number(number)== False or is_between_100_and_999(number)==False or check_zero(number)==False:
        return False
    else:    
        return True 

def check_zero(number):
    number_list=list(number)
    if "0" in number_list:
        return False
    else:
        return True

# ===== answer 추출 =====

def make_answer(numlist):

    """
    sample은 확률 - 조합 처럼 값을 3개 뽑는다.
    
    """
    question = random.sample(numlist,3)
    answer = str(100*int(question[0])+10*int(question[1])+int(question[2]))
    return answer
    
    # print(answer)    #맞춰야 할 답

# ===== answer 확인 결과 =====

def is_same(answer, number):
    """
    answer, number가 같은지 출력

    """


    answer_list = list(answer)
    number_list = list(number)
    check_list = {"ball" : 0, "strike" : 0}
    
    for i in range(len(number_list)):
        if number_list[i] in answer_list:
            if number_list[i] == answer_list[i]:
                check_list["strike"] += 1
            else:
                check_list["ball"] += 1
    

    return check_list

            




while True:
    num_list= [1,2,3,4,5,6,7,8,9]
    answer = make_answer(num_list)
    # print(answer)

    

    # while True:
    #     if guess_answer == "0":
    #         break
    #     elif total_input_check(guess_answer) == False:
    #         guess_answer= input("숫자를 다시 입력하세요!!!!!! \n(000~999) 정수 :   ")
        
    #     else:
    #         break
    # print(guess_answer)
    
    while True:
        guess_answer = input("숫자를 맞춰보세요! 100~999사이 숫자를 입력하세요!\n")
        if guess_answer == "0":
           break
        elif total_input_check(guess_answer) == False:
            print("숫자를 다시 입력하세요!!!!!! \n") 
        elif answer == guess_answer:
            print(" 정답은 {} 였습니다.".format(answer) )
            break
        else:
            check_dict= is_same(answer,guess_answer)
            if check_dict["ball"]==0 and check_dict["strike"]==0:
                print("OUT!!!!!")
            else:
                print(" {} Ball {} Strike".format(check_dict["ball"],check_dict["strike"]))


    if input("더 하시려면 아무거나 입력, 그만 하실거면 0을 눌러주세요!\n") == "0":
        break
