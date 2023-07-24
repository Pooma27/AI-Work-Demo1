#Pooma calculator homework 

def div(num1:int, num2:int): #funtion for division, with local variables: num1 and num2
    ans = num1/num2 #ans is a variable that comes from the result of num1 and num2
    return(ans)

def multi(num1:int, num2:int): #funtion for multiplication
    ans = num1*num2
    return(ans)

def add(num1:int, num2:int): #function for addition
    ans = num1+num2
    return(ans)

def sub(num1:int, num2:int): #funcation for subtraction
    ans = num1-num2
    return(ans)

num1 = int(input("Enter a number: "))  #Input values for the variables
num2 = int(input("Enter a number: "))  #Input values for the variables

print(div(num1,num2)) #print the result of the input number that went into the fuction
print(multi(num1,num2))
print(sub(num1,num2))
print(add(num1,num2))


