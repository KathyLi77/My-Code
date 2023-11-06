#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:01:13 2022

@author: Jiaqi Li, Jiehao Xing
"""

#This program is designed to help the manager looking up students' information

#Setting up dictionary
students_information={'Bob Smith': {'tuition':8000,'sports':200,'lunch':900},
                      'Sue Jones':{'tuition':9500,'sports':200},
                      'Mike Johnson':{'tuition':8000,'lunch':1170},
                      'Mary Thomas':{'tuition':9500, 'status_fee':200}}

#Defining functions
def aggregate_cost (student, type_of_fee):
    total_fee=0
    for k,v in student.items():
        total_fee=total_fee+v.get(type_of_fee,0)
    return total_fee

#Provide specific student and the specific cost of the student
print("We currently have infromation for Bob Smith, Sue Jones, Mike Johnson, Mary Thomas.")
specific_student=input("Who are you looking for? ")
print("The types of costs are tuition, lunch, sports, and status_fee.")
specific_fee=input("What type of cost are you looking for? ")


for k,v in students_information.items():
    if k==specific_student:
        result=v.get(specific_fee, "None")
        if result=="None":
            if specific_fee=="sports":
                print(specific_student + " does not play sports.")
            if specific_fee=="lunch":
                print(specific_student + " bring his/her own lunch to school.")
            if specific_fee=="status_fee":
                print(specific_student + " isn't a new student or graduating.")
        if result==v.get(specific_fee):
            print(str(specific_student) + " owes " + str(result) + " for " + str(specific_fee)+".")
print("")       
     
#Provide aggregate information
print("The types of costs are tuition, lunch, sports, and status_fee.")
look_up_fee=input("What type of cost(fee or tuition) are you looking for? ")
outcome=aggregate_cost(students_information, look_up_fee)
print(look_up_fee+"-------->"+str(outcome))



        

