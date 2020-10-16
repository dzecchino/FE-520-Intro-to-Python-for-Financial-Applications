#This is the print portion of the homework

stringFirst = 'This is the first string'
print(stringFirst)

stringStudent = "I'm a student"
print(stringStudent)

stringFeelings = 'How do you think of this course?'
x = """I am a little nervous about the course.
I am eager to learn python and hope I enjoy it.
I feel as though I am a bit behind the curve and need to catch up."""
print(x)

#This is the operator portion of the homework

a = 100
b = 9

c = a + b
print(c)
print(a/float(b))           # because a and b are both integers, the float type is used to print the decimals as well
print(a/b)                  # because a and b are both integers, the division of a by b will be an integer value as well
print(a%b)                  # % is the mod function which shows the remainder
print(a**b)                 # ** is the power operator

print(a != b)
print(a > b)

#This is the list practice portion of the homework

integer1 = 1
#print(type(integer1))                #used to check to see if this is an integer, which python does recognize it as an integer

integer2 = 2
#print(type(integer2))                #used to check to see if this is an integer, which python does recognize it as an integer

float1 = 10.1
#print(type(float1))                  #used to check to see if this is a float, which python does recognize it as a float

float2 = 10.2
#print(type(float2))                  #used to check to see if this is a float, which python does recognize it as a float

string1 = 'This is item number 5'    #used to check to see if this is a string, which python does recognize it as a string
#print(type(string1))

string2 = 'This is item number 6'    #used to check to see if this is a string, which python does recognize it as a string
#print(type(string1))

List_A = [int(integer1), int(integer2), float(float1), float(float2), string1, string2]
List_B = [1, 2, 3, 4, 5]

List_A.append(List_B)
#print(List_A)                        #used to check if List_B was added to List_A

List_A.insert(1, 'FE520')
#print(List_A)                        #used to check if the string was added to List_A

List_A.remove('FE520')
#print(List_A)                        #used to check if the string was added to List_A

print(List_A[6])
List_A.remove(List_A[6])
print(List_A)                        #used to check if the last item was deleted

List_C = List_A[2: ]                 # colon is used to show that we are including the 3rd element to the end of the list
print(List_C)

List_C.extend(List_C)
#print(List_C)                       #used to check if the list was doubled

List_C.reverse()
#print(List_C)                      #used to check if the sequence was reversed

#This is the practice dictionary portion of the homework

A = [1, 2, 3, 5, 10, 1, 4, 10, 11, 20, 50, 100]

count = {}
for item in A:
    if (item in count):
        count[item] += 1
    else:
        count[item] = 1
print(count)

#This is the loop condition practice portion of the homework

List = [1, 2, 4, 9, 17, 25, 63]
List2 = [63, 25, 17, 9, 4, 2, 1]



def sequence(lst, number):

    temp = 0
    for i in range(len(lst)):
        if(number < lst[i]):
            break
        temp+=1

    return lst[0: temp] + [number] + lst[temp :]

print(sequence(List, 13))

def InverseSequence(lst, number):
    temp = 0
    for i in range(len(lst)):
        if(number > lst[i]):
            break
        temp+=1
    return lst[0: temp] + [number] + lst[temp :]

print(InverseSequence(List2, 13))

def OrderingList(lst, number):
    if (len(lst) == 0):
        return lst + [number]
    if (len(lst) == 1):
        if(lst[0] > number):
            return [number] + lst[0]
        else:
            return [lst[0]] + [number]
    else:
        if(lst[0] > lst[(len(lst)-1)]):
            return InverseSequence(lst,number)
        else:
            return sequence(lst,number)

#Lst1 = []
#Lst2 = [1,3]
#Lst3 = [3,1]
#Lst4 = [2]
#print(OrderingList(Lst1,2))             # This whole section was used to check and see if all of the funcitons work properly
#print(OrderingList(Lst2,2))
#print(OrderingList(Lst3,2))
#print(OrderingList(Lst4,2))

#I pledge my honor that I have abided by the Stevens Honor System.
#Dominic Zecchino
