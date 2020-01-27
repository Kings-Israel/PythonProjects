def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 ==1:
        return 3 * number + 1
try:
    myNumber = int(input())
    while collatz(myNumber) != 1:
        print(collatz(myNumber))
        myNumber = int(input())
except ValueError:
    print("Enter a number")
    
print("finished")