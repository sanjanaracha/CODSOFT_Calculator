# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.


def addition(a,b):

    c=a+b
    print("Addition of given numbers is" ,c)

def subtraction(a,b):

    c=a-b
    print("Subtraction of given numbers is" ,c)
    
def multiplication(a,b):

    c=a*b
    print("Multiplication of given numbers is" ,c)

def division(a,b):

    if b==0:
        print("b value should not be 0.Please enter a valid number.........")

    else:    
        c=a/b
        print("division of given numbers is" ,c)

if __name__=="__main__":

    a=int(input("enter value for a:"))
    b=int(input("enter value for b:"))

    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    
    n=int(input("enter your choice(1,2,3,4):"))
 
    if n==1:
        addition(a,b)
    elif n==2:
        subtraction(a,b)
    elif n==3:
        multiplication(a,b)
    elif n==4:
        division(a,b)
    else:
        print("Please,choose a valid choice!!!!!!!!!!!!!")