#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:51:53 2022

@author: Jiaqi Li, Jiehao Xing
"""
#This is a program designed to determine the students' expected total tuition and fees that will be collected

#Defining the function of amortized payment amount

def amortized_payment_amount_function(passed_principal,n):
    i=0.03
    amortized_payment_amount = float (((passed_principal)*i*(1+i)**n)/((1+i)**n-1))
    return amortized_payment_amount
print ("The author of this program is Jiaqi Li and Jiehao Xing.")

print ("Hello. I am going to calculate the expected total tuition and fees that will be collected for a student!")

#Start inputing information
print ("Do you want to input any student's information?")
keep_going=input("Input '1' to start; otherwise input '0'.")

#Start While Loop
while keep_going=="1":
    subtotal=0
    #Tuition
    print ("Is the student an in-district-student?")
    dist=input("Input '1' if the student is a in-district student otherwise please input '0'.")
    if dist=="1":
        subtotal=subtotal+8000
    elif dist=="0":
        subtotal=subtotal+9500

    #Sports fee
    print ("Do the student plays sports?")
    sports=input("Input 'y' if the student plays a sport otherwise please input 'n'.")
    if sports=="y":
        subtotal=subtotal+200
    elif sports=="n":
        subtotal=subtotal+0

    #Lunch fee
    print ("What type of lunch do the student eats?")
    lunch=input("Input '0' if the student brings lunch;'1' if the student eats standard lunch provided by school;'2' if the student eats premium lunch provided by school.")
    if lunch=="0":
        subtotal=subtotal+0
    elif lunch=="1":
        subtotal=subtotal+900
    elif lunch=="2":
        subtotal=subtotal+1170
    
    #Student status
    print ("What is the student's status in school?")
    student_status=input("If the student is in initial year enter 'i'; If the student is in the guaduation year enter 'g'; Other please enter 'o'.")
    if student_status=="i":
        subtotal=subtotal+200
    elif student_status=="g":
        subtotal=subtotal+100
    elif student_status=="o":
        subtotal=subtotal+0
    print ("The total fees and tuition collected are " + str(subtotal) + " dollars")    
    
    #Determine the way of payment and the amortized payment amount(round to two decimal points)
    print ("How will the student pay his or her bill?")
    payment_method=input("If the student wants to pay in whole right now, enter'w'; If the student wants to pay semi-annually, enter 's'; If the student wants to pay quaterly, enter 'q'; If the student pays monthly,enter 'm'." )
    if payment_method=="w":
        print ("The student is paying in whole.")
        print ("The amount you owe right now is "+str(subtotal)+" dollars.")
    elif payment_method=="s":
        print ("The student is paying semi-annually.")
        total_amount_owed=subtotal
        period=2
        amount_per_period=amortized_payment_amount_function(total_amount_owed,period)
        print ("The amount this student needs to pay per period is "+str (amount_per_period)+" dollars")
    elif payment_method=="q":
        print ("The student is paying quarterly.")
        total_amount_owed=subtotal
        period=4
        amount_per_period=amortized_payment_amount_function(total_amount_owed,period)
        print ("The amount this student needs to pay per period is "+str (amount_per_period)+" dollars")
    elif payment_method=="m":
        print ("The student is paying monthly.")
        total_amount_owed=subtotal
        period=12
        amount_per_period=amortized_payment_amount_function(total_amount_owed,period)
        print ("The amount this student needs to pay per period is "+str (amount_per_period)+" dollars")
    print ("Do you want to keep going?")
    keep_going=input("Enter '1' to continue; enter '2' to end the calculation.")
    
print ("Thank you for using this program. Bye!")

#End of the program
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    