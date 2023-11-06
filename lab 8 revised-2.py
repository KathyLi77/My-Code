#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:44:33 2022

@author: Jiaqi Li, Jiehao Xing
"""
import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

#Defining aggreagate payment function
def total_payment_amount_function(passed_principal,n):
    i=0.1
    numerater=float(passed_principal)*i*(1+i)**float(n)
    dinominator=(1+i)**float(n)-1
    total_payment_amount=(numerater/dinominator)*float(n)
    return total_payment_amount

#Create initial lists
student_list=[]
tuition_code_list=[]
tuition_list=[]
sports_code_list=[]
sports_fee=[]
lunch_code_list=[]
lunch_fee=[]
status_code_list=[]
status_fee=[]
total_fees_and_tuition_list=[]
how_to_pay_list=[]

total_amount_list=[]

print('The authors are Jiaqi Li and Jiehao Xing. Welcome to our program!')

#Opening the file containing students' info
student_file=open('student.txt','a')

#Adding items to the file using mode 'a'
print ("Do you want to input more student's information?")
keep_going=input("Input '1' to start; otherwise input '0'.")

while keep_going=='1': 
    #Asking the student's name
    student_name=input("What is the student's name?")
    
    #Tuition code 
    print ("Is the student an in-district-student?")
    dist=input("Input '1' if the student is a in-district student otherwise please input '0'.")
    
    #Sports code
    print ("Do the student plays sports?")
    sports=input("Input 'y' if the student plays a sport otherwise please input 'n'.")
    
    #Lunch code
    print ("What type of lunch do the student eats?")
    lunch=input("Input '0' if the student brings lunch;'1' if the student eats standard lunch provided by school;'2' if the student eats premium lunch provided by school.")
    
    #Status code
    print ("What is the student's status in school?")
    student_status=input("If the student is in initial year enter 'i'; If the student is in the guaduation year enter 'g'; Other please enter 'o'.") 
    
    #How to pay code
    print ("How will the student pay his or her bill?")
    payment_method=input("If the student wants to pay in whole right now, enter'w'; If the student wants to pay semi-annually, enter 's'; If the student wants to pay quaterly, enter 'q'; If the student pays monthly,enter 'm'." )
    
    #Adding contents of new record to the exsiting file
    x='\n' + student_name +' '+dist+' '+sports+' '+lunch+' '+student_status+' '+payment_method
    student_file.write(x)
    
    #Asking for more students' info
    print ("Do you want to keep going?")
    keep_going=input("Enter '1' to continue; enter '2' to end.")

#Closing the file after writing to it    
student_file.close()

#Opening the file and reading data from it
student_file=open('student.txt')
content=student_file.read()

#Building a new list to seperate each line
student_information_list=[]
student_information_list=content.split('\n')

#CLosing the file
student_file.close()

#Breaking up each entry in student_information_list and putting codes into corresponding lists
for i in range(len(student_information_list)):
    break_up=student_information_list[i].split()
    student_list.append(str(break_up[0]))
    tuition_code_list.append(str(break_up[1]))
    sports_code_list.append(str(break_up[2]))
    lunch_code_list.append(str(break_up[3]))
    status_code_list.append(str(break_up[4]))
    how_to_pay_list.append(str(break_up[5]))

#Transforming codes to values and store in new lists 
for i in range(len(tuition_code_list)):
    if tuition_code_list[i] =="1":
        tuition_list=tuition_list+[8000]
    elif tuition_code_list[i] =="0":
        tuition_list=tuition_list+[9500]
    
for i in range(len(sports_code_list)):
    if sports_code_list[i] =="n":
        sports_fee=sports_fee+[0]
    elif sports_code_list[i] =="y":
        sports_fee=sports_fee+[200]

for i in range(len(lunch_code_list)):
    if lunch_code_list[i]=="0":
        lunch_fee=lunch_fee+[0]
    elif lunch_code_list[i]=="1":
        lunch_fee=lunch_fee+[900]
    elif lunch_code_list[i]=="2":
        lunch_fee=lunch_fee+[1170]

for i in range(len(status_code_list)):
    if status_code_list[i]=="o":
        status_fee=status_fee+[0]
    elif status_code_list[i]=="i":
        status_fee=status_fee+[200]
    elif status_code_list[i]=="g":
        status_fee=status_fee+[100]

#Calculate the total fees and tuition to be collected from the student
for i in range(0, len(tuition_list)):
    total_fees_and_tuition_list.append(float(tuition_list[i])+float(sports_fee[i])+float(lunch_fee[i])+float(status_fee[i]))
    
#Calculate the aggregate amount a student needs to pay after determining his or her payment method                                     
for i in range(0, len(how_to_pay_list)):
    if how_to_pay_list[i]=="w":
        total_amount_list=total_amount_list+[total_fees_and_tuition_list[i]]
    elif how_to_pay_list[i]=="s":
        period=2
        total_amount_list=total_amount_list+[total_payment_amount_function(total_fees_and_tuition_list[i],period)]
    elif how_to_pay_list[i]=="q":
        period=4
        total_amount_list=total_amount_list+[total_payment_amount_function(total_fees_and_tuition_list[i],period)]
    elif how_to_pay_list[i]=="m":
        period=12
        total_amount_list=total_amount_list+[total_payment_amount_function(total_fees_and_tuition_list[i],period)]

            
    
    
    
#Opening a new file to write the result in it
pay_file=open('pay.txt','a')

logging.debug('Start of debugging.')

#for i in range(len(how_to_pay_list)):
        #logging.debug(student_list[i]+" "+str(round(float(total_amount_list[i]),2)))

#define a function to raise exception
def m(): 
    #for i in range(len(how_to_pay_list)):
        #logging.debug(student_list[i]+" "+str(round(float(total_amount_list[i]),2)))
    if how_to_pay_list[i]=="m":
        raise Exception(student_list[i]+" is paying in 12 payments. ")

#finding students who are paying monthly and write students who are not paying monthly into pay.txt file
for i in range(len(student_list)):             
    try:
        m()
        write_var=str(student_list[i])+" "+str(round(total_amount_list[i],2))
        logging.debug(str(write_var))
        if how_to_pay_list[0] == "m":
            pay_file.write(student_list[i]+" "+str(round(total_amount_list[i],2)))
            pay_file.write('\n')
        else:
            if i==0:
                 pay_file.write(student_list[i]+" "+str(round(total_amount_list[i],2)))
            else:
                pay_file.write('\n')
                pay_file.write(student_list[i]+" "+str(round(total_amount_list[i],2)))                                
                                           
    except Exception as err:
        print("An exception has raised: "+str(err))

logging.debug('End of debugging.')
    
#Closing the file
pay_file.close()

#End