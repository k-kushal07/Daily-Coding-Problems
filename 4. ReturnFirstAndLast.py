def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons):
    return cons(lambda a, b: a)

def cdr(cons):
    return cons(lambda a, b: b)


input1 = int(input('Enter first number: '))
input2 = int(input('Enter second number: '))

print(car(cons(input1, input2)))
print(cdr(cons(input1, input2)))
