
""" some discription about the game ::) 
    
    This is a number game in it a player can become a "HUMAN CALCULATOR".
    
    there will be three difficulty levels .
    In normal mode user will get some ramdom addition and substraction problems . and the problems will going to become defficault with 
    every problem.

    In medium mode along with nomal mode's problem user will get some multiplicational problems also.

    In difficult mode along with normal and medium node there will also be restriction about the input time. 
    
    
    
    
    now some rules explaination 
    1-->when user is planing in normal mode then every right answer 1 point will be given.
    2-->when user is planing in medium mode then for every right answer 1 point will be given and if give us worng answer then -1 will be added
    3-->if user is playing in high mode then for right answer 1 point will be given and there are two conditions
            1.) if player gives right answer but time take in calculation is more then 5 second then -1 will be added.
            2.) if player gives wrong answer then -2 will be added.  """ 


#This time module i am using for calcution of some time period.
import time 

#This module will help me to genrate the random numbers and also random operators.
import random

#This is main function of my game 
def main():
   
    #The name of the game :)
    print("************Human Calculator************")
    
    #for tracking the points of the user...
    user_points={'points':0}
    
    #with the help of this variable i will try increase the complexity of the problems in the game.
    i = 1

    print(">>>>>>>>>>Welcome<<<<<<<<<<<<")
    #this will ask about in which mode user want's to play...
    user_play_mode=int(input("Please enter the mode in which you want to play, please Enter : \n1 for the normal mode :\n2 for the medium mode :\n3 for the difficult mode :\nYour input :"))
    while(user_play_mode<=0 or user_play_mode > 3):
        print("Wrong input !")
        user_play_mode=int(input("Please enter the mode in which you want to play, please Enter : \n1 for the normal mode :\n2 for the medium mode :\n3 for the difficult mode :\nYour input :"))



    #Game loop 
    while(True):

        #these two randomly genrated numbers 
        num1=random_num(i)
        num2=random_num(i)
        i += 4

        #the random genrated operator
        op=random_operator(user_play_mode)
        #print(op)
        right_answer = right_answer_calculation(num1,num2,op)
   

        #print(str(right_answer))

        start=int(time.time())#it give the time before the user get problem for solve...
        user_answer=user_input(num1,num2,op)
        end=int(time.time())#it give the time after the user entered the answer...

        if(user_answer==""):
            break

        time_taken=cal_time(start,end)
        #print(str(user_answer))

        compute_result(right_answer , user_answer , time_taken,user_play_mode,user_points)
        #print(str(time_taken))

    if(user_points['points']>=50):
        if(user_play_mode==1):
            print("You are a human calculator. now try yourself in medium mode .")
        elif(user_play_mode==2):
            print("You are a human calculator. now try yourself in difficult mode .")
        else:
            print("You are a human calculator. No one can beat you in this game.")


    if(user_points['points']<0):
        print("Not to worry ! you played well better luck next time.")
    
    print("Your score is : " +str(user_points['points']))
    print("Thanku for playing me ..")


#1-->this function will calculate the result 
def compute_result(right_answer , user_answer ,time_taken ,mode,user_points):

    if(mode==1):
        if(right_answer == int(user_answer) ):
            print("You calculated correctly.")
            user_points['points'] += 1
            return 
        print("You calculated wrong.")
    elif(mode==2):
        if(right_answer == int(user_answer) ):
            print("You calculated correctly.")
            user_points['points'] += 1
            return 
        print("You calculated wrong.")
        user_points['points'] -= 1

    else:
        if((right_answer == int(user_answer)) and (time_taken <= 5 )):
            print("You calculated correctly in between time limit.")
            user_points['points'] += 1
        elif((right_answer == int(user_answer)) and (time_taken > 5 )):
            print("You calculated correctly but you take too much time.")
            user_points['points'] -= 1 
        else:
            print("You calculated wrong.")
            user_points['points'] -= 2



#2-->this function will calculate the right answers for the comparision..
def right_answer_calculation(num1,num2,op):
    if(op=='+'):
        right_answer = (num1 + num2)
    elif(op=='-'):
        right_answer = (num1 - num2)
    else:
        right_answer=(num1 * num2)

    return right_answer

#3-->this function will take user calculated answers
def user_input(num1,num2,op):
    
    if(op=='+'):
        user_answer=input(str(num1)+op+str(num2)+": ")
    elif(op=='-'):
        user_answer=input(str(num1)+op+str(num2)+": ")
    else:
        user_answer=input(str(num1)+op+str(num2)+": ")
    return user_answer



#4-->this function will give us the random number 
def random_num(i):
        return random.randint((0+i),(25+i))


#5-->this function will give us random operators
def random_operator(mode):
    if(mode==1):
        listA = ['+','-'] 
        operator=random.randint(0,len(listA)-1)
        return listA[operator]
    listB = ['+','-','*'] 
    operator=random.randint(0,len(listB)-1)
    return listB[operator]


#6-->this function will calculate the time taken by the user for every given expresion and only for those users who wants to play at highest difficulty...
def cal_time(start,end):
    time_taken=end-start
    return time_taken

if __name__ == '__main__':
    main()