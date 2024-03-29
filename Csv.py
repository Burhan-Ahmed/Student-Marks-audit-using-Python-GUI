import numpy as np
import pandas as pd
import csv


myweightage=[]
mysubj=[]
mynumber=[] #number of quiz,assignment etc
quizScore=[]
assignScore=[]
types = int(input("Enter Types of Assessments Done : "))
for x in range(types):
    name = input("Enter Assessment Name : ")
    quantity = int(input(f"Enter Number of {name} : "))
    weightage = int(input(f"Enter Weightage for {name} : "))
    myweightage.append(weightage)
    mynumber.append(quantity)
    mysubj.append(name)

for x in range(mynumber[0]):
    num = int(input(f"Enter Total Marks for Quiz {x} : "))
    quizScore.append(num)

for x in range(mynumber[1]):
    num = int(input(f"Enter Total Marks for Assignment {x} : "))
    assignScore.append(num)

div=len(quizScore)
div2=len(assignScore)
#--------------------------------------------------------------------------------------------------------------
file4=input("Enter Class Name : ") #CE-115L BEBME 1A.csv
while (True):
    cc=int(input(f"4. {file4}\n 5. Exit\n"))
#---------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------4-------------------------------------------------------
    if(cc==4):
        df = pd.read_csv(file4+".csv", delimiter=',')
        dd=pd.DataFrame(df)
        dd=np.array(dd)

        quiz1=dd[:,2:mynumber[0]+1]
        assign1=dd[:,mynumber[0]+1:mynumber[1]+1]
        mid1=dd[:,mynumber[1]+1:mynumber[2]+1]
        final1=dd[:,mynumber[2]+1:mynumber[3]+1]
        project1=dd[:,mynumber[3]+1:mynumber[4]+1]
       
        quiz=(quiz1.sum(axis=1)/div)*myweightage[0]
        assignment=(assign1.sum(axis=1)/div2)*myweightage[1]  
        mid=(mid1.sum(axis=1)/55)*myweightage[2]  
        final=(final1.sum(axis=1)/50)*myweightage[3]  
        project=(project1.sum(axis=1)/20)*myweightage[4]  
        sum_result=quiz+assignment+mid+final+project # Grand Total
        #stacking the columns
        result=np.hstack((quiz.reshape(-1,1),assignment.reshape(-1,1),mid.reshape(-1,1),final.reshape(-1,1),project.reshape(-1,1)))
#function to calculate grade
        def myfunc(a, b,c,d):
            if a > b:
                return "A"  #Return A if marks greater than 70
            if (a > c and 70>c):
                return "B"  #Return B if marks greater than 60 and less than 70
            if (a > d and 60>d):
                return "C"  #Return C if marks greater than 50 and less then 60
            else:
                return "D"  #Return D if marks greater than 40
        fun = np.vectorize(myfunc) #function will recursvicly continue to loop till complete dataset is not checked
        #this is Faster then for loop
        grade=fun(sum_result, 70,60,50)
        result=np.hstack(((dd[:,:2]),result))
        result=np.hstack((result,sum_result.reshape(-1,1)))
#        tot=np.full((30,1),100) #Additional colum of 100 as total marks
#        result=np.hstack((result,tot)) #stacking with result file
        result=np.hstack((result,grade.reshape(-1,1))) #stacking grade with result file
        Grand_tot=result[:,7:8]
        result=np.hstack(((dd[:,:]),result))
        while(True):
            x=int(input("1. Display class result\n 2. Generate class result in a new .csv file\n 3. Particular Student result\n 4. Highest and Lowest Marks in Class\n 5. Back\n 6. Exit\n"))
            if(x==1):
                display=pd.DataFrame(result, columns=["Roll Num","Name",f'{mysubj[0]}',f'{mysubj[1]}',f'{mysubj[2]}',f'{mysubj[3]}',f'{mysubj[4]}',"Grand Total", "Grade"])
                print(display)
               
            elif(x==2):
                display=pd.DataFrame(result, columns=["Roll Num","Name",f'{mysubj[0]}',f'{mysubj[1]}',f'{mysubj[2]}',f'{mysubj[3]}',f'{mysubj[4]}',"Grand Total", "Grade"])
                display.to_csv('file.csv', index=False,sep=',')              #Close Csv file
                print("File Successfully Generated into .csv file")
#                rows = result.tolist()
#                with open('result.csv', 'w', newline='') as file:  # Open Csv file
#                    writer = csv.writer(file, delimiter='\t')
#                    for row in rows:
#                        writer.writerow(row)
                     #write complete result file into "result.csv" file
#                    file.close()                        #Close Csv file
#                print("File Successfully Generated into .csv file")
               
            elif(x==3):
                #function that return data if a==b, otherwise return Not Found
                def myff(num):
                    for i in result:
                        if i[0] == num: #i[0] indicates the roll number colum to be compared
                            return i
                op=int(input("Enter the Roll Number of Student : ")) #get roll number of student
                single=myff(op).reshape(1,-1)
                print("\n")
                display=pd.DataFrame(single,columns=["Roll Num","Name","QUIZ","Assignment","Midterm","Final","CEA","Grand Total","Total", "Grade"])
                print(display)
                print("\n")
            elif(x==4):
                #fstring is used because it is faster
                print(f"Lowest Marks : {Grand_tot.min()}")
                print(f"Higest Marks : {Grand_tot.max()}")
            elif(x==5): #this will act as a back function
                break; #break current loop and return into outer loop
            elif(x==6):
                print("--Thank you--")
                break;
            else:
                print("INVALID INPUT\n")
#---------------------------------------------------------------------------------------------------------------------
    elif(cc==5):
        print("--Thank you for using my Program--")
        break;
    else:
        print("Invalid Input")