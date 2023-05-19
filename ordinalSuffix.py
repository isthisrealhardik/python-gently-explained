# a function which returns the ordinal suffix such as 42 to 42nd or 30 to 30th

def ordinalSuffix(num):
    strNum = str(num)
    if (strNum.endswith('1')):
        return f"{strNum}st"
    elif (strNum.endswith('2')):
        return f"{strNum}nd"
    elif (strNum.endswith('3')):
        return f"{strNum}rd"
    else:
        return f"{strNum}th"

num = int(input('Your number?: '))
print(ordinalSuffix(num))