def my_add():
    myString = input("enter Numbers to add: ")
    a = myString.split('+')
    result=0  
    for i in range(0,len(a)):
        while a[i].isnumeric()==False:
            print("Wrong input\n") 
            myString = input("enter Numbers to add again : ")
            a = myString.split('+')
            break
    for j in range(0,len(a)):
        result=result+int(a[j])
    print(result)

def my_mul():
    myString = input("enter Numbers to multiply: ")
    a = myString.split('*')
    result=int(a[0])  
    for i in range(0,len(a)):
        while a[i].isnumeric()==False:
            print("Wrong input\n") 
            myString = input("enter Numbers to multiply again : ")
            a = myString.split('*')
            result=int(a[0])
            break
    for j in range(1,len(a)):
        result=result*int(a[j])
    print(result)
def my_sub():
    myString = input("enter Numbers to subscribe: ")
    a = myString.split('-')
    result=int(a[0])  
    for i in range(0,len(a)):
        while a[i].isnumeric()==False:
            print("Wrong input\n") 
            myString = input("enter Numbers to subscribe again : ")
            a = myString.split('-')
            result=int(a[0])
            break
    for j in range(1,len(a)):
        result=result-int(a[j])
    print(result)
     
def my_dev():
    myString = input("enter Numbers to divide: ")
    a = myString.split('/')
    result=int(a[0])
    for i in range(0,len(a)):
        while a[i].isnumeric()==False:
            print("Wrong input\n") 
            myString = input("enter Numbers to divide again : ")
            a = myString.split('/')
            result=int(a[0])
            break
    for j in range(1,len(a)):
        
        result=result/int(a[j])
    print(result) 
print("\nChoose mathematical operation\n")
print(" 1 Add\n 2 subscribe\n 3 multiply\n 4 divide ") 
   
user_choose=int(input())
if user_choose==1:
    my_add()
elif user_choose==2:
    my_sub()
elif user_choose==3:
    my_mul()
else:
    my_dev()