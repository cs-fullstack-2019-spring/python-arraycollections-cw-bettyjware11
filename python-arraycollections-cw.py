def main():
    #Problem1()
    #Problem2()
    #Problem3()
    #Problem4()
    Problem5()
#Create a function with the variable below.
# After you create the variable do the instructions below that.
#arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
def Problem1():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2]) #a) Print the 3rd element of the numberList.
    len(arrayForProblem2)
    print(len(arrayForProblem2))  #b) Print the size of the array
    del(arrayForProblem2[-3])   #c) Delete the second element.
    print(arrayForProblem2)
    print(arrayForProblem2[2])   #d) Print the 3rd element.


#We will keep having this problem until EVERYONE gets it right without help
#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def Problem2():
    userInput = input("Enter q to quit")
    while (True):
        if userInput != "q":
            print("Try again")
        elif userInput == "q":
            break

#Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.
#Jonathan/John
#Michael/Mike
#William/Bill
#Robert/Rob

def Problem3():
    nickNames = {"Jonathan": "John", "Michael":"Mike", "William":"Bill", "Robert": "Rob"}
    print(nickNames)  #a) Print the collection
    print(nickNames["William"])  #b) Print William's nickname

#Create an array of 5 numbers. Using a loop, print the elements
# in the array reverse order. Do not use a function
def Problem4():
    newArray = [1,2,3,4,5]
    print(newArray)
    # for eachElement in range(0,len(newArray), 1):
    for eachElement in range(4,-1,-1):
        print(newArray[eachElement])

#Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def Problem5():
    hardCodedArray = [1,2,3,4,5]
    userInput = input("Enter number")
    for x in range(1,6):
        if hardCodedArray > userInput:
            print("higher")
        elif hardCodedArray < userInput:
            print("lower")
        elif hardCodedArray == userInput:
            print("equal")









































if __name__ == '__main__':
    main()