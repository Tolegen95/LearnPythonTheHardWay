def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACT %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLY %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "DIVIDE %d / %d" %(a, b)
    return a / b


print "Let's do some math with just functions!"
age = add (30, 5) # a blank space after 'add'
height = substract(78, 4)
weight = multiply   (90, 2) # a indent after 'multiply'
iq = divide(100, 2) # can have a enter after 'divide'

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it anyway
print "Here is a puzzle."

# age + (height - weight * iq / 2)
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what , "Can you do it by hand?"
