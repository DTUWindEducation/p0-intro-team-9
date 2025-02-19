def clean_pitch(x, status):
    for it, value in enumerate(status):
        if value == 1 or (90 < x[it] or x[it] < 0 ):
            x[it] = -999
    return x

def square_list(list):
    return [i**2 for i in list]

def goldilocks(length):
    if length < 140:
        i = ('Too short!')
    elif length > 150:
        i = ('Too large!')
    else:
        i = ('Just right!')
    return i

def greet(name):
    print("Hello, " + name + "!")

def fibonacci_stop(num):
    fib_list = []
    a, b = 0, 1
    while a < num:
        fib_list.append(a)
        a, b = b, a + b
    print(f"The Fibonacci values up to {num} is: {fib_list}")
    return fib_list
    