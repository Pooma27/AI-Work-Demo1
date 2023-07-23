
#loop example from previous class
'''
inputRound = int(input("Please enter a number: "))
sum = 0

for x in range(inputRound):
    inputNumber = (input("x" + str(x) + ":"))
'''

#function class
'''
def mewsit(sittime: int=10, name: str="pluem"):
    print(str(sittime) + name)
    return 100
'''
'''
def mewsit(sittime: int=100, name: str="pluem"):
    if sittime == 100:
        print(1)
        return 100

mewsit()
'''
'''
def mew(situp: int = 5):
    if situp >= 10:
        print("Mew is tired.")
    else:
        print("Mew hasn't finish his situp set.")
        
mew()
'''
'''
x = int(input("What is the situp number: "))
def mewSitupcheck(sittime: int=1):

    if sittime < 20:
        print("Mew is still doing situp")
    else:
        print("Mew is tired")
mewSitupcheck(x)
'''