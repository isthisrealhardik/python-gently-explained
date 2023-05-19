# Is Given A Number or Odd or Even

# function checks if a number is odd or even
def isOddOrEven(num):
    if (num % 2 == 0):
        return 'The Given Number is Even'
    else: 
        return 'The Given Number is Odd'
    
# function that asks for an user input
def asksNum():
    num = int(input("Input your number: "))
    return isOddOrEven(num)

print(asksNum())