def compare(number):
    print number
    i = 0
    numbers = []
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
    print "The numbers: "

    for num in numbers:
        print num
        
a = raw_input('> ')
compare(a)
    