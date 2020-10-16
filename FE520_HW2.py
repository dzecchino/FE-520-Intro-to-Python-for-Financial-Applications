#I pledge my honor that I have abided by the Stevens Honor System.
#           Dominic Zecchino


from string import punctuation
from collections import Counter

# Step 1: Loop Condition Practice

def Ball_Drop(original_height, drop_num):
    original_height = float(original_height)          #used to convert original_height from type string to type int
#    print(type(original_height))
    i=1
    distTravelled = 0.0
    while i < drop_num+1:
        # print("Down: " , original_height)
        distTravelled += original_height
        original_height /= 4
        # print("Up: " , original_height)
        distTravelled += original_height

        i += 1
    print(distTravelled)
    return distTravelled

    #print(type(drop_num))      #used to make sure it is interpreted as an integer

# Step 2: String Practice

def Get_Token(Given_str_1):
#    Given_str_1 = Given_str_1.lower()
    #print(Given_str_1)                 #checks to see if all characters were set to lowercase
#    listOfWords = Given_str_1.split()
#    dictionaryOfWords = {}
    #print(listOfWords)         #used to see the ouput of splitting a string
#    for item in listOfWords:
#        if (item in dictionaryOfWords):
#            dictionaryOfWords[item] += 1
#        else:
#            dictionaryOfWords[item] = 1
#    print(dictionaryOfWords)

#    convert = Given_str_1.maketrans('', '' , string.punctuation)
#    print(Given_str_1.translate(convert))
    newString = Given_str_1.replace('\n', ' ')
    newString = newString.replace('\t', ' ')
    newString = newString.split(' ')
    def noPunct(sect):
        changed = sect.lower()
        for i in punctuation:
            changed = changed.replace(i, '')
        changed = changed.strip()
        return changed
    changed = [noPunct(sect)
    for sect in newString]
    changed = [sect for sect in changed if len(sect) != 0]
    output =  dict(Counter(changed))
    print(output)
    return output

# Step 3 : Fibonacci Sequence

def FiboSequence(i):
    if i == 0: return 0
    elif i == 1: return 1
    else: return FiboSequence(i-1)+FiboSequence(i-2)

def Step_2_Fibo(X, isIncrement):        #This entire function tests whether the given value (X) is equal to
                                        #a value in the Fibonacci sequence. If not, it tests to see when the
                                        #given value (X) is greater than the current number in the sequence
    X = int(X)                          #and less than the next number. When that is true, the function
    low = 0                             #finds the difference between the given value and the current value in
    high = 0                            #the sequence, and the difference between the next value and the givent
                                        #value in the sequence
    i = 0
#    print(type(X))              # X was originally interpreted as a string. This line told me that fact
#    print(type(high))                   # high was correctly interpreted as an int

    while (X > high):
        low = FiboSequence(i)
        high = FiboSequence(i+1)
        i+=1
        if (X == low or X == high):
            print('0')
            return 0
    if(X != low or X != high):
        print('Decrementing the number requeires ' , (X - low) , ' steps.')
        print('Incrementing the number requeires ' , (high - X) , ' steps.')
        if (X-low > high - X):
#            print('Here we are using high-X')
            return high-X
        elif(X-low<high-X):
#            print('Here we are using X-low')
            return X-low

        else:
            return high-X
    else:
        return 0

# Step 4: Identity Substring
'''
def splitterFunction(text):             #splits each character into a list
    return list(text)
def Combos(list):                     #uses the length of the list and the values of the list to create all combinations
#    return list(combinations(arr, l))  #incorrectly written
    if not(1< len(list)):
        yield list
        yield []
    else:

        for i in Combos(list[1: ]):
            yield [list[0]] + i
            yield i
'''            #The above section is no lomger needed
def identi_Substring(S):
    'SList = splitterFunction(S)'
#    print(SList)                   # used to make sure that SList was split so
                                    #that every character is its own element in a list
#    l = len(SList)
    #print("list: ",SList)
    #print("l",l)                       #double checked the length of my new list
    #print("List: ", ( Combos(SList, 2)))       #incorrectly written

    ''' counter = 0
    Possibilities = [y for y in Combos(SList)]
    for i in Possibilities:
        counter += 1
    counter = counter - 1
    print(counter)

    Possibilities.sort()                #evaluate all possible combinations
    print (Possibilities)               #printing all possible combinations
    '''     #This code doesnt work because it doesnt account for duplicates
    length = len(S)
    output = [S[i:j] for i in range (length)
    for j in range (i+1, length+1)]
    newList = []
    #about to append the possibilities to a new arrau
    for i in output:
        x = set(list(i))
        if len(x)==1:
            newList.append(i)
    print(len(newList))
    return len(newList)

if __name__ == "__main__":
    print('This is the ball drop portion of the assignment: ')
    Ball_Drop(input("Please enter the height from which the ball was dropped in meters: "), 5)

    print('=========================================')
    print('This is the token part of the assignment: ')

#    Get_Token('''This course is designed for those students have no experience or
    #limited experience on Python. This course will cover the basis
    #syntax rules, modules, importing packages (Numpy, pandas), data
    #visualization, and Intro for machine learning on Python. You will
    #need to implement what you learn from this course to do a finance
    #related project. This course aims to get you familiar with Python
    #language, and can finish a simple project with Python.''')
    Get_Token(input('Input a string: '))

    print('=========================================')
    print('This is the Fibonacci part of the assignment: ')

    Step_2_Fibo(input("Please enter the desired number: "), True)

    print('=========================================')
    print('This is the Substring part of the assignment: ')

    identi_Substring(input('Input a string: ' ))




######Below is all code I used to test the functions before implementing the main function


#Ball_Drop(input("Please enter the height from which the ball was dropped in meters: "), 5)


#Get_Token('''This course is designed for those students have no experience or
#limited experience on Python. This course will cover the basis
#syntax rules, modules, importing packages (Numpy, pandas), data
#visualization, and Intro for machine learning on Python. You will
#need to implement what you learn from this course to do a finance
#related project. This course aims to get you familiar with Python
#language, and can finish a simple project with Python.''')

#Step_2_Fibo(input("Please enter the desired number: "), True)

#identi_Substring(input('Input a string: ' ))
