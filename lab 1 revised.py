#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:23:00 2022

@author: Jiaqi Li, Jiehao Xing
"""
#This is a program designed to process the incoming students' information to determine the expected total tuition and fees.

print ("Hello. I am going to calculate the total tuition and fees for Krannert!")

#Assining values to the variables
subtotal = 0
total_tuition = 0
total_fees = 0
total_students = 0
sports_students = 0
bring_lunch_students = 0
standard_lunch_students = 0
premium_lunch_students = 0
graduating_students = 0

#Start inputing information
print ("Do you want to input any student's information?")
keep_going=input("Input '1' to start; otherwise input '0'.")

#Start While Loop
while keep_going=="1":
    #Tuition
    print ("Is the student an in-district-student?")
    dist=input("Input '1' if the student is a in-district student otherwise please input '0'.")
    if dist=="1":
        subtotal=subtotal+8000
        total_tuition=total_tuition+8000
        total_students=total_students+1
    elif dist=="0":
        subtotal=subtotal+9500
        total_tuition=total_tuition+9500
        total_students=total_students+1
    

    #Sports fee
    print ("Do the student plays sports?")
    sports=input("Input 'y' if the student plays a sport otherwise please input 'n'.")
    if sports=="y":
        subtotal=subtotal+200
        total_fees=total_fees+200
        sports_students=sports_students+1
    elif sports=="n":
        subtotal=subtotal+0
        total_fees=total_fees+0
   

    #Lunch fee
    print ("What type of lunch do the student eats?")
    lunch=input("Input '0' if the student brings lunch;'1' if the student eats standard lunch provided by school;'2' if the student eats premium lunch provided by school")
    if lunch=="0":
        subtotal=subtotal+0
        total_fees=total_fees+0
        bring_lunch_students=bring_lunch_students+1
    elif lunch=="1":
        subtotal=subtotal+900
        total_fees=total_fees+900
        standard_lunch_students=standard_lunch_students+1
    elif lunch=="2":
        subtotal=subtotal+1170
        total_fees=total_fees+1170
        premium_lunch_students=premium_lunch_students+1
    

    #Student status
    print ("What is the student's status in school?")
    student_status=input("If the student is in initial year enter 'i'; If the student is in the guaduation year enter 'g'; Other please enter 'o'.")
    if student_status=="i":
        subtotal=subtotal+200
        total_fees=total_fees+200
    elif student_status=="g":
        subtotal=subtotal+100
        total_fees=total_fees+100
        graduating_students=graduating_students+1
    elif student_status=="o":
        subtotal=subtotal+0
        total_fees=total_fees+0
    
    print ("Do you want to keep going?")
    keep_going=input("Enter '1' to continue; enter '2' to end the calculation.")
    

#Display the final result
print ("The total fees and tuition collected are " + str(subtotal) + " dollars")
print ("The total tuition collected is " + str(total_tuition) + " dollars")
print ("The total fees collected are " + str(total_fees) + " dollars")
print ("The total number of students is/are " + str(total_students))
print ("The total number of sports students is/are " + str(sports_students))
print ("The total number of bring lunch students is/are " + str(bring_lunch_students))
print ("The total number of standard lunch students is/are " + str(standard_lunch_students))
print ("The total number of premium lunch students is/are " + str(premium_lunch_students))
print ("The number of graduating students is/are " + str(graduating_students))

print ("Thank you for using this program. Bye!")

#End of the program




