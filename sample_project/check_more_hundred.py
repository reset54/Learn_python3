string = input()
numbers = string.split(" ")
one = int(numbers[0])
two = int(numbers[1])

max = one

if one > 100 and two > 100:
    if two > one:
        max = two
        print(max)
    else:
        print(max)
else:
    print(two + 112)
    