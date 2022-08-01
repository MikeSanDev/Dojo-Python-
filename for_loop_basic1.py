# Basic - Print all integers from 0 to 150.
for x in range(151):
    print(x)
# Multiples of Five - Print all the multiples of 5 from 5 to 1, 000
for i in range(5, 1001, 5):
    print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 101):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coding Dojo")
    else:
        print(str(x))
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
minimum = 0
maximum = 500000
total = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of {0} to {1} is {2}".format(
    minimum, maximum, total))

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 0
highNum = 21
mult = 2

for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)
