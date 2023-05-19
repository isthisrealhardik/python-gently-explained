# a function with an int parameter 'upto',
# if a number is divisble by both 3 & 5, print 'fizzBuzz'
# if a number is divisble by only 3, print 'fizz'
# if a number is divisble by only 5, print 'Buzz'
# if a number is not divisble by both, print the number

# plan: 
# create a function named 'fizzBuzz'
# with a paramter named 'upTo', that takes an int
# create an array of a string till the 'upTo' index number
# check if the current index matches with any of the above specified condition, and add that to an array
# after the loop ends, return the array

def fizzBuzz(upTo = 1):
    array = []
    for i in range(1, upTo + 1):
        if (i % 3 == 0 and i % 5 == 0):
            array.append('FizzBuzz')
        elif (i % 3 == 0):
            array.append('Fizz')
        elif (i % 5 == 0): 
            array.append('Buzz')
        else:
            array.append(i)
    return array

print(fizzBuzz(35))